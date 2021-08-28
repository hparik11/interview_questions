#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_continuous_subarray_sum.py
@Author   : Harsh Parikh
@Date     : 8/1/21 11:59 PM

523. Continuous Subarray Sum

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.



Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
"""


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        """
        [23, 2, 4, 6, 7]
        Lets walk through the code with the example.
        (i=0) : sums = 23 => 23%6 => (sums = 5)
        (i=1) : sums = 5+2=7 => 7%6 => (sums = 1)
        (i=2) : sums = 1+4=5 => 5%6 => (sums = 5)
        We have encountered the same sums(remainder) again which means we have the subarray of sums%k = 0.
        But, there's another aspect to this problem. The subarray must have a minimum size of 2.
        That is why we check if (i - d[sums])>1.
        In the above example, this if loop is executed when (i=2) and (d[sums]=1).
        In other words, the same remainder(sums=5) has been encountered twice and then we check for the respective difference in indices.

        """

        prefixSum = 0
        prefixModDictn = {0: -1}  # Subarray should be greater than 2

        for i, num in enumerate(nums):
            prefixSum += num

            if k != 0:
                prefixSum = prefixSum % k

            if prefixSum in prefixModDictn:
                if (i - prefixModDictn[prefixSum]) > 1:
                    return True
            else:
                prefixModDictn[prefixSum] = i

        return False