#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_height_of_highest_accessible_cell.py
@Author   : Harsh Parikh
@Date     : 9/13/21 2:50 PM

[
  [900 500 300]
 [700 500 300]
 [0 100 200]
]

Output: 300 (0 -> 100 -> 200 -> 300)

Top-down view of hiking area
Each number => height of that cell
Goal: find the height of the highest accessible cell
A cell is accessible if:
Height = 0; or
Adjacent to another accessible cell, height difference <= 100
'''

Note: There can be many zeros .


"""

from collections import deque


def heighestAccessibleCell(area):
    if not area or len(area) == 0:
        return 0

    queue = deque()
    rows = len(area)
    cols = len(area[0])
    visited = [[False] * rows] * cols
    for i in range(rows):
        for j in range(cols):
            if area[i][j] == 0:
                queue.append([i, j])

    maxCell = 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        cell = queue.popleft()
        i = cell[0]
        j = cell[1]
        maxCell = max(maxCell, area[i][j])
        for x, y in directions:
            newX = x + i
            newY = y + j

            if (0 <= newX < rows and 0 <= newY < cols \
                    and area[newX][newY] - area[i][j] <= 100 and not
                    visited[newX][newY]):
                visited[newX][newY] = True
                queue.append([newX, newY])

    return maxCell


area = [[0, 500, 400], [100, 200, 300], [0, 100, 500]]
print(heighestAccessibleCell(area))
