#!/usr/bin/env python
# coding:utf-8
"""
@FileName : amazon_sorting_center.py
@Author   : Harsh Parikh
@Date     : 7/20/21 5:24 PM

You're given a 2d matrix, where '1' means an amazon sorting center, and 0 means a normal road.
Amazon needs to open a new sorting center, and its must be as far as it can from other sorting centers.

Write a function to return the max distance from all sorting centers. Here, distance means Manhattan distance,
i.e. distance(p1, p2) = |x1 - x2| + |y1 - y2| where p is a point (x, y).

Example
Input:

1 0 1
0 0 0
1 0 1
Output:

2
Explanation - (1, 1) is at distance 2 from all sorting centers.

Example 2
Input

1 0 0
0 0 0
0 0 0
Output: 4

Explanation: (2,2) is farthest from (0,0) and distance is |2-0| + |2-0| = 4

****************************************************************************************************************************************************************************************************************************
****************************************************************************************************************************************************************************************************************************


547. Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly
connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.



Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
"""

from typing import List
import collections


class UnionFind(object):
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0 for _ in range(n)]
        self.numberOfFriendsCircle = n

    def union(self, a, b):
        xr, yr = self.find(a), self.find(b)

        if xr == yr:
            return
        elif self.rank[xr] < self.rank[yr]:
            self.parents[xr] = yr
            self.rank[yr] += 1
        else:
            self.parents[yr] = xr
            self.rank[xr] += 1

        self.numberOfFriendsCircle -= 1

    def find(self, a):
        while self.parents[a] != a:
            a = self.parents[a]
        return a


class Solution1(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        if not M:
            return 0

        s = len(M)

        uf = UnionFind(s)
        for r in range(s):
            for c in range(r, s):
                if M[r][c] == 1:
                    uf.union(r, c)

        print(uf.parents)
        # print(uf.rank)
        return len(set([uf.find(i) for i in range(s)]))


class Solution:
    def amazonphonescreen(self, arr):
        centers = []
        output = 0
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == 1:
                    arr[i][j] = 0
                    centers.append([i, j])
                elif arr[i][j] == 0:
                    arr[i][j] = float('inf')

        for coords in centers:
            dfs(arr, coords[0], coords[1], 0)
            # bfs(arr, coords[0], coords[1])

        print(arr)
        for row in arr:
            output = max(output, max(row))
        return output

    def dfs(arr, i, j, dist):
        if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[i]) or dist > arr[i][j]:
            return
        arr[i][j] = dist
        dfs(arr, i - 1, j, dist + 1)
        dfs(arr, i, j + 1, dist + 1)
        dfs(arr, i + 1, j, dist + 1)
        dfs(arr, i, j - 1, dist + 1)

    def bfs(arr, i, j):
        q = [[i, j]]
        seen = set()
        dist = 0
        while q:
            length = len(q)
            for _ in range(length):
                curr = q.pop(0)
                i = curr[0]
                j = curr[1]
                if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[i]) or (i, j) in seen:
                    continue
                seen.add((i, j))
                arr[i][j] = min(arr[i][j], dist)
                q.append([i - 1, j])
                q.append([i, j + 1])
                q.append([i + 1, j])
                q.append([i, j - 1])
            dist += 1


if __name__ == '__main__':
    # s = Solution()
    # print(s.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))

    s = Solution1()
    print(s.findCircleNum([[1, 0, 0, 1],
                           [0, 1, 1, 0],
                           [0, 1, 1, 1],
                           [1, 0, 1, 1]]))

    print(s.findCircleNum([[1, 0, 1],
                           [0, 0, 0],
                           [1, 0, 1]]))
