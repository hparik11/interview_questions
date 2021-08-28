#!/usr/bin/env python
# coding:utf-8
"""
@FileName : numbers_of_ways_to_split_a_string.py
@Author   : Harsh Parikh
@Date     : 7/30/21 7:06 PM

1573. Number of Ways to Split a String

Given a binary string s (a string consisting only of '0's and '1's), we can split s into 3 non-empty strings s1, s2, s3 (s1+ s2+ s3 = s).

Return the number of ways s can be split such that the number of characters '1' is the same in s1, s2, and s3.

Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: s = "10101"
Output: 4
Explanation: There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
"1|010|1"
"1|01|01"
"10|10|1"
"10|1|01"
Example 2:

Input: s = "1001"
Output: 0
Example 3:

Input: s = "0000"
Output: 3
Explanation: There are three ways to split s in 3 parts.
"0|0|00"
"0|00|0"
"00|0|0"
Example 4:

Input: s = "100100010100110"
Output: 12

"""


class Solution:
    def numWays(self, s: str) -> int:
        n, ones = len(s), []
        for i, val in enumerate(s):
            if val == '1':
                ones.append(i)
        total = len(ones)
        if total == 0:
            # ref: https://en.wikipedia.org/wiki/Combination
            # combination of selecting 2 places to split the string out of n-1 places
            return ((n - 1) * (n - 2) // 2) % (10 ** 9 + 7)
        if total % 3 != 0:
            return 0
        target = total // 3
        return (ones[target] - ones[target - 1]) * (ones[target * 2] - ones[target * 2 - 1]) % (10 ** 9 + 7)


if __name__ == '__main__':
    s = Solution()
    print(s.numWays("1001"))
