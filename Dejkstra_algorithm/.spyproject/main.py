# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 22:32:31 2016

@author: Egor
"""


# constant to define lack of the edge
infinity = -1


# function to find minimun element and it's value in the array
# TODO: find minimum by splitting in two halfs
def findMin(data_array):
    min_val = [0, data_array[0]]
    for i in range(len(data_array)):
        if ((infinity != data_array[i]) and
                ((data_array[i] < min_val[1]) or
                 (infinity == min_val[1]))):
            min_val = [i, data_array[i]]
    return min_val


# number of vertices in our graph
graph_size = int(input("enter number of vertices: "))

# list for distances to find minimum of the distances left
# and list of real best way
# TODO: learn how to use arrays
distances = [infinity] * graph_size
true_dist = [infinity] * graph_size

# initialisation of the vertex-edge incidence matrix
graph = [
         [infinity for i in range(graph_size)]
         for j in range(graph_size)
        ]

# input matrix values
# -1 stands for infinity
# no check for correctness
# TODO: try to load data from the file
for i in range(graph_size):
    for j in range(i + 1, graph_size):
        graph[i][j] = int(input("enter distance for (" +
                                str(i) + ", " + str(j) + "): "))
        graph[j][i] = graph[i][j]

# a number of vertex to start from
start_vertex = int(input("enter start vertex: "))

# some initialisation in distance's lists
for i in range(graph_size):
    distances[i] = graph[start_vertex][i]
    true_dist[i] = graph[start_vertex][i]

# set distance to the start vertex equals 0
# 'cause we don't need to find it. (and because it's equal to zero)
true_dist[start_vertex] = 0

# find minimun value and it's vertex number
min_val = findMin(distances)

# main part of the program
# TODO: find out, why i cant assign min_val right inside while loop
while (min_val[1] > 0):
    # set value in the distance list to 0,
    # so program won't use it any more
    distances[min_val[0]] = infinity
    for i in range(graph_size):
        # check all vertices which have edges with the current
        if (infinity != graph[min_val[0]][i]):
            # if new distance is better (less) than the old one
            if (
                (infinity == true_dist[i]) or
                (true_dist[i] > min_val[1] +
                 graph[min_val[0]][i])
            ):
                # reassign it
                true_dist[i] = min_val[1] + graph[min_val[0]][i]
    # find another min distance
    min_val = findMin(distances)

# print results
for i in range(graph_size):
    if (infinity == true_dist[i]):
        print("inf")
    else:
        print(true_dist[i])
