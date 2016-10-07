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
            if (line_int_arr[j] > infinity):
                graph[i - 1].append(j)
                graph[i - 1].append(line_int_arr[j])
    if (len(line_int_arr) > 1):
        i += 1


# номер стартовой вершины
start_vertex = input("введите номер вершины из которой надо искать пути: ")

# будем хранить пары {номер вершины: расстояние_до_неё_от_стартовой} в виде словаря
distances = {i: infinity for i in range(graph_size)}


# начало самого алгоритма
cur_vertex = start_vertex
it = iter(graph[cur_vertex])
min_dist_vert = it.next()
min_dist_val = it.next()
while (graph[cur_vertex]):
    dist_vert = it.next()
    dist_val = it.next()
    if (dist_val < min_dist_val):
        min_dist_vert = dist_vert
        min_dist_val = dist_val
    if ((infinity == distances[dist_vert]) || (distances[cur_vertex] 
+ distances[dist_vert] < distances[dist_vert])):
        distances[dist_vert] = distances[cur_vertex]  + distances[dist_vert]
    
