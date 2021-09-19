# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: amazon_rotten_oranges.py
# @Date:   8/11/20, Tue

"""
994. Rotting Oranges
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
"""

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_cnt = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_cnt += 1

        return self.bfs(queue, grid, row, col, fresh_cnt)

    def is_valid(self, row, col, m, n):
        if row < 0 or col < 0 or row >= m or col >= n:
            return False
        return True

    def bfs(self, queue, grid, row, col, fresh_cnt) -> int:

        total_min = -1
        while len(queue) > 0:
            total_min += 1
            total_children = len(queue)

            for _ in range(total_children):
                element = queue.popleft()
                for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    newRow = element[0] + direction[0]
                    newCol = element[1] + direction[1]

                    if self.is_valid(newRow, newCol, row, col):
                        if grid[newRow][newCol] == 1:
                            fresh_cnt -= 1
                            queue.append((newRow, newCol))
                            grid[newRow][newCol] = 2

        if fresh_cnt != 0:
            return -1
        elif total_min == -1:
            return 0
        return total_min


if __name__ == '__main__':
    s = Solution()
    print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    print(s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
    print(s.orangesRotting([[0]]))
    print(s.orangesRotting([[1]]))
