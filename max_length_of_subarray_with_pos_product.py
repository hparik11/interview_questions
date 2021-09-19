# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: max_length_of_subarray_with_pos_product.py
# @Date:   8/29/20, Sat


"""
Maximum Length of Subarray With Positive Product

Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.



Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.
Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
Example 4:

Input: nums = [-1,2]
Output: 1
Example 5:

Input: nums = [1,2,3,5,-6,4,0,10]
Output: 4

"""

from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        firstNegative = -1
        start = -1
        maxLength = 0
        # total_neg is used to count the number of negative numbers from start to current index
        total_neg = 0
        i = 0
        while i < len(nums):
            if nums[i] < 0:
                total_neg += 1
                # // we only need to know index of first negative number
                if firstNegative == -1:
                    firstNegative = i
            # // if current number is 0, we can't use any element from index 0 to i anymore,
            # so update start, and reset total_neg and firstNegative.

            if nums[i] == 0:
                total_neg = 0
                start = i
                firstNegative = -1
            else:
                # // consider index of zero
                if total_neg % 2 == 0:
                    maxLength = max(maxLength, i - start)
                # // consider index of first negative number
                else:
                    maxLength = max(maxLength, i - firstNegative)
            # print(i, nums[i], firstNegative, start, total_neg, maxLength)
            i += 1
        return maxLength


if __name__ == '__main__':
    s = Solution()
    print(s.getMaxLen([-1, -2, -3, 0, 1]) == 2)
    # print(s.getMaxLen([-1, 2]) == 1)
    # print(s.getMaxLen([1, 2, 3, 5, -6, 4, 0, 10]) == 4)
    # print(s.getMaxLen([0, 1, -2, -3, -4]) == 3)
    # print(s.getMaxLen([5, -20, -20, -39, -5, 0, 0, 0, 36, -32, 0, -7, -10, -7, 21, 20, -12, -34, 26, 2]) == 8)
