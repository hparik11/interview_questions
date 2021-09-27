#!/usr/bin/env python
# coding:utf-8
"""
@FileName : palindrome_partitioning.py
@Author   : Harsh Parikh
@Date     : 9/5/21 6:57 PM

131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
"""

"""
Time Complexity : O(N *2^N)
, where N is the length of string ss. This is the worst-case time complexity when all the possible substrings are palindrome.

Space Complexity: O(N)
"""


class Solution:
    def partition(self, s: str):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return

        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)

    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.partition("aab"))
