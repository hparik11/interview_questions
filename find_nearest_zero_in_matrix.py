# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: find_nearest_zero_in_matrix.py
# @Date:   9/29/20, Tue
"""
542. 01 Matrix
Medium

1735

111

Add to List

Share
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.



Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
"""

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        def is_valid(i, j, row, col):
            if i < 0 or i > row - 1 or j < 0 or j > col - 1:
                return False
            return True

        def get_neighbors(i, j, row, col, visited):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            neighs = []
            for each in directions:
                x, y = i + each[0], j + each[1]
                if is_valid(x, y, row, col) and (x, y) not in visited:
                    neighs.append((x, y))

            return neighs

        def bfs(i, j, row, col, matrix):
            queue = deque([(i, j)])
            visited = set()
            level = 0
            while len(queue):
                for _ in range(len(queue)):
                    node = queue.popleft()
                    visited.add(node)
                    if matrix[node[0]][node[1]] == 0:
                        return level
                    else:
                        for neigh in get_neighbors(node[0], node[1], row, col, visited):
                            queue.append(neigh)

                level += 1

            return level

        if not matrix:
            return matrix
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    matrix[i][j] = bfs(i, j, row, col, matrix)

        return matrix


if __name__ == '__main__':
    s = Solution()
    print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
