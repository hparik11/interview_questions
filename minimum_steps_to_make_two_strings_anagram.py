#!/usr/bin/env python
# coding:utf-8
"""
@FileName : minimum_steps_to_make_two_strings_anagram.py
@Author   : Harsh Parikh
@Date     : 8/25/21 12:39 PM

1347. Minimum Number of Steps to Make Two Strings Anagram

Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.



Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams.
Example 4:

Input: s = "xxyyzz", t = "xxyyzz"
Output: 0
Example 5:

Input: s = "friend", t = "family"
Output: 4
"""

from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:

        firstString = Counter(s)
        replacements = 0

        for ch in t:
            if ch in firstString and firstString[ch] > 0:
                firstString[ch] -= 1
            else:
                replacements += 1

        return replacements

