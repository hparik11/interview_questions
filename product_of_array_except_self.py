#!/usr/bin/env python
# coding:utf-8
"""
@FileName : product_of_array_except_self.py
@Author   : Harsh Parikh
@Date     : 7/27/21 11:14 AM

238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        leftProduct = [1 for _ in nums]
        rightProduct = [1 for _ in nums]
        productArray = [0 for _ in nums]

        i = 0
        j = len(nums) - 1

        while i < len(nums):
            if i == 0:
                leftProduct[i] = 1
            else:
                leftProduct[i] = leftProduct[i - 1] * nums[i - 1]

            i += 1

        while j >= 0:
            if j == len(nums) - 1:
                rightProduct[j] = 1
            else:
                rightProduct[j] = (rightProduct[j + 1] * nums[j + 1])

            j -= 1

        for i in range(len(nums)):
            productArray[i] = leftProduct[i] * rightProduct[i]

        return productArray

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [1 for _ in range(n)]

        forward, backward = 1, 1

        for i in range(n):
            result[i] *= forward
            result[n - 1 - i] *= backward
            forward *= nums[i]
            backward *= nums[n - 1 - i]

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1, 2, 0, 4]))
