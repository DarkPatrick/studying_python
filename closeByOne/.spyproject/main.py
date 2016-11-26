# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:14:26 2016

@author: Egor

close by one algorithm
"""


import formal_concepts as fc


def findFormalConcepts():
    # input number of objects (rows) and attributes (columns)
    num_of_objs = eval(input("Enter number of objects: "))

    # prepare an empty matrix for early initialization
    context = list([])

    # TODO: make reading from files
    for i in range(num_of_objs):
        context.append(list([]))
        # input the full rows
        rd_str = input("enter attributes for " + str(i) + " object: ")
        # each value must be separated with space from the neighborhood
        temp_list = rd_str.split()
        for j in temp_list:
            # and only 0 and 1 are allowed
            if (('0' == j) or ('1' == j)):
                context[i].append(int(j))

    # create an object of concept lattice
    # and give it the matrix for future calculations
    concept_lattice = fc.ConceptLattice(matrix=context)
    # compute all formal concepts
    concept_lattice.calculateFormalConcepts()

    return concept_lattice


def findConceptRules(concept_lattice):
    pass


concept_lattice = findFormalConcepts()
concept_lattice.findContentRules(support=0.5)
print(concept_lattice.content_rules)
# print(concept_lattice)
# findConceptRules(concept_lattice)
