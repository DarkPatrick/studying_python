# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 22:32:31 2016

@author: Egor
"""


import numpy as np


# костанта под бесконечность
# тут вроде есть бесконечность, но хз
infinity = -1


# ввод имени файла в котором хранится граф
graph_file_name = input("введите имя файла с графом: ")


# открытие файла для чтения
graph_file = open(graph_file_name, 'r')
i = 0
for line in graph_file:
    file_str = line
    if (0 == i):
# количество вершин в графе
        graph_size = int(file_str)
# массив вешин из списков расстояний до тех вершин, с которыми имеется связь
        graph = np.array({} for i in range(graph_size))
    else:
        line_str_arr = file_str.split(' ');
        line_int_arr = [int(num) for num in line_str_arr]
        for j in line_int_arr:
            #if ()
    i += 1


# номер стартовой вершины
start_vertex = input("введите номер вершины: ")

# будем хранить пары {номер вершины: расстояние_до_неё_от_стартовой} в виде словаря
distances = {i: infinity for i in range(graph_size)}

# расстояние от начальной вершины до неё самой равно 0
distances[start_vertex] = 0

