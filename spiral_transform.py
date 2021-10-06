"""
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        row_start = 0
        row_end = len(matrix) - 1

        col_start = 0
        col_end = len(matrix[0]) - 1

        res = []
        while row_start <= row_end and col_start <= col_end:

            # right
            for j in range(col_start, col_end + 1):
                res.append(matrix[row_start][j])
            row_start += 1

            # down
            for i in range(row_start, row_end + 1):
                res.append(matrix[i][col_end])
            col_end -= 1

            # left
            if row_start <= row_end:
                for j in range(col_end, col_start - 1, -1):
                    res.append(matrix[row_end][j])

                row_end -= 1

            # up
            if col_start <= col_end:
                for i in range(row_end, row_start - 1, -1):
                    res.append(matrix[i][col_start])
                col_start += 1

        return res
