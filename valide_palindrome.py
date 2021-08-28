#!/usr/bin/env python
# coding:utf-8
"""
@FileName : valid_palindrome.py
@Author   : Harsh Parikh
@Date     : 6/14/21 12:18 AM
"""

"""
680. Valid Palindrome II
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(word):
            if len(word) < 2:
                return True

            i = 0
            j = len(word) - 1

            while i < j:
                if word[i] != word[j]:
                    return False
                i += 1
                j -= 1

            return True

        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i] != s[j]:
                if is_palindrome(s[i + 1: j + 1]) | is_palindrome(s[i:j]):
                    return True
                else:
                    return False
            else:
                i += 1
                j -= 1

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.validPalindrome("aba") is True)
    print(s.validPalindrome("abca") is True)
    print(s.validPalindrome("abc") is False)
