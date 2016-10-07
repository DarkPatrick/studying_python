# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 22:32:31 2016

@author: Egor
"""


import numpy as np


# костанта под бесконечность
# тут вроде есть бесконечность, но хз
infinity = 0


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
        for j in range(len(line_int_arr)):
# yep. that is a strange condition. but only beacause i assign infinity to zero
            if (line_int_arr[j]>infinity):
                graph[i - 1].append(j)
                graph[i - 1].append(line_int_arr[j])
    if (len(line_int_arr) > 1):
        i += 1


# номер стартовой вершины
start_vertex = input("введите номер вершины из которой надо искать пути: ")

# будем хранить пары {номер вершины: расстояние_до_неё_от_стартовой} в виде словаря
distances = {i: infinity for i in range(graph_size)}


# начало самого алгоритма
min_dist_val = graph[start_vertex].pop()
min_dist_vert = graph[start_vertex].pop()

