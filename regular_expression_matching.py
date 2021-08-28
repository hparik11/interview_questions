#!/usr/bin/env python
# coding:utf-8
"""
@FileName : regular_expression_matching.py
@Author   : Harsh Parikh
@Date     : 7/21/21 3:23 PM

10. Regular Expression Matching

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input: s = "mississippi", p = "mis*is*p*."
Output: false
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        n = len(s)
        m = len(p)

        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]

        # empty string matches empty string
        dp[0][0] = True

        # This deals with patterns like a* or a*b* or a*b*c*
        for c in range(1, m + 1):
            if c >= 2 and p[c - 1] == '*':
                dp[0][c] = dp[0][c - 2]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # if current pattern is a dot
                # or if current pattern has same character
                # as current text then the answer is the one
                # diagonally above(removing both chars)
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]

                # if its a star then it gets interesting.
                # first its automatically equal to [i][j-2]
                # since that's accounting for the STAR being of 0 length
                # aka a* being ''(empty). Then if that doesnt work
                # if the pattern is a dot(accounting for .*) or
                # previous pattern before * is similar as text
                # then its the answer above since your accounting for
                # removing last char of text
                elif j >= 2 and p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = (dp[i][j] or dp[i - 1][j])

        return dp[n][m]


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("aab", "c*a*b"))
