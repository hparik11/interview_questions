#!/usr/bin/env python
# coding:utf-8
"""
@FileName : longest_common_subsequence.py
@Author   : Harsh Parikh
@Date     : 8/30/21 8:22 PM
"""

"""
Complexity Analysis

Time complexity :O(M⋅N).

This time, solving each subproblem has a cost of O(1)O(1). Again, there are M \cdot NM⋅N subproblems, and so we get a total time complexity of O(M \cdot N)O(M⋅N).

Space complexity : O(M⋅N).

We need to store the answer for each of the M⋅N subproblems.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def lcs(word1, word2, idx1, idx2, cache):

            if idx1 == len(word1) or idx2 == len(word2):
                return 0

            if (idx1, idx2) in cache:
                return cache[(idx1, idx2)]

            if word1[idx1] == word2[idx2]:
                cache[(idx1, idx2)] = 1 + lcs(word1, word2, idx1 + 1, idx2 + 1, cache)
            else:
                cache[(idx1, idx2)] = max(lcs(word1, word2, idx1 + 1, idx2, cache),
                                          lcs(word1, word2, idx1, idx2 + 1, cache))

            return cache[(idx1, idx2)]

        cache = collections.defaultdict(int)

        return lcs(text1, text2, 0, 0, cache)


"""
Complexity Analysis

Let M be the length of the first word, and NN be the length of the second word.

Time complexity : O(M⋅N).

Like before, we're solving M⋅N subproblems, and each is an O(1) operation to solve.

Space complexity : O(min(M,N)).

We've reduced the auxilary space required so that we only use two 1D arrays at a time; each the length of the shortest input word. Seeing as the 22 is a constant, we drop it, leaving us with the minimum length out of the two words.


"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # If text1 doesn't reference the shortest string, swap them.
        if len(text2) < len(text1):
            text1, text2 = text2, text1

        # The previous and current column starts with all 0's and like
        # before is 1 more than the length of the first word.
        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text1) + 1)

        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
            # The current column becomes the previous one, and vice versa.
            previous, current = current, previous

        # The original problem's answer is in previous[0]. Return it.
        return previous[0]
