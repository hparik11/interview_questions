# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: max_product_subarray.py
# @Date:   9/18/20, Fri

"""
152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        You have three choices to make at any position in array.

        - You can get maximum product by multiplying the current element with
          maximum product calculated so far. (might work when current
          element is positive).
        - You can get maximum product by multiplying the current element with
          minimum product calculated so far. (might work when current
          element is negative).
        - Current element might be a starting position for maximum product sub
          array

        """
        prevMaxProd = nums[0]
        prevMinProd = nums[0]

        ans = nums[0]
        for i in range(1, len(nums)):
            maxProd = max(prevMaxProd * nums[i], prevMinProd * nums[i], nums[i])
            minProd = min(prevMaxProd * nums[i], prevMinProd * nums[i], nums[i])
            prevMaxProd = maxProd
            prevMinProd = minProd

            ans = max(ans, maxProd)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([2, 3, -2, 4]))
    print(s.maxProduct([-2, 0, -1]))
    print(s.maxProduct([-4, -3, -2]))
