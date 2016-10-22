# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:14:26 2016

@author: Egor
"""


import formal_concepts as fc


num_of_objs = eval(input("Enter number of objects: "))
num_of_atts = eval(input("Enter number of attributes: "))

context = list([])

for i in range(num_of_objs):
    context.append(list([]))
    """
    for j in range(num_of_atts):
        context[i].append(
            eval(input("(" + str(i) + ", " + str(j) + "): "))
        )
    """
    rd_str = input("enter attributes for " + str(i) + " object: ")
    temp_list = rd_str.split()
    for j in temp_list:
        if (('0' == j) or ('1' == j)):
            context[i].append(int(j))


concept_lattice = fc.ConceptLattice(matrix=context)
concept_lattice.calculate_formal_concepts()
print(concept_lattice)
# 101
# 110
# 101
