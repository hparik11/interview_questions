#!/usr/bin/env python
# coding:utf-8
"""
@FileName : longest_mountain_array.py
@Author   : Harsh Parikh
@Date     : 9/7/21 8:04 PM

845. Longest Mountain in Array
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.



Example 1:

Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.
"""


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        """
        Note: Mountain arrays can be naturally symmetric but also non-symmetric! Example:
         /\
           \
            \
        """
        i = 0
        ans = 0

        while i < len(arr):

            # define a new start point
            base = i

            # walk up as long as it goes
            while i + 1 < len(arr) and arr[i] < arr[i + 1]:
                i += 1

            have_we_climbed_at_all = i > base

            if have_we_climbed_at_all:
                peak = i  # then we have reached a peak
            else:
                i += 1
                continue  # otherwise we walked flat or went down without ascent hence start over

            # walk down the peak as long as it goes (now that we have a peak)
            while i + 1 < len(arr) and arr[i] > arr[i + 1]:
                i += 1

            have_we_gone_down_at_all = i > peak

            if have_we_gone_down_at_all:
                end = i
            else:
                i += 1
                continue  # otherwise we climbed back up or walked flat without descent hence start over

            # update longest mountain
            ans = max(ans, end - base + 1)

        return ans
