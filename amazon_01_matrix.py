#!/usr/bin/env python
# coding:utf-8
"""
@FileName : amazon_01_matrix.py
@Author   : Harsh Parikh
@Date     : 9/4/21 12:40 AM

542. 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.


Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        m, n = len(mat), len(mat[0])

        # top to bottom
        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else float('inf')
                    left = mat[r][c - 1] if c > 0 else float('inf')
                    mat[r][c] = min(top, left) + 1

        # Bottom to top
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else float('inf')
                    right = mat[r][c + 1] if c < n - 1 else float('inf')

                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

        return mat

