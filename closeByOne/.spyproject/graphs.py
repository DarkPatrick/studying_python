# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 09:22:24 2016

@author: Egor
"""


class Graph:
    def __init__(self):
        self.edges = dict()

    def setEdge(self, v1, v2, weight):
        if (v1 < v1):
            self.edges[(v1, v2)] = weight
        else:
            self.edges[(v2, v1)] = weight

    def getEdge(self, v1, v2):
        try:
            if (v1 < v2):
                return self.edges[(v1, v2)]
            else:
                return self.edges[(v2, v1)]
        except:
            return {}
