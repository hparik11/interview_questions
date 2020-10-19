# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: decode_ways.py
# @Date:   9/12/20, Sat
"""
Decode Ways
Medium

3006

3055

Add to List

Share
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""


class Solution:
    def helper(self, string, dictn):

        if len(string) == 0:
            return 1
        if string in dictn:
            return dictn[string]
        if string[0] == '0':
            dictn[string] = 0
            return dictn[string]
        if len(string) == 1:
            dictn[string] = 1
            return dictn[string]

        res = 0
        res += self.helper(string[1:], dictn)

        if len(string) >= 2:
            if int(string[0: 2]) <= 26:
                res += self.helper(string[2:], dictn)

        dictn[string] = res
        return dictn[string]

    def numDecodings(self, s: str) -> int:
        dictn = {}

        return self.helper(s, dictn)


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("1226") == 5)
    print(s.numDecodings("1234") == 3)
    print(s.numDecodings("011") == 0)
    print(s.numDecodings("226") == 3)
    print(s.numDecodings("110") == 1)
