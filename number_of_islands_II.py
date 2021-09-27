#!/usr/bin/env python
# coding:utf-8
"""
@FileName : number_of_islands_II.py
@Author   : Harsh Parikh
@Date     : 8/19/21 1:34 AM

305. Number of Islands II

You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:


Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
Explanation:
Initially, the 2d grid is filled with water.
- Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
- Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
- Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
- Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.
Example 2:

Input: m = 1, n = 1, positions = [[0,0]]
Output: [1]
"""

from collections import defaultdict


class UnionFind:
    def __init__(self, numRows, numCols):
        self.parents = defaultdict(tuple)
        self.ranks = defaultdict(int)
        self.numberOfIslands = 0
        self.numRows = numRows
        self.numCols = numCols

    def is_valid(self, i, j):
        return 0 <= i < self.numRows and 0 <= j < self.numCols

    def find(self, location):
        while self.parents[location] != location:
            location = self.parents[location]

        return location

    def union(self, r1, c1, r2, c2):
        parents_1 = self.find((r1, c1))
        parents_2 = self.find((r2, c2))

        if parents_1 == parents_2:
            return False

        elif self.ranks[parents_1] <= self.ranks[parents_2]:
            self.parents[parents_1] = parents_2
            self.ranks[parents_1] += 1
        else:
            self.parents[parents_2] = parents_1
            self.ranks[parents_1] += 1

        return True

    def add_island(self, row, col):
        if (row, col) in self.parents or not self.is_valid(row, col):
            return

        self.parents[(row, col)] = (row, col)
        self.numberOfIslands += 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for each in directions:
            neigh_x = row + each[0]
            neigh_y = col + each[1]

            # If neighbors in parents then we already found an island
            # so union them
            if self.is_valid(neigh_x, neigh_y) and (neigh_x, neigh_y) in self.parents:
                if self.union(row, col, neigh_x, neigh_y):
                    self.numberOfIslands -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        if not positions:
            return []

        answer = []
        uf = UnionFind(m, n)

        for pos in positions:
            uf.add_island(pos[0], pos[1])
            answer.append(uf.numberOfIslands)

        return answer
