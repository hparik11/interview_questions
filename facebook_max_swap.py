#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_max_swap.py
@Author   : Harsh Parikh
@Date     : 9/17/21 12:25 AM

670. Maximum Swap

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.



Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        i = 0
        while i < n - 1:  # find index where s[i] < s[i+1], meaning a chance to flip
            if s[i] < s[i + 1]:
                break
            i += 1

        if i == n-1:
            return num  # if nothing find, return num

        max_idx, max_val = i + 1, s[i + 1]  # keep going right, find the maximum value index

        for j in range(i + 1, n):
            if max_val <= s[j]:
                max_idx, max_val = j, s[j]

        left_idx = i  # going right from i, find most left value that is less than max_val
        for j in range(i, -1, -1):
            if s[j] < max_val:
                left_idx = j

        s[max_idx], s[left_idx] = s[left_idx], s[max_idx]  # swap maximum after i and most left less than max

        return int(''.join(s))  # re-create the integer
