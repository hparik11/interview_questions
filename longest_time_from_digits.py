# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: longest_time_from_digits.py
# @Date:   9/3/20, Thu
"""
Largest Time for Given Digits
Easy

365

738

Add to List

Share
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.



Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""
"""

from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        perms = permutations(A)
        # print(list(perms))
        hour, minute = -1, -1
        for p in perms:
            currH, currM = p[0] * 10 + p[1], p[2] * 10 + p[3]

            if currH >= 24 or currM >= 60:
                continue

            totalMins = currH * 60 + currM
            if totalMins > hour * 60 + minute:
                hour, minute = currH, currM

        if hour == -1:
            return ""
        return ":".join([f'{hour:02}', f'{minute:02}'])
