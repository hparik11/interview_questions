#!/usr/bin/env python
# coding:utf-8
"""
@FileName : path_sum_III.py
@Author   : Harsh Parikh
@Date     : 8/13/21 5:43 PM
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        def dfs(prefixSumHash, prefixSum, targetSum, node):
            nonlocal count

            if not node:
                return

            # current prefix sum
            prefixSum += node.val

            # here is the count we're looking for
            # number of times the prefixSum − targetSum has occurred already,
            # determines the number of times a path with targetSum
            # has occurred up to the current node
            count += prefixSumHash[prefixSum - targetSum]

            # add the current sum into hashmap
            # to use it during the child nodes processing
            prefixSumHash[prefixSum] += 1

            if node.left:
                dfs(prefixSumHash, prefixSum, targetSum, node.left)

            if node.right:
                dfs(prefixSumHash, prefixSum, targetSum, node.right)

            # After processing children, we need to remove them from hashmap to avoid
            # Another subtree prefix calculation
            prefixSumHash[prefixSum] -= 1

        prefixSumHash = collections.defaultdict(int, {0: 1})
        count = 0
        dfs(prefixSumHash, 0, targetSum, root)

        return count
