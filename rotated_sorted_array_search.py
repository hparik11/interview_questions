#!/usr/bin/env python
# coding:utf-8
"""
@FileName : rotated_sorted_array_search.py
@Author   : Harsh Parikh
@Date     : 6/14/21 7:18 PM
"""

"""
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        # determine it's left rotated or right rotated
        """
        No rotated:
        1 2 3 4 5 6 7
             mid

        left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
        3 4 5 6 7 1 2
             mid
        search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side

        right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
        6 7 1 2 3 4 5
             mid          
        search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
        """

        while low <= high:

            """
            int low = 1170105034 
            int high = 1347855270 
            (low + high) / 2       --> outputs  -888503496 
            low + (high - low) / 2 --> outputs 1258980152 
            """
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:  # left rotated
                # in ascending order side
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:  # right rotated
                # in ascending order side
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
