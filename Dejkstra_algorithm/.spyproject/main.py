# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 22:32:31 2016

@author: Egor
"""


infinity = 0


def findMin(data_array):
    min_val = [0, data_array[0]]
    for i in range(data_array):
        if ((infinity != data_array[i]) and
                ((data_array[i] < min_val[0]) or
                 (infinity == min_val[0]))):
            min_val = [i, data_array[i]]
    return min_val


graph_size = int(input("enter number of vertices: "))

distances = [infinity] * graph_size
true_dist = [infinity] * graph_size

graph = [[infinity] * graph_size, [infinity] * graph_size]

for i in range(graph_size):
    for j in range(i + 1, graph_size):
        int(input('(' + str(i) + ', ' + str(j) +
            ')' + " enter path len: "))

start_vertex = input("enter start vertex: ")

for i in range(graph_size):
    distances[i] = graph[start_vertex, i]
    true_dist[i] = graph[start_vertex, i]

min_val = findMin(distances)

