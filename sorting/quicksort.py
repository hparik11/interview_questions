#!/usr/bin/env python
# coding:utf-8
"""
@FileName : quicksort.py
@Author   : Harsh Parikh
@Date     : 7/1/21 12:04 AM
"""


def quickSort(array):
    # Write your code here.
    if len(array) <= 1:
        return array

    quickSortUtil(array, 0, len(array) - 1)

    return array


def quickSortUtil(array, startIndex, endIndex):
    if startIndex >= endIndex:
        return

    pivotIndex = startIndex
    leftIndex = startIndex + 1
    rightIndex = endIndex

    while leftIndex <= rightIndex:
        if array[rightIndex] < array[pivotIndex] < array[leftIndex]:
            swap(array, leftIndex, rightIndex)

        if array[leftIndex] <= array[pivotIndex]:
            leftIndex += 1

        if array[rightIndex] >= array[pivotIndex]:
            rightIndex -= 1

    swap(array, pivotIndex, rightIndex)

    quickSortUtil(array, startIndex, rightIndex - 1)
    quickSortUtil(array, rightIndex + 1, endIndex)


def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]


if __name__ == '__main__':
    input_array = [8, 5, 2, 9, 5, 6, 3]
    quickSort(input_array)
    print(input_array)