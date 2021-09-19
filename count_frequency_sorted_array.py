#!/usr/bin/env python
# coding:utf-8
"""
@FileName : count_frequency_sorted_array.py
@Author   : Harsh Parikh
@Date     : 7/8/21 10:11 PM

Count number of occurrences (or frequency) in a sorted array
Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[]. Expected time complexity is O(Logn)

Examples:

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 2
  Output: 4 // x (or 2) occurs 4 times in arr[]

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 3
  Output: 1

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 1
  Output: 2

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 4
  Output: -1 // 4 doesn't occur in arr[]
"""


def count(arr, x, n):
    # get the index of first
    # occurrence of x
    i = first(arr, 0, n - 1, x, n)

    # If x doesn't exist in
    # arr[] then return -1
    if i == -1:
        return i

    # Else get the index of last occurrence
    # of x. Note that we are only looking
    # in the subarray after first occurrence
    j = last(arr, i, n - 1, x, n);

    # return count
    return j - i + 1;


# if x is present in arr[] then return
# the index of FIRST occurrence of x in
# arr[0..n-1], otherwise returns -1
def first(arr, low, high, x, n):
    if high >= low:

        # low + (high - low)/2
        mid = (low + high) // 2

        if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return first(arr, (mid + 1), high, x, n)
        else:
            return first(arr, low, (mid - 1), x, n)
    return -1;


# if x is present in arr[] then return
# the index of LAST occurrence of x
# in arr[0..n-1], otherwise returns -1
def last(arr, low, high, x, n):
    if high >= low:

        # low + (high - low)/2
        mid = (low + high) // 2;

        if (mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return last(arr, low, (mid - 1), x, n)
        else:
            return last(arr, (mid + 1), high, x, n)
    return -1


# driver program to test above functions
arr = [1, 2, 2, 3, 3, 3, 3]
x = 3  # Element to be counted in arr[]
n = len(arr)
c = count(arr, x, n)
print("%d occurs %d times " % (x, c))
