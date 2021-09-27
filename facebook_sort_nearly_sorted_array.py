#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_sort_nearly_sorted_array.py
@Author   : Harsh Parikh
@Date     : 9/13/21 3:48 PM

Sort a nearly sorted (or K sorted) array
Difficulty Level : Medium
Last Updated : 12 Aug, 2021

Given an array of n elements, where each element is at most k away from its target position, devise an algorithm that sorts in O(n log k) time. For example, let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

Examples:

Input : arr[] = {6, 5, 3, 2, 8, 10, 9}
            k = 3
Output : arr[] = {2, 3, 5, 6, 8, 9, 10}

Input : arr[] = {10, 9, 8, 7, 4, 70, 60, 50}
         k = 4
Output : arr[] = {4, 7, 8, 9, 10, 50, 60, 70}
"""

import heapq
from heapq import heappop, heappush


# Function to sort a k–sorted array
def sort_k_sorted_arr(list, k):
    # build a min-heap from the first `k+1` elements in the list
    pq = list[0:k + 1]
    heapq.heapify(pq)

    # do for remaining elements in the list
    index = 0
    for i in range(k + 1, len(list)):
        # pop the top element from the min-heap and assign them to the
        # next available list index
        list[index] = heappop(pq)
        index = index + 1

        # push the next list element into min-heap
        heappush(pq, list[i])

    # pop all remaining elements from the min-heap and assign them to the
    # next available list index
    while pq:
        list[index] = heappop(pq)
        index = index + 1


if __name__ == '__main__':
    list = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
    k = 2

    sort_k_sorted_arr(list, k)
    print(list)
