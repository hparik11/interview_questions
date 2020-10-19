"""

64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

from typing import List
import math


class Solution:
    #     def minPathSum(self, grid: List[List[int]]) -> int:
    #         m = len(grid)
    #         n = len(grid[0])

    #         if m == 0 or n == 0:
    #             return 0

    #         dp = [[None for _ in range(n)] for _ in range(m)]
    #         dp[0][0] = grid[0][0]

    #         return self.recursiveMinSum(grid, m - 1, n - 1, dp)

    #     def recursiveMinSum(self, grid, row, col, dp):
    #         if dp[row][col] != None:
    #             return dp[row][col]
    #         if row < 0 or col < 0:
    #             return math.inf

    #         dp[row][col] = min(self.recursiveMinSum(grid, row - 1, col, dp),                                                    self.recursiveMinSum(grid, row, col - 1, dp)) + grid[row][col]

    #         return dp[row][col]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if m == 0 or n == 0:
            return 0

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[r][c] = grid[0][0]
                elif c == 0:
                    dp[r][c] = dp[r - 1][c] + grid[r][c]
                elif r == 0:
                    dp[r][c] = dp[r][c - 1] + grid[r][c]
                else:
                    dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]

        return dp[m - 1][n - 1]


if __name__ == "__main__":
    s = Solution()
    # print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print(s.minPathSum([[0, 0], [0, 0]]))
