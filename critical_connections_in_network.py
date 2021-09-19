#!/usr/bin/env python
# coding:utf-8
"""
@FileName : critical_connections_in_network.py
@Author   : Harsh Parikh
@Date     : 8/9/21 8:41 PM

1192. Critical Connections in a Network

There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.



Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
"""

from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        """
        Iterate over the edges, remove an edge and run a DFS on the remaining graph
        (exclusing the edge you just removed) to see whether you'd still be able to traverse the entrie graph.
        If (len(visited) != number of nodes), the removed edge is a bridge.
        """

        def dfs(graph, node, seen):
            if node in seen:
                return

            seen.add(node)

            for neigh in graph[node]:
                if neigh not in seen:
                    dfs(graph, neigh, seen)

        if len(connections) <= 1:
            return connections

        critical_connections = []

        for removing_edge in connections:
            adj_list = defaultdict(list)
            seen = set()

            for connection in connections:
                if connection != removing_edge:
                    node = connection[0]
                    neigh = connection[1]

                    adj_list[node].append(neigh)
                    adj_list[neigh].append(node)

            dfs(adj_list, node, seen)

            if len(seen) != n:
                critical_connections.append(removing_edge)

        return critical_connections
