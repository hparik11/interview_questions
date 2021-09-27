# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: climbing_stairs.py
# @Date:   9/18/20, Fri
"""
Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

"""
Complexity Analysis

Time complexity : O(n). Size of recursion tree can go upto nn.

Space complexity : O(n). The depth of recursion tree can go upto nn.
"""


class Solution:
    def climbStairs(self, n: int, dp=None) -> int:
        if dp is None:
            dp = {}
        if n == 0 or n == 1:
            return 1
        if n in dp:
            return dp[n]
        else:
            dp[n] = self.climbStairs(n - 1, dp) + self.climbStairs(n - 2, dp)

        return dp[n]

    def countWaysUtil(self, n, m):
        # Creates list res with all elements 0
        res = [0 for x in range(n + 1)]
        res[0], res[1] = 1, 1

        for i in range(2, n + 1):
            j = 1
            while j <= m and j <= i:
                res[i] = res[i] + res[i - j]
                j = j + 1
        return res[n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(5))
