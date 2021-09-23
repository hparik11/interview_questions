# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: min_size_subarray_sum.py
# @Date:   10/4/20, Sun
"""
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

"""
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        currSum = 0
        i = 0
        j = 0
        minLength = float('inf')

        while j < len(nums):
            if currSum >= s:
                minLength = min(minLength, j - i)
                currSum -= nums[i]
                i += 1
            else:
                currSum += nums[j]
                j += 1

        if i == 0 and currSum < s:
            return 0

        while i < j:
            if currSum >= s:
                minLength = min(minLength, j - i)
                currSum -= nums[i]
            i += 1

        return minLength


if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 1, 3]))
    print(s.minSubArrayLen(20, [2, 3]))
    print(s.minSubArrayLen(213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]))
