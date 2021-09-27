#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_max_consecutive_III.py
@Author   : Harsh Parikh
@Date     : 9/16/21 12:56 AM

1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        start = 0
        maxSeq = 0

        for i in range(len(nums)):

            if nums[i] == 0 and k:
                k -= 1

            elif nums[i] == 0:
                while nums[start] != 0:
                    start += 1
                start += 1

            maxSeq = max(maxSeq, i - start + 1)

        return maxSeq
