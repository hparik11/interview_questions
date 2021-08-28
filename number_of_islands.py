"""
200. Number of Islands

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

from typing import List


class Solution:
    def is_valid(self, row, col, m, n):
        if row < 0 or col < 0 or row >= m or col >= n:
            return False
        return True

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        print(m, n)
        num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col, m, n)
                    num_islands += 1

        print(grid)
        return num_islands

    def dfs(self, grid, row, col, m, n):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        grid[row][col] = '2'
        for each in directions:
            r, c = row + each[0], col + each[1]
            if self.is_valid(r, c, m, n) and grid[r][c] == "1":
                self.dfs(grid, r, c, m, n)


if __name__ == '__main__':
    print(Solution().numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
