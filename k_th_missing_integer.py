#!/usr/bin/env python
# coding:utf-8
"""
@FileName : k_th_missing_integer.py
@Author   : Harsh Parikh
@Date     : 7/29/21 11:22 PM

1539. Kth Missing Positive Number
Easy

1243

79

Add to List

Share
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.



Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
"""


class Solution:
    def findKthPositive(self, arr, k: int) -> int:

        positive_integer = 1
        array_ptr = 0

        missing_positive_integer = 0

        while array_ptr < len(arr):
            if positive_integer == arr[array_ptr]:
                array_ptr += 1

            else:
                missing_positive_integer += 1
                if missing_positive_integer == k:
                    return positive_integer

            positive_integer += 1

        return (positive_integer - 1) + (k - missing_positive_integer)

