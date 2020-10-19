# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: sparse_matrix_multiplication.py
# @Date:   10/2/20, Fri
"""
Sparse Matrix Multiplication
Medium

530

207

Add to List

Share
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""
from typing import List


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        def array_mul(array_a, array_b):
            result = 0
            for a, b in zip(array_a, array_b):
                result += a * b
            return result

        def getColumnData(array):
            cols = len(array[0])
            b_cols_array = []
            for i in range(cols):
                temp = []
                for j in range(len(array)):
                    temp.append(array[j][i])
                b_cols_array.append(temp)

            return b_cols_array

        B_prime = getColumnData(B)

        rows = len(A)
        cols = len(B_prime)
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = array_mul(A[i], B_prime[j])

        return matrix


if __name__ == '__main__':
    s = Solution()
    print(s.multiply([[1, 0, 0], [-1, 0, 3]], [[7,0,0],[0,0,0],[0,0,1]]))
    print(s.multiply([[1, 0, 0], [-1, 0, 3]], [[7, 0, 1, 2], [0, 0, 0, 1], [0, 0, 1, 2]]))
