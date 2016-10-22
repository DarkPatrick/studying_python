# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:14:26 2016

@author: Egor
"""

import numpy as np

num_of_objs = eval(input("Enter number of objects: "))
num_of_atts = eval(input("Enter number of attributes: "))

context = np.zeros((num_of_objs, num_of_atts), dtype=int)

for i in range(num_of_objs):
    for j in range(num_of_atts):
        context[i][j] = eval(
            input("(" + str(i) + ", " + str(j) + "): ")
        )

