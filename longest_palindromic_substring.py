# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: longest_palindromic_substring.py
# @Date:   8/26/20, Wed

"""
5. Longest Palindromic Substring
Medium

7644

563

Add to List

Share
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


def findPalindrome(string, index, isOdd=True):
    if isOdd:
        leftIndex = index - 1
        rightIndex = index + 1
    else:
        leftIndex = index
        rightIndex = index + 1

    isPalindrome = False
    while leftIndex >= 0 and rightIndex < len(string):
        if string[leftIndex] != string[rightIndex]:
            break
        isPalindrome = True
        leftIndex -= 1
        rightIndex += 1

    return string[leftIndex + 1: rightIndex] if isPalindrome else ''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        longestString = s[0]
        for i in range(0, len(s)):
            currString1 = findPalindrome(s, i, True)
            currString2 = findPalindrome(s, i, False)

            longestString = max(currString1, currString2, longestString, key=lambda x: len(x))

        return longestString


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))
