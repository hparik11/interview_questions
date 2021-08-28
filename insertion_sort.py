#!/usr/bin/env python
# coding:utf-8
"""
@FileName : insertion_sort.py
@Author   : Harsh Parikh
@Date     : 6/28/21 2:02 AM
"""


def insertionSort(array):
    # Write your code here.

    for i in range(1, len(array)):
        j = i

        while j > 0 and array[j] <= array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

    return array


# Verify it works
random_list_of_nums = [12, 8, 3, 20, 11]
insertionSort(random_list_of_nums)
print(random_list_of_nums)
