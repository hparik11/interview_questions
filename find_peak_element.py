#!/usr/bin/env python
# coding:utf-8
"""
@FileName : find_peak_element.py
@Author   : Harsh Parikh
@Date     : 8/1/21 9:05 AM

162. Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.



Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""


class Solution:
    def findPeakElement(self, nums) -> int:

        if not nums:
            return 0

        if len(nums) <= 2:
            return nums.index(max(nums))

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return low


if __name__ == '__main__':
    s = Solution()
    print(s.findPeakElement([1, 2, 3, 1]))
    print(s.findPeakElement([5, 4, 3, 4, 5]))
