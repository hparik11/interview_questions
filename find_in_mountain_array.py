#!/usr/bin/env python
# coding:utf-8
"""
@FileName : find_in_mountain_array.py
@Author   : Harsh Parikh
@Date     : 8/31/21 7:05 PM

1095. Find in Mountain Array

(This problem is an interactive problem.)

You may recall that an array A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.



Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
"""


def find_peak_in_mountain_array(array):
    low = 0
    high = len(array) - 1

    while low < high:
        mid = low + (high - low) // 2

        if array[mid] > array[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return low  # or high because low = high


def binary_search(array, target, start, end, isAscendingOrder=True):
    low = start
    high = end

    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == target:
            return mid

        if isAscendingOrder:
            if array[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if array[mid] > target:
                low = mid + 1
            else:
                high = mid - 1
    return -1


def find_in_mountain_array(array, target):
    peakIndex = find_peak_in_mountain_array(array)
    if array[peakIndex] == target:
        return peakIndex
    # If element on left hand side
    leftSide = binary_search(array, target, 0, peakIndex - 1, True)

    # if not then look right hand side
    if leftSide == -1:
        return binary_search(array, target, peakIndex + 1, len(array) - 1, False)
    return leftSide


if __name__ == '__main__':
    array = [0, 2, 3, 4, 5, 3, 1]
    print(find_in_mountain_array(array, 3))
    print(find_in_mountain_array(array, 1))
