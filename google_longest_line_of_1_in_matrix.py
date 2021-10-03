#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_longest_line_of_1_in_matrix.py
@Author   : Harsh Parikh
@Date     : 10/2/21 11:46 AM

562. Longest Line of Consecutive One in Matrix

Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.

The line could be horizontal, vertical, diagonal, or anti-diagonal.



Example 1:


Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
Output: 3
Example 2:


Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
Output: 4
"""


class Solution:
    # O(mn) | O(mn)
    def longestLine1(self, mat) -> int:
        maxOnes = 0
        num_rows = len(mat)
        num_cols = len(mat[0])

        dp = [[[0, 0, 0, 0] for _ in range(num_cols)] for _ in range(num_rows)]

        for i in range(num_rows):
            for j in range(num_cols):
                if mat[i][j] == 1:
                    dp[i][j][0] = 1 + dp[i][j - 1][0] if j > 0 else 1
                    dp[i][j][1] = 1 + dp[i - 1][j][1] if i > 0 else 1
                    dp[i][j][2] = 1 + dp[i - 1][j - 1][2] if i > 0 and j > 0 else 1
                    dp[i][j][3] = 1 + dp[i - 1][j + 1][3] if i > 0 and j < num_cols - 1 else 1

                    maxOnes = max(maxOnes, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])

        return maxOnes

    # O(mn) | O(n)
    def longestLine2(self, mat) -> int:

        maxOnes = 0
        num_rows = len(mat)
        num_cols = len(mat[0])

        curr = [[0, 0, 0, 0] for _ in range(num_cols)]
        prev = [[0, 0, 0, 0] for _ in range(num_cols)]

        for i in range(num_rows):
            for j in range(num_cols):
                if mat[i][j] == 1:
                    curr[j][0] = 1 + curr[j - 1][0] if j > 0 else 1
                    curr[j][1] = 1 + prev[j][1] if i > 0 else 1
                    curr[j][2] = 1 + prev[j - 1][2] if i > 0 and j > 0 else 1
                    curr[j][3] = 1 + prev[j + 1][3] if i > 0 and j < num_cols - 1 else 1

                    maxOnes = max(maxOnes, curr[j][0], curr[j][1], curr[j][2], curr[j][3])

            prev = curr[:]
            curr = [[0, 0, 0, 0] for _ in range(num_cols)]

        return maxOnes


