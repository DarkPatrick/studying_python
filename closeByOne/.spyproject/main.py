# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:14:26 2016

@author: Egor
"""


import numpy as np


def dash(rows, num_of_atts):
    attributes = set({i for i in range(num_of_atts)})
    for i in rows:
        attributes = attributes.intersection(i)
    return attributes


def doubleDash(rows, num_of_atts, num_of_objs):
    objects = set({i for i in range(num_of_objs)})
    attributes = dash(rows, num_of_atts)
    for i in attributes:
        temp_obj = set({j for j in range(num_of_atts) if context[j][i] == 1})
        objects = objects.intersection(temp_obj)
    return objects


def findFormalConcept(cur_obj_set, cur_obj_num, closure_test):
    pass


num_of_objs = eval(input("Enter number of objects: "))
num_of_atts = eval(input("Enter number of attributes: "))

context = np.zeros((num_of_objs, num_of_atts), dtype=int)
L = set({})

for i in range(num_of_objs):
    for j in range(num_of_atts):
        context[i][j] = eval(
            input("(" + str(i) + ", " + str(j) + "): ")
        )

for i in range(num_of_objs):
    obj_set = set({j for j in range(num_of_atts) if context[i][j] == 1})
    # findFormalConcept()
