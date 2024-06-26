#!/usr/bin/env python
# coding:utf-8
"""
@FileName : remove_max_edges_to_keep_graph_traversal.py
@Author   : Harsh Parikh
@Date     : 8/29/21 8:32 PM

1579. Remove Max Number of Edges to Keep Graph Fully Traversable
Alice and Bob have an undirected graph of n nodes and 3 types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can by traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if it's impossible for the graph to be fully traversed by Alice and Bob.



Example 1:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:



Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
"""

from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1 for _ in range(n)]
        self.connected_edges = 0

    def find(self, node):
        while self.parents[node] != node:
            node = self.parents[node]

        return node

    def union(self, node1, node2):
        parent_node1 = self.find(node1)
        parent_node2 = self.find(node2)

        if parent_node1 == parent_node2:
            return False

        if self.ranks[parent_node1] < self.ranks[parent_node2]:
            self.parents[parent_node1] = parent_node2
            self.ranks[parent_node2] += 1
        else:
            self.parents[parent_node2] = parent_node1
            self.ranks[parent_node1] += 1

        self.connected_edges += 1

        return True


"""
Complexity

Time complexity: O(N)
Space complexity: O(N)
"""


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        redundant_edges = 0
        unionFind_alice = UnionFind(n + 1)
        unionFind_bob = UnionFind(n + 1)

        # Find redundant edges for both traversal or type = 3
        for edge_type, node1, node2 in edges:
            if edge_type == 3:
                if not unionFind_alice.union(node1, node2) or not unionFind_bob.union(node1, node2):
                    redundant_edges += 1

        # Find redundant edges for individual traversal or type = 1 or 2
        for edge_type, node1, node2 in edges:
            if edge_type == 1:
                if not unionFind_alice.union(node1, node2):
                    redundant_edges += 1

            elif edge_type == 2:
                if not unionFind_bob.union(node1, node2):
                    redundant_edges += 1

        return redundant_edges if unionFind_alice.connected_edges == n - 1 and unionFind_bob.connected_edges == n - 1 else -1
