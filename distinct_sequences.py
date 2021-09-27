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

            # Always make this recursive call
            ans = uniqueSubsequences(i + 1, j)

            # If the characters match, make the other
            # one and add the result to "ans"
            if s[i] == t[j]:
                ans += uniqueSubsequences(i + 1, j + 1)

            # Cache the answer and return
            memo[i, j] = ans
            return ans

        return uniqueSubsequences(0, 0)