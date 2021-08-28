#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_subarray_sum_k.py
@Author   : Harsh Parikh
@Date     : 7/17/21 2:54 PM

560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        """
        / Sliding window -- No, contains negative number
        // hashmap + preSum
        /*
            1. Hashmap<sum[0,i - 1], frequency>
            2. sum[i, j] = sum[0, j] - sum[0, i - 1]    --> sum[0, i - 1] = sum[0, j] - sum[i, j]
                   k           sum      hashmap-key     -->  hashmap-key  =  sum - k
            3. now, we have k and sum.
                  As long as we can find a sum[0, i - 1], we then get a valid subarray
                 which is as long as we have the hashmap-key,  we then get a valid subarray
            4. Why don't map.put(sum[0, i - 1], 1) every time ?
                  if all numbers are positive, this is fine
                  if there exists negative number, there could be preSum frequency > 1
        */
        """

        prefixSumDict = defaultdict(int)

        # We need to either insert 0 in beginning or put into prefixSumDict[0] = 1 to deal with scenario when there's only one element with sum = k
        nums.insert(0, 0)

        currSum = 0
        totalNumberOfContinuousSubarraysWithSumK = 0

        for num in nums:
            currSum += num

            if currSum - k in prefixSumDict:
                totalNumberOfContinuousSubarraysWithSumK += prefixSumDict[currSum - k]

            prefixSumDict[currSum] += 1

        return totalNumberOfContinuousSubarraysWithSumK
