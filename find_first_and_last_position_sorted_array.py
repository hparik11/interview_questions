#!/usr/bin/env python
# coding:utf-8
"""
@FileName : find_first_and_last_position_sorted_array.py
@Author   : Harsh Parikh
@Date     : 8/8/21 11:59 PM

34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""


class Solution:
    def searchRange(self, nums, target):
        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if x > A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if x >= A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

            return right

        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]
