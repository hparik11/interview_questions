#!/usr/bin/env python
# coding:utf-8
"""
@FileName : subarray_sort.py
@Author   : Harsh Parikh
@Date     : 8/12/21 11:20 PM

Write a function that takes in an array of integers of length at least 2.
The function should return an array of the starting and ending indices of the
smallest subarray in the input array that needs to be sorted in place in order
for the entire input array to be sorted. If the input array is already sorted,
the function should return [-1, -1].

Sample input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19] Sample output: [3, 9]


"""


def subarraySort(array):
    # Write your code here.
    minValue = float("inf")
    maxValue = float("-inf")

    for index, num in enumerate(array):
        if isOutOfOrder(index, num, array):
            minValue = min(minValue, num)
            maxValue = max(maxValue, num)

    if minValue == float("inf") or maxValue == float("-inf"):
        return [-1, -1]

    leftIndex = 0
    while leftIndex < len(array) and minValue >= array[leftIndex]:
        leftIndex += 1

    rightIndex = len(array) - 1
    while rightIndex >= 0 and maxValue <= array[rightIndex]:
        rightIndex -= 1

    return [leftIndex, rightIndex]


def isOutOfOrder(index, num, array):
    if index == 0:
        return num > array[index + 1]
    elif index == len(array) - 1:
        return num < array[index - 1]
    else:
        return array[index + 1] < num or num < array[index - 1]