# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: path_sum_BT_II.py
# @Date:   8/15/20, Sat

"""
113. Path Sum II
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return []

        path = [root.val]
        paths = []

        self.findPathSum(root, sum, path, paths)
        return paths

    def findPathSum(self, node, sum, path, paths):

        if not node.left and not node.right:
            if sum == node.val:
                paths.append(path)
        else:
            if node.left:
                self.findPathSum(node.left, sum - node.val, path + [node.left.val], paths)
            if node.right:
                self.findPathSum(node.right, sum - node.val, path + [node.right.val], paths)
