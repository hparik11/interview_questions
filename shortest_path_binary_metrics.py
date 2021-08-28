# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: shortest_path_binary_metrics.py
# @Date:   10/13/20, Tue
"""
1091. Shortest Path in Binary Matrix

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.



Example 1:

Input: [[0,1],[1,0]]


Output: 2

Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]


Output: 4



Note:

1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1
"""
from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        queue = deque([(0, 0)])

        grid[0][0] = 1
        DIRECTIONS = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        visited = set()
        depth = 1
        while len(queue):
            children = len(queue)

            for _ in range(children):
                i, j = queue.popleft()
                if i == row - 1 and j == col - 1:
                    return depth

                visited.add((i, j))

                for r, c in DIRECTIONS:
                    x = i + r
                    y = j + c
                    if 0 <= x < row and 0 <= y < col and grid[x][y] == 0 and (x, y) not in visited:
                        # grid[x][y] = 1
                        queue.append((x, y))

            depth += 1

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.shortestPathBinaryMatrix([[0, 1], [1, 0]]))
    print(s.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
    print(s.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))
