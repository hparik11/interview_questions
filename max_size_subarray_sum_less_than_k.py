#!/usr/bin/env python
# coding:utf-8
"""
@FileName : max_size_subarray_sum_less_than_k.py
@Author   : Harsh Parikh
@Date     : 7/28/21 1:27 AM

325. Maximum Size Subarray Sum Equals k

Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.



Example 1:

Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
"""


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        """
        input nums = [-2, 7, 1,-1, 5,-2, 3]
        prefix_sums = [0,-2, 5, 6, 5,10, 8,11]
        At curr_index 7 in the prefix_sums list,
        the sum from the beginning to curr_index is 8,
        and if you subtract 8 with the target of 3 then you get 5.
        From that we are looking for an index to the left of curr_index that equates to that 5.
        To the left of curr_index because whatever index we find represents at that specific point in time, that was the sum.
        If you do find that index to the left of curr_index that is equal to 5,
        then you have found two indexes that have changed a difference of 3 (target) and therefore have sumed to 3.
        then the difference between the indexes represents the length of that subarray.

        """

        seen_sum = {0: 0}
        total_sum, largest_len = 0, 0

        for i in range(len(nums)):
            total_sum += nums[i]
            if total_sum == k:
                largest_len = i + 1
            else:
                required = total_sum - k
                if required in seen_sum:
                    largest_len = max(largest_len, i - seen_sum[required])

            if total_sum not in seen_sum:
                seen_sum[total_sum] = i

        return largest_len
