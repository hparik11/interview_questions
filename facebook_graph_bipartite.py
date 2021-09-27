#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_graph_bipartite.py
@Author   : Harsh Parikh
@Date     : 9/13/21 4:13 PM

785. Is Graph Bipartite?
Share
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.



Example 1:


Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
Example 2:


Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
"""


# O(E + V)
class Solution_Graph_Coloring:
    """
    Color a node blue if it is part of the first set, else red.
    We should be able to greedily color the graph if and only if it is bipartite:
    one node being blue implies all it's neighbors are red, all those neighbors are blue, and so on.


    """
    from collections import deque

    def isBipartite(self, graph):
        color = {}
        for node in range(len(graph)):
            if node not in color:
                queue = deque([node])
                color[node] = 0
                while queue:
                    node = queue.popleft()
                    for nei in graph[node]:
                        if nei not in color:
                            queue.append(nei)
                            color[nei] = 1 if color[node] == 0 else 0  # color[node] ^ 1
                        elif color[nei] == color[node]:
                            return False
        return True


class Solution_UnionFind:
    def __init__(self):
        self.rank = [0] * num_nodes
        self.parent_arr = [i for i in range(num_nodes)]

    def isBipartite(self, graph):
        num_nodes = len(graph)

        for node in range(num_nodes):
            neighbors = graph[node]
            for neighbor in neighbors:
                if self.find(node) == self.find(neighbor):
                    return False
                self.union(neighbor, neighbors[0])
        return True

    def union(self, node_one, node_two):
        root_node_one = self.find(node_one)
        root_node_two = self.find(node_two)

        if root_node_one == root_node_two:
            return False

        if self.rank[root_node_one] > self.rank[root_node_two]:
            self.parent_arr[root_node_two] = root_node_one
        elif self.rank[root_node_one] < self.rank[root_node_two]:
            self.parent_arr[root_node_one] = root_node_two
        else:
            self.parent_arr[root_node_one] = root_node_two
            self.rank[root_node_two] += 1

        return True

    def find(self, node):
        if self.parent_arr[node] != node:
            self.parent_arr[node] = self.find(self.parent_arr[node])
        return self.parent_arr[node]
