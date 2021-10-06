#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_map_of_highest_peak.py
@Author   : Harsh Parikh
@Date     : 10/2/21 10:59 PM

1765. Map of Highest Peak

You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

If isWater[i][j] == 0, cell (i, j) is a land cell.
If isWater[i][j] == 1, cell (i, j) is a water cell.
You must assign each cell a height in a way that follows these rules:

The height of each cell must be non-negative.
If the cell is a water cell, its height must be 0.
Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
Find an assignment of heights such that the maximum height in the matrix is maximized.

Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.



Example 1:



Input: isWater = [[0,1],[0,0]]
Output: [[1,0],[2,1]]
Explanation: The image shows the assigned heights of each cell.
The blue cell is the water cell, and the green cells are the land cells.
Example 2:



Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
Output: [[1,1,0],[0,1,1],[1,2,2]]
Explanation: A height of 2 is the maximum possible height of any assignment.
Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.
"""

import collections


class Solution:
    def highestPeak(self, isWater):

        def is_inbound(i, j, r, c):
            return 0 <= i < r and 0 <= j < c

        def get_neighs(i, j, r, c):
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            neighbors = []
            for x, y in dirs:
                new_r, new_c = i + x, j + y

                if is_inbound(new_r, new_c, r, c):
                    neighbors.append((new_r, new_c))

            return neighbors

        num_rows = len(isWater)
        num_cols = len(isWater[0])
        height = [[-1] * num_cols for i in range(num_rows)]  # heights

        queue = collections.deque([])

        for i in range(num_rows):
            for j in range(num_cols):
                if isWater[i][j]:
                    queue.append((i, j))
                    height[i][j] = 0

        if not queue:
            return isWater

        while queue:
            r, c = queue.popleft()

            neighs = get_neighs(r, c, num_rows, num_cols)

            for nr, nc in neighs:
                if height[nr][nc] == -1:
                    height[nr][nc] = height[r][c] + 1
                    queue.append((nr, nc))

        return height
