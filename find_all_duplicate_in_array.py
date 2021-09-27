#!/usr/bin/env python
# coding:utf-8
"""
@FileName : find_all_duplicate_in_array.py
@Author   : Harsh Parikh
@Date     : 9/2/21 1:17 AM

442. Find All Duplicates in an Array
Medium

4136

197

Add to List

Share
Given an integer array nums of length n where all the integers of nums are in the range [1, n]
and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.



Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        def swap(nums, currIdx, correctIdx):
            nums[currIdx], nums[correctIdx] = nums[correctIdx], nums[currIdx]

        currIdx = 0

        while currIdx < len(nums):
            correctIdx = nums[currIdx] - 1

            if nums[currIdx] != nums[correctIdx]:
                swap(nums, currIdx, correctIdx)
            else:
                currIdx += 1

        duplicate_numbers = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicate_numbers.append(nums[i])

        return duplicate_numbers
