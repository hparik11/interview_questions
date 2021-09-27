#!/usr/bin/env python
# coding:utf-8
"""
@FileName : unique_binary_search_tree.py
@Author   : Harsh Parikh
@Date     : 8/28/21 7:07 PM

96. Unique Binary Search Trees

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.



Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
"""


class Solution:
    def numTrees(self, n: int) -> int:
        def countTrees(n, cache):
            if n == 0:
                return 1
            if n == 1:
                return 1

            if n in cache:
                return cache[n]

            Result = 0

            for i in range(n):
                LeftTrees = countTrees(i, cache)
                RightTrees = countTrees(n - i - 1, cache)
                Result += LeftTrees * RightTrees

            cache[n] = Result

            return Result

        cache = {}
        return countTrees(n, cache)
