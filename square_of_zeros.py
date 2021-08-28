#!/usr/bin/env python
# coding:utf-8
"""
@FileName : square_of_zeros.py
@Author   : Harsh Parikh
@Date     : 7/31/21 12:18 AM

"""


# Time O(n^4) | Space O(1)
def squareOfZeroes(matrix):
    # Write your code here.

    numRows = len(matrix)
    numCols = len(matrix[0])

    for row in range(numRows):
        for col in range(numCols):
            squareLength = 2

            while numRows - row >= squareLength and numCols - col >= squareLength:
                bottomRow = row + squareLength - 1
                rightCol = col + squareLength - 1

                if is_squared_of_zeros(matrix, row, bottomRow, col, rightCol):
                    return True

                squareLength += 1

    return False


def is_squared_of_zeros(matrix, topRow, bottomRow, leftCol, rightCol):
    for i in range(topRow, bottomRow + 1):
        if matrix[i][leftCol] != 0 or matrix[i][rightCol] != 0:
            return False

    for j in range(leftCol, rightCol + 1):
        if matrix[topRow][j] != 0 or matrix[bottomRow][j] != 0:
            return False

    return True


if __name__ == '__main__':
    matrix = [
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 1]
    ]

    print(squareOfZeroes(matrix))
