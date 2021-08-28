#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_find_frequency_of_elements_in_sorted_array.py
@Author   : Harsh Parikh
@Date     : 8/8/21 12:25 AM

Given a sorted array of integers, find the number of a specific integer.
E.g. [1,2,3,3,5], q=3 returns 2. There are 2 3's in the array.
[1,2,3,3,5], q=4 returns 0. There is no 4 in the array.
"""

import bisect


def find_leftmost_index_of_element(array, target, low, high):
    res = -1
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == target:
            res = mid
            high = mid - 1
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return res


def find_rightmost_index_of_element(array, target, low, high):
    res = -1
    while low <= high:
        mid = low + (high - low) // 2  #
        if array[mid] == target:
            res = mid
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return res


def find_frequency_of_elements_in_sorted_array(array, target):
    low = 0
    high = len(array) - 1

    print(find_leftmost_index_of_element(array, target, low, high))
    print(find_rightmost_index_of_element(array, target, low, high))


if __name__ == '__main__':
    print(find_frequency_of_elements_in_sorted_array([1, 2, 3, 3, 3, 5], 3))
    # print(find_frequency_of_elements_in_sorted_array([1, 2, 3, 3, 5], 3))
