"""
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0,
set its entire row and column to 0's, and return the matrix.

You must do it in place.



Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        mark_rows = set()
        mark_cols = set()

        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == 0:
                    mark_rows.add(i)
                    mark_cols.add(j)

        for i in range(num_rows):
            for j in range(num_cols):
                if i in mark_rows or j in mark_cols:
                    matrix[i][j] = 0
