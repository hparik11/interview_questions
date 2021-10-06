# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: longest_increasing_path_matrix.py
# @Date:   9/23/20, Wed

"""
329. Longest Increasing Path in a Matrix
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
import collections
from typing import List


class Solution:
    def is_valid(self, x, y, row, cols):
        return 0 <= x < row and 0 <= y < cols

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        def dfs(i, j, row1, col1, visited, dp, matrix):
            if dp[i][j] != 0:
                return dp[i][j]

            visited[i][j] = True
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            count = 1
            for x, y in directions:
                new_x, new_y = i + x, j + y
                if self.is_valid(new_x, new_y, row1, col1) \
                        and not visited[new_x][new_y] \
                        and matrix[i][j] < matrix[new_x][new_y]:
                    count = max(count, 1 + dfs(new_x, new_y, row1, col1, visited, dp, matrix))

            dp[i][j] = count
            visited[i][j] = False
            return count

        row = len(matrix)
        col = len(matrix[0])

        visited = [[False] * col for _ in range(row)]
        dp = [[0] * col for _ in range(row)]

        maxCount = 0
        for i in range(row):
            for j in range(col):
                if dp[i][j] == 0:
                    maxCount = max(maxCount, dfs(i, j, row, col, visited, dp, matrix))

        print(dp)
        return maxCount

    def longestIncreasingPath2(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        if rows == 0:
            return 0

        cols = len(matrix[0])
        indegree = [[0 for x in range(cols)] for y in range(rows)]
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        for x in range(rows):
            for y in range(cols):
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]
                    if self.is_valid(nx, ny, rows, cols):
                        if matrix[nx][ny] < matrix[x][y]:
                            indegree[x][y] += 1

        queue = collections.deque()
        for x in range(rows):
            for y in range(cols):
                if indegree[x][y] == 0:
                    queue.append((x, y))

        path_len = 0
        while queue:
            sz = len(queue)
            for i in range(sz):
                x, y = queue.popleft()
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]
                    if self.is_valid(nx, ny, rows, cols):
                        if matrix[nx][ny] > matrix[x][y]:
                            indegree[nx][ny] -= 1
                            if indegree[nx][ny] == 0:
                                queue.append((nx, ny))
            path_len += 1
        return path_len


if __name__ == '__main__':
    s = Solution()
    print(s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4)
    print(s.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4)
    print(s.longestIncreasingPath([[1, 2]]) == 2)
