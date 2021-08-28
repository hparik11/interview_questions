#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_subarray_product_less_than_k.py
@Author   : Harsh Parikh
@Date     : 7/27/21 10:26 PM

713. Subarray Product Less Than K
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
"""

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Input: nums = [10, 5, 2, 6], k = 100

        ======== (End for loop, r = 0 snapshot) =============
        [10, 5, 2, 6]
          r
          l
        prod = 10
        cnt += 1


        ======== (End for loop, r = 1 snapshot) =============
        [10, 5, 2, 6]
             r
          l
        prod = 50
        cnt += 2


        ======== (r = 2, prod >= k snapshot) ================
        [10, 5, 2, 6]
                r
          l
        prod = 100, >= k,
        keep moving l till < k


        ======== (End for loop, r = 2 snapshot) =============
        [10, 5, 2, 6]
                r
             l
        prod = 10
        cnt += 2


        ======== (End for loop, r = 3 snapshot) =============
        [10, 5, 2, 6]
                   r
             l
        prod = 60
        cnt += 3

        """

        if k == 0:
            return 0

        left = 0
        currProd = 1
        right = 0
        numberOfSubarray = 0

        while right < len(nums):
            currProd *= nums[right]

            while currProd >= k and left <= right:
                currProd /= nums[left]
                left += 1

            numberOfSubarray += (right - left + 1)

            right += 1

        return numberOfSubarray


if __name__ == '__main__':
    s = Solution()
    print(s.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
