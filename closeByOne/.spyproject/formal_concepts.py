# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 17:06:40 2016

@author: Egor
"""

import copy as cp


class Concept:
    def __init__(self, objects=[], attributes=[]):
        self.objects = cp.deepcopy(objects)
        self.attributes = cp.deepcopy(attributes)

    def __str__(self):
        return("{" + str(self.objects) + ", " + str(self.attributes) + "}")

    def __eq__(self, concept):
        if ((self.objects == concept.objects) or
                (self.attributes == concept.attributes)):
            return True
        else:
            return False

    def __ne__(self, concept):
        return(not (self == concept))


class ConceptLattice:
    class ConceptMatrix:
        def __init__(self, matrix):
            self.matrix = cp.deepcopy(matrix)
            self.num_of_objs = len(self.matrix)
            if (self.num_of_objs > 0):
                self.num_of_atts = len(self.matrix[0])
            self.objects = list([])
            self.attributes = list([])
            for i in range(self.num_of_objs):
                self.objects.append(
                    set({
                         j for j in range(self.num_of_atts)
                         if (1 == matrix[i][j])
                    }))
            for i in range(self.num_of_atts):
                self.attributes.append(
                    set({
                         j for j in range(self.num_of_objs)
                         if (1 == matrix[j][i])
                    }))

        def __str__(self):
            return(str(self.matrix))

        def dashObjects(self, objects_nums):
            attributes = set({i for i in range(self.num_of_atts)})
            for i in objects_nums:
                attributes &= self.objects[i]
            return attributes

        def dashAttributes(self, attributes_nums):
            objects = set({i for i in range(self.num_of_objs)})
            # print(attributes_nums)
            for i in attributes_nums:
                objects &= self.attributes[i]
            return objects

    def __init__(self, matrix=[]):
        self.num_of_concepts = 0
        self.concepts = []
        self.concept_matrix = self.ConceptMatrix(matrix)

    def __str__(self):
        res_str = ''
        for i in self.concepts:
            res_str += i.__str__() + '\n'
        return(res_str)

    def __add__(self, concept):
        for i in self.concepts:
            if (i == concept):
                break
        else:
            self.concepts.append(concept)

    def calculate_formal_concepts(self):
        def process(set_of_objs, cur_obj, concept):
            for i in range(cur_obj):
                if (i in (set_of_objs - set(concept.objects))):
                    break
            else:
                self.__add__(concept)
                for i in range(cur_obj + 1, self.concept_matrix.num_of_objs):
                    if (i not in set_of_objs):
                        set_of_objs = set(concept.objects) | set({i})
                        cur_obj_atts = set(
                            concept.attributes
                            ) & self.concept_matrix.dashObjects([i])
                        cur_obj_dbl_dash = self.concept_matrix.dashAttributes(
                            list(cur_obj_atts)
                            )
                        concept = Concept(cur_obj_dbl_dash, cur_obj_atts)
                        process(set_of_objs, i, concept)

        for i in range(self.concept_matrix.num_of_objs):
            cur_obj_set = set({i})
            cur_obj = i
            cur_obj_atts = self.concept_matrix.dashObjects([i])
            cur_obj_dbl_dash = self.concept_matrix.dashAttributes(
                                    list(cur_obj_atts))
            concept = Concept(cur_obj_dbl_dash, cur_obj_atts)
            process(cur_obj_set, cur_obj, concept)
