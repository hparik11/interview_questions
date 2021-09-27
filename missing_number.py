#!/usr/bin/env python
# coding:utf-8
"""
@FileName : missing_number.py
@Author   : Harsh Parikh
@Date     : 9/2/21 12:05 AM

268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?



Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
Example 4:

Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Cyclic sort

        def swap(nums, i, correctIndex):
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i]

        currIdx = 0

        while currIdx < len(nums):
            correctIndex = nums[currIdx]

            if nums[currIdx] < len(nums) and nums[currIdx] != nums[correctIndex]:
                swap(nums, currIdx, correctIndex)
            else:
                currIdx += 1

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)

    """
    missing

        =4∧(0∧0)∧(1∧1)∧(2∧3)∧(3∧4)
        =(4∧4)∧(0∧0)∧(1∧1)∧(3∧3)∧2
        =0∧0∧0∧0∧2
        =2

    """
    def missingNumber_XOR(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
