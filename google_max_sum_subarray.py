#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_max_sum_subarray.py
@Author   : Harsh Parikh
@Date     : 10/2/21 8:45 PM

Write an efficient program to find the sum of contiguous subarray within a
one-dimensional array of numbers that has
the largest sum.
"""


def find_subarray_with_max_sum(array):
    startIdx = 0
    maxSumSoFar = array[0]
    globalMaxSum = float('-inf')
    maxSumSubArray = []

    for i in range(1, len(array)):
        num = array[i]

        maxSumSoFar += num

        if maxSumSoFar > globalMaxSum:
            maxSumSubArray = [startIdx, i]
            globalMaxSum = maxSumSoFar

        if num > maxSumSoFar:
            startIdx = i
            maxSumSoFar = num

    if not maxSumSubArray:
        return array
    else:
        return array[maxSumSubArray[0]: maxSumSubArray[1] + 1]


if __name__ == '__main__':
    print(find_subarray_with_max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
