#!/usr/bin/env python
# coding:utf-8
"""
@FileName : one_edit_distance.py
@Author   : Harsh Parikh
@Date     : 7/7/21 6:57 PM

161. One Edit Distance

Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.


Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "a", t = ""
Output: true
Example 4:

Input: s = "", t = "A"
Output: true
"""


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False

        if len(s) == len(t):
            return sum(a != b for a, b in zip(s, t)) == 1

        if len(s) > len(t):
            smaller_string, larger_string = t, s
        else:
            smaller_string, larger_string = s, t

        i = 0

        while i < len(smaller_string) and smaller_string[i] == larger_string[i]:
            i += 1

        return smaller_string[i:] == larger_string[i + 1:]


if __name__ == '__main__':
    print(Solution().isOneEditDistance("ta", "t"))
    print(Solution().isOneEditDistance("a", "A"))
    print(Solution().isOneEditDistance("", ""))
