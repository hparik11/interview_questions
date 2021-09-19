#!/usr/bin/env python
# coding:utf-8
"""
@FileName : largest_square_subarray_of_1.py
@Author   : Harsh Parikh
@Date     : 8/5/21 3:42 PM

Given a 2D array of 1s and 0s, find the largest square subarray of all 1s.

eg.

subarray([1, 1, 1, 0]
         [1, 1, 1, 1]
         [1, 1, 0, 0]) = 2

"""


def bottom_up_square_submatrix(mat):
    """
    Bottom up solution. Start from the upper left-hand corner and compute
    progressively larger submatrices.

    [1, 1, 1, 0]           [1, 1, 1, 0]
    [1, 1, 1, 1]    ====>  [1, 2, 2, 1]
    [1, 1, 1, 0]           [1, 2, 3, 0]
    [1, 1, 0, 1]           [1, 2, 0, 1]
    """
    max_val = 0
    # Initialize cache
    cache = [[False] * len(mat[0])] * len(mat)
    # Iterate over the matrix to compute all values
    for i in range(len(cache)):
        for j in range(len(cache[0])):
            # If we are in the first row or column then the value is just
            # 1 if that cell is true and 0 otherwise. In other rows and
            # columns, need to look up and to the left.
            if i == 0 or j == 0:
                cache[i][j] = 1 if mat[i][j] else 0
            elif mat[i][j]:
                cache[i][j] = 1 + min(cache[i][j - 1], cache[i - 1][j], cache[i - 1][j - 1])
            if cache[i][j] > max_val:
                max_val = cache[i][j]

    return max_val


if __name__ == '__main__':
    print(bottom_up_square_submatrix([[1, 1, 1, 0],
                                     [1, 1, 1, 1],
                                     [1, 1, 1, 0],
                                      [1, 1, 0, 1]]))
