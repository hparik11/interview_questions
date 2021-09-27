#!/usr/bin/env python
# coding:utf-8
"""
@FileName : single_number_II.py
@Author   : Harsh Parikh
@Date     : 9/2/21 1:10 PM

137. Single Number II

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
"""


class Solution:
    def singleNumber(self, nums) -> int:

        single = 0

        for i in range(32):
            mask = (1 << i)

            count = 0

            for num in nums:
                if num & mask != 0:
                    count += 1

            # If count is not 3 then add mask to single
            if count % 3 != 0:
                single |= mask

        # For negative numbers Not operator of positive number (~5 = -6, ~4 = -5)
        if single > 2 ** 31 - 1:
            return single - 2 ** 32

        return single


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([2, 2, 3, 2]))
    print(s.singleNumber([-4, 2, 2, 3, 3, 3, 2,]))
