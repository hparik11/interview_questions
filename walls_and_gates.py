#!/usr/bin/env python
# coding:utf-8
"""
@FileName : walls_and_gates.py
@Author   : Harsh Parikh
@Date     : 7/15/21 11:30 AM

286. Walls and Gates

You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.



Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
Example 3:

Input: rooms = [[2147483647]]
Output: [[2147483647]]
Example 4:

Input: rooms = [[0]]
Output: [[0]]
"""

from typing import List
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        def is_valid(i, j, row, col):
            return 0 <= i < row and 0 <= j < col

        row = len(rooms)
        col = len(rooms[0])

        queue = deque([])

        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        while queue:
            currentRow, currentCol = queue.popleft()

            dist = rooms[currentRow][currentCol] + 1

            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                r = currentRow + dx
                c = currentCol + dy
                if is_valid(r, c, row, col) and rooms[r][c] == 2147483647:
                    rooms[r][c] = min(dist, rooms[r][c])
                    queue.append((r, c))


if __name__ == '__main__':
    s = Solution()
    rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],
             [2147483647, -1, 2147483647, -1],
             [0, -1, 2147483647, 2147483647]]

    s.wallsAndGates(rooms)
    print(rooms)
