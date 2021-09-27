#!/usr/bin/env python
# coding:utf-8
"""
@FileName : find_ceil_floor_in_binary_search.py
@Author   : Harsh Parikh
@Date     : 8/31/21 5:19 PM

1. input = [1, 4, 5, 8, 9, 14, 16, 18], target = 15
    output = 16

2. input = [1, 4, 5, 8, 9, 14, 15, 18], target = 15
    output = 15

"""

import bisect


def find_ceil_bst(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == target:
            return array[mid]
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return array[low]


def find_floor_bst(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == target:
            return array[mid]
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return array[high]


if __name__ == '__main__':
    print(find_ceil_bst([1, 4, 5, 8, 9, 14, 15, 16, 18], 15))
    print(bisect.bisect_left([1, 4, 5, 8, 9, 14, 15, 16, 18], 15))
    print(find_ceil_bst([1, 4, 5, 8, 9, 14, 15, 18], 15))

    print(find_floor_bst([1, 4, 5, 8, 9, 14, 16, 18], 15))
    print(find_floor_bst([1, 4, 5, 8, 9, 14, 15, 18], 15))
