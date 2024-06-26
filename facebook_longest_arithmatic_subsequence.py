#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_longest_arithmatic_subsequence.py
@Author   : Harsh Parikh
@Date     : 9/16/21 12:26 AM

1027. Longest Arithmetic Subsequence

Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Recall that a subsequence of an array nums is a list nums[i1], nums[i2], ..., nums[ik] with 0 <= i1 < i2 < ... < ik <= nums.length - 1, and that a sequence seq is arithmetic if seq[i+1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).



Example 1:

Input: nums = [3,6,9,12]
Output: 4
Explanation:
The whole array is an arithmetic sequence with steps of length = 3.
Example 2:

Input: nums = [9,4,7,2,10]
Output: 3
Explanation:
The longest arithmetic subsequence is [4,7,10].
Example 3:

Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation:
The longest arithmetic subsequence is [20,15,10,5].
"""


class Solution:
    def longestArithSeqLength(self, nums) -> int:
        dp = {}
        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i, diff] = dp.get((j, diff), 1) + 1

        print(dp)

        return max(dp.values())


if __name__ == '__main__':
    s = Solution()
    print(s.longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]))
