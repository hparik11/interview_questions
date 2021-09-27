#!/usr/bin/env python
# coding:utf-8
"""
@FileName : delete_opertion_for_two_strings.py
@Author   : Harsh Parikh
@Date     : 8/30/21 7:27 PM

583. Delete Operation for Two Strings
Medium

2081

38

Add to List

Share
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.



Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        cache = collections.defaultdict(int)

        return len(word1) + len(word2) - 2 * self.lcs(word1, word2, 0, 0, cache)

    """
    Complexity Analysis

    Time complexity : O(M⋅N).
    
    This time, solving each subproblem has a cost of O(1)O(1). Again, there are M⋅N subproblems, 
    and so we get a total time complexity of O(M⋅N).
    
    Space complexity : O(M⋅N).
    
    """

    def lcs(self, word1, word2, idx1, idx2, cache):

        if idx1 == len(word1) or idx2 == len(word2):
            return 0

        if (idx1, idx2) in cache:
            return cache[(idx1, idx2)]

        if word1[idx1] == word2[idx2]:
            cache[(idx1, idx2)] = 1 + self.lcs(word1, word2, idx1 + 1, idx2 + 1, cache)
        else:
            cache[(idx1, idx2)] = max(self.lcs(word1, word2, idx1 + 1, idx2, cache),
                                      self.lcs(word1, word2, idx1, idx2 + 1, cache))

        return cache[(idx1, idx2)]
