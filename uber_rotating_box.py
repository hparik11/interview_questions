#!/usr/bin/env python
# coding:utf-8
"""
@FileName : uber_rotating_box.py
@Author   : Harsh Parikh
@Date     : 8/18/21 12:32 PM

1861. Rotating the Box

You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.



Example 1:



Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
Example 2:



Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
Example 3:



Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[str]]) -> List[List[str]]:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        # iterate through matrix
        for i in range(n):
            for j in range(i, n):
                # transpose the matrix, turning rows into columns and vice versa
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            # reverse the resulting rows
            matrix[i].reverse()

        return matrix

    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:

        numRows = len(box)
        numCols = len(box[0])

        for rowIdx in range(numRows):
            currRow = box[rowIdx]

            colIdx = numCols - 1
            empty_spaces = []  # Maintain queue of c

            while colIdx >= 0:
                if currRow[colIdx] == ".":
                    empty_spaces.append(colIdx)
                elif currRow[colIdx] == '*':
                    empty_spaces = []
                else:
                    if len(empty_spaces) > 0:
                        empty_space = empty_spaces.pop(0)
                        box[rowIdx][colIdx] = '.'
                        empty_spaces.append(colIdx)
                        box[rowIdx][empty_space] = '#'

                colIdx = colIdx - 1

        return self.rotate(box)


if __name__ == '__main__':
    s = Solution()
    print(s.rotateTheBox(
        [["#", "#", "*", ".", "*", "."], ["#", "#", "#", "*", ".", "."], ["#", "#", "#", ".", "#", "."]]))
