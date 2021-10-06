#!/usr/bin/env python
# coding:utf-8
"""
@FileName : first_missing_positive.py
@Author   : Harsh Parikh
@Date     : 9/7/21 2:55 AM

41. First Missing Positive

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        def swap(nums, currIdx, correct_idx):
            nums[currIdx], nums[correct_idx] = nums[correct_idx], nums[currIdx]

        # cyclic sort
        # Put all the numbers in their positions from 0..len(nums)-1 ignoring the -ve and greater numbers
        if not nums:
            return 1

        i, n = 0, len(nums)

        while i < n:
            correctIdx = nums[i] - 1
            if 0 < nums[i] < n and nums[i] != nums[correctIdx]:
                swap(nums, i, correctIdx)
            else:
                i += 1

        # Find the first number missing in it's palce while looping thru 0..n-1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If you can't find it, return n+1
        return n + 1
