#!/usr/bin/env python
# coding:utf-8
"""
@FileName : distinct_sequences.py
@Author   : Harsh Parikh
@Date     : 9/15/21 2:22 PM

115. Distinct Subsequences

Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.



Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag
"""


class Solution:
    # O(m*n) space
    def numDistinct(self, s: str, t: str) -> int:

        memo = {}
        M, N = len(s), len(t)

        def uniqueSubsequences(i, j):
            # Base case
            if i == M or j == N:
                # if j ppinter reaches to end then 1 otherwise 0
                return int(j == N)

            # Check if the result is already cached
            if (i, j) in memo:
                return memo[i, j]

            # If the characters match, make the other
            # one and add the result to "ans"
            if s[i] == t[j]:
                ans = uniqueSubsequences(i + 1, j) + uniqueSubsequences(i + 1, j + 1)
            else:
                ans = uniqueSubsequences(i + 1, j)

            # Cache the answer and return
            memo[i, j] = ans
            return ans

        return uniqueSubsequences(0, 0)

    def numDistinct4(self, s: str, t: str) -> int:

        M, N = len(s), len(t)

        # Dynamic Programming table
        dp = [[0 for i in range(N + 1)] for j in range(M + 1)]

        # Base case initialization
        for j in range(N + 1):
            dp[M][j] = 0

        # Base case initialization
        for i in range(M + 1):
            dp[i][N] = 1

        # Iterate over the strings in reverse so as to
        # satisfy the way we've modeled our recursive solution
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):

                # Remember, we always need this result
                dp[i][j] = dp[i + 1][j]

                # If the characters match, we add the
                # result of the next recursion call (in this
                # case, the value of a cell in the dp table
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]

    # O(m*n) space
    def numDistinct1(self, s, t):
        l1, l2 = len(s) + 1, len(t) + 1
        dp = [[1] * l2 for _ in range(l1)]
        for j in range(1, l2):
            dp[0][j] = 0
        for i in range(1, l1):
            for j in range(1, l2):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]

    # O(n) space
    def numDistinct2(self, s, t):
        l1, l2 = len(s) + 1, len(t) + 1
        cur = [0] * l2
        cur[0] = 1
        for i in range(1, l1):
            pre = cur[:]
            for j in range(1, l2):
                if s[i - 1] == t[j - 1]:
                    cur[j] = pre[j] + pre[j - 1]
                else:
                    cur[j] = pre[j]

        return cur[-1]