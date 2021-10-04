#!/usr/bin/env python
# coding:utf-8
"""
@FileName : constrained_sequence_sum.py
@Author   : Harsh Parikh
@Date     : 10/1/21 10:04 PM

1425. Constrained Subsequence Sum
Hard

641

27

Add to List

Share
Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.



Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].
Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.
Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].
"""

import collections
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        queue = collections.deque()

        for i, num in enumerate(nums):

            while queue and queue[0] < i - k:
                queue.popleft()

            if queue:  # compute the max sum we can get at index i
                nums[i] = nums[queue[0]] + num

            while queue and nums[queue[-1]] < nums[i]:
                # delete all the sequence that smaller than current sum, becaus there will never be
                # considers ==> smaller than current sequence, and end before current sequence
                queue.pop()

            if nums[i] > 0:  # if nums[i] < 0, it can't be a useful prefix sum
                queue.append(i)

        return max(nums)
