#!/usr/bin/env python
# coding:utf-8
"""
@FileName : all_subsets_of_given_list.py
@Author   : Harsh Parikh
@Date     : 7/14/21 12:23 AM


Input: [1, 2, 3]

Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
"""


def powerset(array):
    # Write your code here.

    subsets = [[]]

    for elem in array:
        for i in range(len(subsets)):
            currentSubSet = subsets[i]
            subsets.append(currentSubSet + [elem])

    return subsets


def subsets(self, nums):
    res = []
    self.generateSubsets(nums, res, [], 0)
    return res


def generateSubsets(self, nums, res, curr, index):
    res.append(list(curr))
    for i in range(index, len(nums)):
        curr.append(nums[i])
        self.generateSubsets(nums, res, curr, i + 1)
        curr.pop()


if __name__ == '__main__':
    print(powerset([1, 2, 3]))
