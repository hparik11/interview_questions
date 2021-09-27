#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_count_continuous_subarray.py
@Author   : Harsh Parikh
@Date     : 7/30/21 12:23 PM

Contiguous Subarrays
You are given an array arr of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfill the following conditions:
The value at index i must be the maximum element in the contiguous subarrays, and
These contiguous subarrays must either start from or end on index i.
Signature
int[] count Subarrays(int[] arr)
Input
Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
Size N is between 1 and 1,000,000
Output
An array where each index i contains an integer denoting the maximum number of contiguous subarrays of arr[i]
Example:
arr = [3, 4, 1, 6, 2]
output = [1, 3, 1, 5, 1]
Explanation:
For index 0 - [3] is the only contiguous subarray that starts (or ends) with 3, and the maximum value in this subarray is 3.
For index 1 - [4], [3, 4], [4, 1]
For index 2 - [1]
For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
For index 4 - [2]
So, the answer for the above input is [1, 3, 1, 5, 1]
"""


def count_subarrays(arr):
    # Write your code here
    n = len(arr)
    res = [1] * n

    # Left
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()

        if not stack:
            res[i] += i
        else:
            res[i] += i - 1 - stack[-1]

        stack.append(i)

    # Right
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        if not stack:
            res[i] += n - 1 - i
        else:
            res[i] += stack[-1] - 1 - i
        stack.append(i)

    return res


if __name__ == '__main__':
    print(count_subarrays([3, 4, 1, 6, 1]))
