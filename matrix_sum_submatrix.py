#!/usr/bin/env python
# coding:utf-8
"""
@FileName : matrix_sum_submatrix.py
@Author   : Harsh Parikh
@Date     : 8/27/21 11:58 PM
"""


def maximumSumSubmatrix(matrix, size):
    # Write your code here.
    if not matrix:
        return []

    prefixSumOfMatrix = (findPrefixSums(matrix))

    maxSubmatrixSum = float('-inf')

    for i in range(size - 1, len(matrix)):
        for j in range(size - 1, len(matrix[0])):
            total = prefixSumOfMatrix[i][j]

            # If top side is not on boarder
            touchTopBoarder = True if i - size < 0 else False
            if not touchTopBoarder:
                total -= prefixSumOfMatrix[i - size][j]

            # If left side is not on boarder
            touchLeftBoarder = True if j - size < 0 else False
            if not touchLeftBoarder:
                total -= prefixSumOfMatrix[i][j - size]

            # If top left corner available
            if not touchTopBoarder and not touchLeftBoarder:
                total += prefixSumOfMatrix[i - size][j - size]

            maxSubmatrixSum = max(maxSubmatrixSum, total)

    return maxSubmatrixSum


def findPrefixSums(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    prefixSumOfMatrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                prefixSumOfMatrix[i][j] = matrix[i][j]
            elif i == 0:
                prefixSumOfMatrix[i][j] = prefixSumOfMatrix[i][j - 1] + matrix[i][j]
            elif j == 0:
                prefixSumOfMatrix[i][j] = prefixSumOfMatrix[i - 1][j] + matrix[i][j]
            else:
                prefixSumOfMatrix[i][j] = prefixSumOfMatrix[i][j - 1] + prefixSumOfMatrix[i - 1][j] \
                                          - prefixSumOfMatrix[i - 1][j - 1] + matrix[i][j]

    return prefixSumOfMatrix
