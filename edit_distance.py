#!/usr/bin/env python
# coding:utf-8
"""
@FileName : edit_distance.py
@Author   : Harsh Parikh
@Date     : 8/25/21 1:33 AM
"""


class Solution:
    def minDistance(self, word1, word2):
        """Naive recursive solution"""
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        insert = 1 + self.minDistance(word1, word2[1:])
        delete = 1 + self.minDistance(word1[1:], word2)
        replace = 1 + self.minDistance(word1[1:], word2[1:])
        return min(insert, replace, delete)


class Solution1:
    def minDistance(self, word1, word2):
        """Dynamic programming solution"""
        m = len(word1)
        n = len(word2)
        memo = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            memo[i][0] = i
        for j in range(n + 1):
            memo[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1]
                else:
                    memo[i][j] = 1 + min(memo[i - 1][j], memo[i][j - 1], memo[i - 1][j - 1])
        return memo[-1][-1]