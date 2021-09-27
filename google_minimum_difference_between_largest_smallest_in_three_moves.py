#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_minimum_difference_between_largest_smallest_in_three_moves.py
@Author   : Harsh Parikh
@Date     : 9/18/21 12:56 PM

1509. Minimum Difference Between Largest and Smallest Value in Three Moves

Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.

Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.



Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2].
The difference between the maximum and minimum is 2-2 = 0.
Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1].
The difference between the maximum and minimum is 1-0 = 1.
Example 3:

Input: nums = [6,6,0,1,1,4,6]
Output: 2
Example 4:

Input: nums = [1,5,6,14,15]
Output: 1
"""


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        """

        If the size <= 4, then just delete all the elements and either no or one element would be left giving the answer 0.
        else sort the array
        there are 4 possibilities now:-

        delete 3 elements from left and none from right
        delete 0 elements from left and 3 from right
        delete 2 elements from left and one from right
        delete 1 elements from left and two from right

        now just print the minima.

        """

        nums.sort()
        length = len(nums)

        if length <= 4:
            return 0

        return min(nums[length - 4] - nums[0], nums[length - 1] - nums[3], nums[length - 2] - nums[2],
                   nums[length - 3] - nums[1])
