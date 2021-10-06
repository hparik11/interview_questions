#!/usr/bin/env python
# coding:utf-8
"""
@FileName : largest_plus_sign.py
@Author   : Harsh Parikh
@Date     : 8/27/21 10:00 PM

764. Largest Plus Sign

You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.



Example 1:


Input: n = 5, mines = [[4,2]]
Output: 2
Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.
Example 2:


Input: n = 1, mines = [[0,0]]
Output: 0
Explanation: There is no plus sign, so return 0.

"""


# Brute force | O(n^3)
class Solution1(object):
    def orderOfLargestPlusSign(self, N, mines):
        banned = {tuple(mine) for mine in mines}
        ans = 0
        for r in xrange(N):
            for c in xrange(N):
                k = 0
                while (k <= r < N - k and k <= c < N - k and
                       (r - k, c) not in banned and
                       (r + k, c) not in banned and
                       (r, c - k) not in banned and
                       (r, c + k) not in banned):
                    k += 1
                ans = max(ans, k)
        return ans


class Solution2:
    @staticmethod
    def orderOfLargestPlusSign(n: int, mines) -> int:

        rows = n
        cols = n
        mines = set((x, y) for x, y in mines)

        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            count_ones = 0

            for j in range(cols):
                if (i, j) not in mines:
                    count_ones += 1
                else:
                    count_ones = 0

                dp[i][j] = count_ones

            count_ones = 0
            for j in range(cols - 1, -1, -1):
                if (i, j) not in mines:
                    count_ones += 1
                else:
                    count_ones = 0

                dp[i][j] = min(count_ones, dp[i][j])

        final_answer = 0

        for j in range(cols):
            count_ones = 0
            for i in range(rows):
                if (i, j) not in mines:
                    count_ones += 1
                else:
                    count_ones = 0

                dp[i][j] = min(count_ones, dp[i][j])

            count_ones = 0

            for i in range(rows - 1, -1, -1):
                if (i, j) not in mines:
                    count_ones += 1
                else:
                    count_ones = 0

                dp[i][j] = min(count_ones, dp[i][j])

                final_answer = max(final_answer, dp[i][j])

        return final_answer
