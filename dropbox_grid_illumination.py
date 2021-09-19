#!/usr/bin/env python
# coding:utf-8
"""
@FileName : dropbox_grid_illumination.py
@Author   : Harsh Parikh
@Date     : 7/17/21 11:53 PM

1001. Grid Illumination

There is a 2D grid of size n x n where each cell of this grid has a lamp that is initially turned off.

You are given a 2D array of lamp positions lamps, where lamps[i] = [rowi, coli] indicates that the lamp at grid[rowi][coli] is turned on. Even if the same lamp is listed more than once, it is turned on.

When a lamp is turned on, it illuminates its cell and all other cells in the same row, column, or diagonal.

You are also given another 2D array queries, where queries[j] = [rowj, colj]. For the jth query, determine whether grid[rowj][colj] is illuminated or not. After answering the jth query, turn off the lamp at grid[rowj][colj] and its 8 adjacent lamps if they exist. A lamp is adjacent if its cell shares either a side or corner with grid[rowj][colj].

Return an array of integers ans, where ans[j] should be 1 if the cell in the jth query was illuminated, or 0 if the lamp was not.



Example 1:


Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
Output: [1,0]
Explanation: We have the initial grid with all lamps turned off. In the above picture we see the grid after turning on the lamp at grid[0][0] then turning on the lamp at grid[4][4].
The 0th query asks if the lamp at grid[1][1] is illuminated or not (the blue square). It is illuminated, so set ans[0] = 1. Then, we turn off all lamps in the red square.

The 1st query asks if the lamp at grid[1][0] is illuminated or not (the blue square). It is not illuminated, so set ans[1] = 0. Then, we turn off all lamps in the red rectangle.

Example 2:

Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
Output: [1,1]
Example 3:

Input: n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
Output: [1,1,0]
"""

from collections import defaultdict
from typing import List


class Solution:

    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        lamps = {(light[0], light[1]) for light in lamps}
        row, col, diag, andi = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
        for x, y in lamps:
            row[x] += 1;
            col[y] += 1;
            diag[x - y] += 1;
            andi[x + y] += 1

        res = []
        adjacentLamps = [(0, 0), (0, -1), (0, 1),
                         (-1, 0), (-1, -1), (-1, 1),
                         (1, 0), (1, -1), (1, 1)]

        for x, y in queries:
            if row[x] > 0 \
                    or col[y] > 0 \
                    or diag[x - y] > 0 \
                    or andi[x + y] > 0:

                res.append(1)

            else:
                res.append(0)

            for r1, c1 in adjacentLamps:
                new_r = x + r1
                new_c = y + c1

                if (new_r, new_c) in lamps:
                    lamps.remove((new_r, new_c))
                    row[new_r] -= 1;
                    col[new_c] -= 1;
                    diag[new_r - new_c] -= 1;
                    andi[new_r + new_c] -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.gridIllumination(6,
                             [[2, 5], [4, 2], [0, 3], [0, 5], [1, 4], [4, 2], [3, 3], [1, 0]],
                             [[4, 3], [3, 1], [5, 3], [0, 5], [4, 4], [3, 3]]))
