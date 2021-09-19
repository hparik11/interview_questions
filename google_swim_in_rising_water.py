#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_swim_in_rising_water.py
@Author   : Harsh Parikh
@Date     : 8/25/21 12:33 AM

778. Swim in Rising Water

You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).



Example 1:


Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:


Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
"""

import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        Let's keep a priority queue of which square we can walk in next. We always walk in the smallest one that is 4-             directionally adjacent to ones we've visited.

        When we reach the target, the largest number we've visited so far is the answer.

        Time Complexity: O(N^2 log N)
        Space Complexity: O(N^2)


        """

        def is_valid(row, col, numRows, numCols):
            return 0 <= row < numRows and 0 <= col < numCols

        numRows = len(grid)
        numCols = len(grid[0])

        visited_cells = set()

        priority_queue = [(grid[0][0], 0, 0)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = grid[0][0]

        while priority_queue:
            elevation, row, col = heapq.heappop(priority_queue)
            ans = max(ans, elevation)

            if (row == numRows - 1) and (col == numCols - 1):
                return ans

            visited_cells.add((row, col))

            for each in directions:
                new_r, new_c = row + each[0], col + each[1]

                if is_valid(new_r, new_c, numRows, numCols) and (new_r, new_c) not in visited_cells:
                    heapq.heappush(priority_queue, (grid[new_r][new_c], new_r, new_c))


