#!/usr/bin/env python
# coding:utf-8
"""
@FileName : number_of_connected_components_in_graph.py
@Author   : Harsh Parikh
@Date     : 8/10/21 5:47 PM

323. Number of Connected Components in an Undirected Graph

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.



Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
"""


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0 for _ in range(n)]

    def find(self, node):
        while self.parents[node] != node:
            node = self.parents[node]

        return node

    def union(self, node1, node2):
        parent_node1 = self.find(node1)
        parent_node2 = self.find(node2)

        if parent_node1 == parent_node2:
            return

        if self.ranks[parent_node1] < self.ranks[parent_node2]:
            self.parents[parent_node1] = parent_node2
            self.ranks[parent_node2] += 1
        else:
            self.parents[parent_node2] = parent_node1
            self.ranks[parent_node1] += 1

    def count(self, n):
        return len(set([self.find(i) for i in range(n)]))


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]

            uf.union(node1, node2)

        return uf.count(n)
