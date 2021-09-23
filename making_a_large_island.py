#!/usr/bin/env python
# coding:utf-8
"""
@FileName : making_a_large_island.py
@Author   : Harsh Parikh
@Date     : 7/23/21 11:38 PM

827. Making A Large Island

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.



Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
"""

from collections import deque


class Solution:
    def largestIsland(self, grid) -> int:

        N = len(grid)
        DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        address = {}

        def dfs(row, column, island_id):
            queue = deque([(row, column, island_id)])
            visited.add((row, column))
            area = 1
            while queue:
                row, column, island_id = queue.pop()
                address[(row, column)] = island_id
                for direction in DIRECTIONS:
                    r, c = row + direction[0], column + direction[1]
                    if r in range(N) and c in range(N) and grid[r][c] == 1 and (r, c) not in visited:
                        queue.append((r, c, island_id))
                        visited.add((r, c))
                        area += 1
            return area

        visited = set()
        area = {}
        island_id = 0

        for row in range(N):
            for column in range(N):
                if grid[row][column] == 1 and (row, column) not in visited:
                    area[island_id] = dfs(row, column, island_id)
                    island_id += 1

        if len(address.keys()) == N ** 2:
            return N ** 2

        largest_area = 1
        for row in range(N):
            for column in range(N):
                if grid[row][column] == 0:
                    neighbours = set()
                    large_area = 1
                    for direction in DIRECTIONS:
                        r, c = row + direction[0], column + direction[1]
                        if r in range(N) and c in range(N) and grid[r][c] == 1 and address[(r, c)] not in neighbours:
                            neighbours.add(address[(r, c)])
                            large_area += area[address[(r, c)]]
                    largest_area = max(largest_area, large_area)

        return largest_area


if __name__ == '__main__':
    s = Solution()
    print(s.largestIsland([[1, 0], [0, 1]]))
