#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_longest_subarray_with_sum_k.py
@Author   : Harsh Parikh
@Date     : 7/17/21 3:20 PM

Longest sub-array having sum k
Difficulty Level : Hard
Last Updated : 21 May, 2021
Given an array arr[] of size n containing integers. The problem is to find the length of the longest sub-array having sum equal to the given value k.
Examples:


Input : arr[] = { 10, 5, 2, 7, 1, 9 },
            k = 15
Output : 4
The sub-array is {5, 2, 7, 1}.

Input : arr[] = {-5, 8, -14, 2, 4, 12},
            k = -5
Output : 5
"""


# Python3 implementation to find the length
# of longest subArray having sum k

# function to find the longest
# subarray having sum k
def lenOfLongSubarr(arr, n, k):
    # dictionary mydict implemented
    # as hash map
    mydict = dict()

    # Initialize sum and maxLen with 0
    sum = 0
    maxLen = 0

    # traverse the given array
    for i in range(n):

        # accumulate the sum
        sum += arr[i]

        # when subArray starts from index '0'
        if sum == k:
            maxLen = i + 1

        # check if 'sum-k' is present in
        # mydict or not
        elif (sum - k) in mydict:
            maxLen = max(maxLen, i - mydict[sum - k])

        # if sum is not present in dictionary
        # push it in the dictionary with its index
        if sum not in mydict:
            mydict[sum] = i

    return maxLen


# Driver Code
if __name__ == '__main__':
    arr = [10, 5, 2, 7, 1, 9]
    n = len(arr)
    k = 15
    print("Length =", lenOfLongSubarr(arr, n, k))