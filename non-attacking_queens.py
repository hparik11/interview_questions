#!/usr/bin/env python
# coding:utf-8
"""
@FileName : non-attacking_queens.py
@Author   : Harsh Parikh
@Date     : 8/9/21 3:31 AM
"""


def nonAttackingQueens(n):
    # Write your code here.

    """
         0  1  2  3
      0  Q
      1           Q
      2     Q
      3

    """

    # Each index in columnPlacements represents a row of board
    # and value it points to is the column of that relevant row
    # where a queen is placed.
    columnPlacements = [0] * n

    return getNumberOfValidPlacements(0, columnPlacements, n)


def getNumberOfValidPlacements(row, columnPlacements, boardSize):
    if row == boardSize:
        return 1

    validPlacements = 0

    for col in range(boardSize):
        if is_valid_placement(row, col, columnPlacements):
            columnPlacements[row] = col
            validPlacements += getNumberOfValidPlacements(row + 1, columnPlacements, boardSize)

    return validPlacements


def is_valid_placement(row, column, columnPlacements):
    for each in range(row):
        if columnPlacements[each] == column:
            return False

        diagonal = (row - column) == (each - columnPlacements[each])
        anti_diagonal = (row + column) == (each + columnPlacements[each])

        if diagonal or anti_diagonal:
            return False

    return True
