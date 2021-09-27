#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_find_k_closest_elements.py
@Author   : Harsh Parikh
@Date     : 9/17/21 1:59 AM

658. Find K Closest Elements
Medium

3179

360

Add to List

Share
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

"""


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Base case
        if len(arr) == k:
            return arr

        # Find the closest element and initialize two pointers
        left = bisect_left(arr, x) - 1
        right = left + 1

        if left == len(arr) - 1:
            right = left

        # While the window size is less than k
        while right - left - 1 < k:
            # Be careful to not go out of bounds
            if left == -1:
                right += 1
                continue

            # Expand the window towards the side with the closer number
            # Be careful to not go out of bounds with the pointers
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        # Return the window
        return arr[left + 1:right]