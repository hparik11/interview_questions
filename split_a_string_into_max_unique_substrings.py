#!/usr/bin/env python
# coding:utf-8
"""
@FileName : split_a_string_into_max_unique_substrings.py
@Author   : Harsh Parikh
@Date     : 8/27/21 10:15 PM

1593. Split a String Into the Max Number of Unique Substrings
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc'].
Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
"""


class Solution:
    # Time complexity: O(2^N)
    # Space complexity: O(N), cause max stack size is N, max set size is N

    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        ans = self.helper(s, seen)
        return ans

    def helper(self, s, seen):
        if not s:
            return 0

        ans = 0

        for i in range(1, len(s) + 1):
            candidate = s[:i]

            if candidate not in seen:
                seen.add(candidate)

                ans = max(ans, 1 + self.helper(s[i:], seen))

                seen.remove(candidate)

        return ans
