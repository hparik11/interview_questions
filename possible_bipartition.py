#!/usr/bin/env python
# coding:utf-8
"""
@FileName : possible_bipartition.py
@Author   : Harsh Parikh
@Date     : 9/14/21 11:53 PM

886. Possible Bipartition

We want to split a group of n people (labeled from 1 to n) into two groups of any size.
Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that
the person labeled ai does not like the person labeled bi, return true if it is possible
to split everyone into two groups in this way.



Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].
Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
"""


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        graph = collections.defaultdict(list)

        for group in dislikes:
            personA = group[0]
            personB = group[1]

            graph[personA].append(personB)
            graph[personB].append(personA)

        def bfs(graph):

            color = {}
            for node in range(1, len(graph) + 1):
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

        return bfs(graph)