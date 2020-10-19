"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""

from typing import List


class Solution:
    def is_valid(row, col, m, n):
        if row < 0 or col < 0 or row >= m or col >= n:
            return False
        return True

    def binaryArraySearching(self, matrix: List[int], target: int):
        low = 0
        high = len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2
            if matrix[mid] == target:
                return True
            elif matrix[mid] < target:
                low += 1
            else:
                high -= 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        if not matrix[0]:
            return False

        row, col = 0, 0
        m, n = len(matrix), len(matrix[0])
        # while True:
        #     if is_valid(row, col, m, n):
        #         currValue = matrix[row][col]
        #         if currValue == target:
        #             return True
        #         elif currValue < target:
        #             new_row, col = row + 1, col
        #             if is_valid(new_row, col, m, n):
        #                 if binaryArraySearching(matrix[])


class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        if not matrix[0]:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False


if __name__ == "__main__":
    print(Solution1().searchMatrix(
        [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
