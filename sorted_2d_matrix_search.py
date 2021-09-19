"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""

from typing import List


class Solution:

    def columnWiseSearching(self, matrix: List[int], target: int):
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

    def rowWiseSearching(self, matrix: List[List[int]], target: int):
        low = 0
        high = len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2
            midRow = matrix[mid]
            print(midRow)
            if midRow[0] > target:
                high -= 1
            elif midRow[0] <= target <= midRow[-1]:
                return self.columnWiseSearching(midRow, target)
            else:
                low += 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        if not matrix[0]:
            return False
        return self.rowWiseSearching(matrix, target)


if __name__ == "__main__":
    print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 30))
