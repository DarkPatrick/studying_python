# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 22:32:31 2016

@author: Egor
"""

# костанта под бесконечность
# тут вроде есть бесконечность, но хз
infinity = -1

# количество веhiby в графе
graph_size = 3

# номер стартовой вершины
start_vertex = 0

# будем хранить пары {номер вершины: расстояние_до_неё_от_стартовой} в виде словаря
distances = {i: infinity for i in range(graph_size)}

# расстояние от начальной вершины до неё самой равно 0
distances[start_vertex] = 0

