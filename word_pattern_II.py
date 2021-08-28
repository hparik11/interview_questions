#!/usr/bin/env python
# coding:utf-8
"""
@FileName : word_pattern_II.py
@Author   : Harsh Parikh
@Date     : 8/24/21 10:05 PM

291. Word Pattern II

Given a pattern and a string s, return true if s matches the pattern.

A string s matches a pattern if there is some bijective mapping of single characters to strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.



Example 1:

Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"
Example 2:

Input: pattern = "aaaa", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "asd"
Example 3:

Input: pattern = "abab", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "a"
'b' -> "sdasd"
Note that 'a' and 'b' cannot both map to "asd" since the mapping is a bijection.
Example 4:

Input: pattern = "aabb", s = "xyzabcxzyabc"
Output: false
"""

from collections import defaultdict


class Solution:
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.helper(pattern, str, 0, 0, defaultdict(set))

    def helper(self, pattern, str, i, j, pattern2wordTable):
        if i == len(pattern) and j == len(str):
            return True
        elif i == len(pattern) or j == len(str):
            return False
        elif i < len(pattern) and j < len(str):
            p = pattern[i]
            if p in pattern2wordTable:
                w = pattern2wordTable[p]

                if w == str[j: j + len(w)]:
                    if self.helper(pattern, str, i + 1, j + len(w), pattern2wordTable):
                        return True
            else:
                for k in range(j, len(str)):
                    w = str[j: k + 1]

                    if w not in pattern2wordTable.values():

                        pattern2wordTable[p] = w

                        if self.helper(pattern, str, i + 1, k + 1, pattern2wordTable):
                            return True

                        pattern2wordTable.pop(p)

        return False


class Solution2:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        p2s, s2p = dict(), dict()

        return self.dfs(pattern, s, p2s, s2p)

    def dfs(self, p, s, p2s, s2p):
        if not p and not s:
            return True
        if not p and s:
            return False
        if p and not s:
            return False

        for i in range(len(s)):
            cur_p = p[0]
            cur_s = s[:i + 1]
            if (cur_p in p2s and cur_s not in s2p) or (cur_p not in p2s and cur_s in s2p):
                continue
            elif cur_p in p2s and cur_s in s2p:
                if p2s[cur_p] != cur_s:
                    continue
                if self.dfs(p[1:], s[i + 1:], p2s, s2p):
                    return True
            else:
                p2s[cur_p] = cur_s
                s2p[cur_s] = cur_p
                if self.dfs(p[1:], s[i + 1:], p2s, s2p):
                    return True
                del p2s[cur_p]
                del s2p[cur_s]


if __name__ == '__main__':
    s = Solution()
    print(s.wordPatternMatch("abab", "redblueredblue"))
