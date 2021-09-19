#!/usr/bin/env python
# coding:utf-8
"""
@FileName : snapchat_subset_less_than_k.py
@Author   : Harsh Parikh
@Date     : 7/9/21 4:24 PM

Given an input array, find min(subset) + max(subset) < k

input_array = [3, 2, 1, 4, 0], k=4

output = [(0), (1), (0, 1), (0, 2), (0, 3), (1, 2), (0, 1, 2), (0, 1, 2, 3)]
"""


def find_subsets_with_less_than_k(input_array, k):

    filtered_input_array = [value for value in input_array if value < k]

    sorted_input_array = sorted(filtered_input_array)

    subsets = set()

    i = 0

    while i < len(sorted_input_array):
        j = i
        while j < len(sorted_input_array):
            if sorted_input_array[i] + sorted_input_array[j] < k:
                if sorted_input_array[i] != sorted_input_array[j]:
                    subsets.add(tuple((sorted_input_array[i], sorted_input_array[j])))
                subsets.add(tuple(sorted_input_array[i: j+1]))

            j += 1
        i += 1

    return subsets


if __name__ == '__main__':
    print(find_subsets_with_less_than_k([3, 2, 1, 4, 0], 4))
