#!/usr/bin/env python
# coding:utf-8
"""
@FileName : subsets.py
@Author   : Harsh Parikh
@Date     : 8/3/21 12:04 AM

78. Subsets
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""


class Solution:
    def subsets(self, nums):
        res = []
        self.generateSubsets(nums, res, [], 0)
        return res

    def generateSubsets(self, nums, res, curr, index):

        if index > len(nums):
            return

        res.append(curr[:])

        for i in range(index, len(nums)):
            curr.append(nums[i])
            print("Append: ", curr[:])
            self.generateSubsets(nums, res, curr, i + 1)
            curr.pop()
            print("Popped: ", curr[:])


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))
