#!/usr/bin/env python
# coding:utf-8
"""
@FileName : valid_sudoku.py
@Author   : Harsh Parikh
@Date     : 9/29/21 11:33 PM

36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""


class Solution:

    def check_duplicates_in_array(self, value, array):
        return value in array

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])

        row_map = [{} for _ in range(row)]
        col_map = [{} for _ in range(col)]
        box_map = [{} for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if board[i][j] != '.':
                    if board[i][j] in row_map[i] or board[i][j] in col_map[j]:
                        return False

                    row_map[i][board[i][j]] = True

                    col_map[j][board[i][j]] = True

                    box_index = (i // 3) * 3 + j // 3

                    if board[i][j] in box_map[box_index]:
                        return False

                    box_map[box_index][board[i][j]] = True

        return True