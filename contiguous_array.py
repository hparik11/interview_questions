#!/usr/bin/env python
# coding:utf-8
"""
@FileName : contiguous_array.py
@Author   : Harsh Parikh
@Date     : 9/6/21 9:31 PM

525. Contiguous Array
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.



Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""


class Solution:
    """
    https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation
    """

    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length = 0

        table = {0: -1}

        for index, num in enumerate(nums):

            if num == 0:
                count -= 1
            else:
                count += 1

            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index

        return max_length
