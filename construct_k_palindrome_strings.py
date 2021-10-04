#!/usr/bin/env python
# coding:utf-8
"""
@FileName : construct_k_palindrome_strings.py
@Author   : Harsh Parikh
@Date     : 8/19/21 1:42 AM

1400. Construct K Palindrome Strings

Given a string s and an integer k. You should construct k non-empty palindrome strings using all the characters in s.

Return True if you can use all the characters in s to construct k palindrome strings or False otherwise.



Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.
Example 3:

Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.
Example 4:

Input: s = "yzyzyzyzyzyzyzy", k = 2
Output: true
Explanation: Simply you can put all z's in one string and all y's in the other string. Both strings will be palindrome.
Example 5:

Input: s = "cr", k = 7
Output: false
Explanation: We don't have enough characters in s to construct 7 palindromes.
"""

from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        """

        The solution is based on the understanding that a string can be a palindrome only
        if it has at most 1 character whose frequency is odd. So if the number of characters
        having an odd frequency is greater than the number of palindromes we need to form,
        then naturally it's impossible to do so.

        """
        if k > len(s):
            return False

        h = Counter(s)

        countOdds = 0

        for value in h.values():
            if value % 2 == 1:
                countOdds += 1

        if countOdds > k:
            return False

        return True
