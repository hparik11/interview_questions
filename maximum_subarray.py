# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: maximum_subarray.py
# @Date:   9/13/20, Sun

"""
Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-2147483647]
Output: -2147483647
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxSum = nums[0]
        currSum = nums[0]
        for i in range(1, len(nums)):
            currSum = max(nums[i], nums[i] + currSum)
            if maxSum < currSum:
                maxSum = currSum

        return maxSum


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(s.maxSubArray([-1]))
    print(s.maxSubArray([1]))
    print(s.maxSubArray([-2,-1]))
    print(s.maxSubArray([-1,-2]))
