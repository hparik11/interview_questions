#!/usr/bin/env python
# coding:utf-8
"""
@FileName : network_delay_time.py
@Author   : Harsh Parikh
@Date     : 8/25/21 10:56 PM

743. Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times,
a list of travel times as directed edges times[i] = (ui, vi, wi),
where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel
from source to target.

We will send a signal from a given node k. Return the time it takes
for all the n nodes to receive the signal. If it is impossible for all the n nodes to
receive the signal, return -1.



Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
"""

"""
Dijkstra's shortest path algorithm is O(ElogV) where:

V is the number of vertices
E is the total number of edges
"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for (u, v, w) in times:
            graph[u].append((v, w))

        priority_queue = [(0, k)]
        shortest_path = {}
        while priority_queue:
            time, node = heapq.heappop(priority_queue)
            if node not in shortest_path:
                shortest_path[node] = time

                for neigh, neigh_time in graph[node]:
                    heapq.heappush(priority_queue, (time + neigh_time, neigh))

        if len(shortest_path) == n:
            return max(shortest_path.values())
        else:
            return -1
