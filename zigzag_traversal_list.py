#!/usr/bin/env python
# coding:utf-8
"""
@FileName : zigzag_traversal_list.py
@Author   : Harsh Parikh
@Date     : 8/3/21 5:25 PM

498. Diagonal Traverse

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

"""


def zigzagTraverse(array):
    # Write your code here.
    isGoDown = True
    numRows = len(array) - 1
    numCols = len(array[0]) - 1
    i = 0
    j = 0
    zigZagArray = []

    while 0 <= i <= numRows and 0 <= j <= numCols:
        zigZagArray.append(array[i][j])
        if isGoDown:
            if j == 0 or i == numRows:
                isGoDown = False
                if i == numRows:
                    j += 1
                else:
                    i += 1
            else:
                i += 1
                j -= 1
        else:
            if j == numCols or i == 0:
                isGoDown = True
                if j == numCols:
                    i += 1
                else:
                    j += 1
            else:
                i -= 1
                j += 1

    return zigZagArray


if __name__ == '__main__':
    print(zigzagTraverse([
        [1, 3, 4, 10],
        [2, 5, 9, 11],
        [6, 8, 12, 15],
        [7, 13, 14, 16]
    ]))
