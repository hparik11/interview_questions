#!/usr/bin/env python
# coding:utf-8
"""
@FileName : find_path_with_greatest_product.py
@Author   : Harsh Parikh
@Date     : 8/5/21 1:34 AM

Given a matrix, find the path from top left to bottom right with the greatest product by moving only down and right.

eg.

[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

1 -> 4 -> 7 -> 8 -> 9
2016

[-1, 2, 3]
[4, 5, -6]
[7, 8, 9]

-1 -> 4 -> 5 -> -6 -> 9
1080

"""


def find_path_with_greatest_product(matrix):
    numRows = len(matrix)
    numCols = len(matrix[0])

    maxCache = [[float('-inf') for _ in range(numCols)] for _ in range(numRows)]
    minCache = [[float('inf') for _ in range(numCols)] for _ in range(numRows)]

    for i in range(numRows):
        for j in range(numCols):
            if i == 0 and j == 0:
                maxCache[i][j] = matrix[i][j]
                minCache[i][j] = matrix[i][j]
            elif i == 0:
                maxCache[i][j] = max(maxCache[i][j - 1] * matrix[i][j], minCache[i][j - 1] * matrix[i][j])
                minCache[i][j] = min(maxCache[i][j - 1] * matrix[i][j], minCache[i][j - 1] * matrix[i][j])
            elif j == 0:
                maxCache[i][j] = max(maxCache[i - 1][j] * matrix[i][j], minCache[i - 1][j] * matrix[i][j])
                minCache[i][j] = max(maxCache[i - 1][j] * matrix[i][j], minCache[i - 1][j] * matrix[i][j])
            else:
                maxCache[i][j] = max(maxCache[i - 1][j] * matrix[i][j], minCache[i - 1][j] * matrix[i][j],
                                     maxCache[i][j - 1] * matrix[i][j], minCache[i][j - 1] * matrix[i][j])
                minCache[i][j] = min(maxCache[i - 1][j] * matrix[i][j], minCache[i - 1][j] * matrix[i][j],
                                     maxCache[i][j - 1] * matrix[i][j], minCache[i][j - 1] * matrix[i][j])

    return maxCache[numRows - 1][numCols - 1]


if __name__ == '__main__':
    print(find_path_with_greatest_product([[1, 2, 3],
                                           [4, 5, 6],
                                           [7, 8, 9]]))

    print(find_path_with_greatest_product([[-1, 2, 3],
                                           [4, 5, -6],
                                           [7, 8, 9]]))
