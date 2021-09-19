#!/usr/bin/env python
# coding:utf-8
"""
@FileName : four_sum.py
@Author   : Harsh Parikh
@Date     : 8/12/21 10:47 PM

Problem Statement

Write a function that takes in a non-empty array of distinct integers and an integer
representing a target sum. The function should nd all quadruplets in the array
that sum up to the target sum and return a two-dimensional array of all these
quadruplets in no particular order. If no four numbers sum up to the target sum,
the function should return an empty array.

Sample input: [7, 6, 4, -1, 1, 2], 16 Sample output: [[7, 6, 4, -1], [7, 6, 1, 2]]
"""

from collections import defaultdict


def fourNumberSum(array, targetSum):
    # Write your code here.

    allPairsSum = defaultdict(list)
    quadruples = []

    for i in range(1, len(array) - 1):
        for k in range(i + 1, len(array)):
            currentSum = array[i] + array[k]

            if targetSum - currentSum in allPairsSum:
                for pair in allPairsSum[targetSum - currentSum]:
                    quadruples.append(pair + [array[i], array[k]])

        for j in range(0, i):
            currentSum = array[i] + array[j]

            allPairsSum[currentSum].append([array[j], array[i]])

    return quadruples


if __name__ == '__main__':
    print(fourNumberSum([7, 6, 4, -1, 1, 2], 16))
