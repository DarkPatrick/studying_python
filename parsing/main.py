# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:48:42 2016

@author: Egor
"""

import sys
import ply.lex as lex
import ply.yacc as yacc
import re


sys.path.insert(0, "../..")

tokens = ('NAME', 'NUMBER',)

literals = ['+', '&', '-', '|', '>', '(', ')']


def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except:
        t.value = 0
    finally:
        if (t.value not in set({0, 1})):
            t.value = 0
    return t


t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def p_statement_expr(p):
    'statement : expression'
    print(p[1])


def p_expression_binop(p):
    '''expression : expression '>' expression
                  | expression '|' expression
                  | expression '+' expression
                  | expression '&' expression'''
    if (p[2] == '>'):
        p[0] = (1 - p[1]) | p[3]
    elif (p[2] == '|'):
        p[0] = p[1] | p[3]
    elif (p[2] == '+'):
        p[0] = p[1] ^ p[3]
    elif (p[2] == '&'):
        p[0] = p[1] & p[3]


def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = 1 - p[2]


def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]


def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]


def p_error(p):
    print("Syntax error at '%s'" % p.value)


precedence = (
    ('left', '>'),
    ('left', '+', '|'),
    ('left', '&'),
    ('right', 'UMINUS'),
    )

names = {}

yacc.yacc()

lex.lex()

eq_str = input("Enter your string: ")

eq_str = re.sub(r'/\\', '&', eq_str)
eq_str = re.sub(r'\\/', '|', eq_str)
eq_str = re.sub(r'\+', '+', eq_str)
eq_str = re.sub(r'\~', '-', eq_str)
eq_str = re.sub(r'->', '>', eq_str)

eval_str = re.split(r'\-|\||\&|\+|\(|\)|\>', eq_str)
num_of_vars = 0
variables = list()
for i in range(len(eval_str)):
    if (('' != eval_str[i]) and
       (eval_str[i] is not None) and (eval_str[i] not in variables)):
        variables.append(eval_str[i])
        num_of_vars += 1

res_str = 'calculating f('
for i in range(len(variables)):
    res_str += str(variables[i])
    if (i < num_of_vars - 1):
        res_str += ', '
print(res_str + ')')

var_val = list(0 for i in range(num_of_vars))
for i in range(2 ** num_of_vars):
    temp_eq_str = eq_str
    res_str = 'f('
    for j in range(num_of_vars):
        var_val[j] = int(((1 << j) & i) > 0)
        res_str += str(var_val[j])
        if (j < num_of_vars - 1):
            res_str += ', '
        temp_eq_str = re.sub(r''.join(variables[j]),
                             str(var_val[j]), temp_eq_str)
    print(res_str + ') = ', end='')
    yacc.parse(temp_eq_str)
