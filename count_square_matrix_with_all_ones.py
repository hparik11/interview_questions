#!/usr/bin/env python
# coding:utf-8
"""
@FileName : count_square_matrix_with_all_ones.py
@Author   : Harsh Parikh
@Date     : 9/5/21 2:18 AM

1277. Count Square Submatrices with All Ones

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.



Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.
"""


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        """
        https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/643429/Python-DP-Solution-%2B-Thinking-Process-Diagrams-(O(mn)-runtime-O(1)-space)
        """

        rows = len(matrix)
        cols = len(matrix[0])

        total_square_submatrix = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    # Cases with first row or first col
                    if i == 0 or j == 0:
                        # The 1 cells are square on its own
                        total_square_submatrix += 1

                    else:
                        matrix[i][j] = 1 + min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1])
                        total_square_submatrix += matrix[i][j]

        return total_square_submatrix
