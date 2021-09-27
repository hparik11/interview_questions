#!/usr/bin/env python
# coding:utf-8
"""
@FileName : missing_numbers_II.py
@Author   : Harsh Parikh
@Date     : 9/2/21 12:22 AM

448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.



Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Cyclic sort

        def swap(nums, currIdx, correctIdx):
            nums[currIdx], nums[correctIdx] = nums[correctIdx], nums[currIdx]

        currIdx = 0

        while currIdx < len(nums):
            correctIdx = nums[currIdx] - 1

            if nums[correctIdx] != nums[currIdx]:
                swap(nums, currIdx, correctIdx)
            else:
                currIdx += 1

        missing_numbers = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                missing_numbers.append(i + 1)

        return missing_numbers
