#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_closest_BST_value.py
@Author   : Harsh Parikh
@Date     : 9/17/21 1:39 AM

270. Closest Binary Search Tree Value
Easy

1200

82

Add to List

Share
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.



Example 1:


Input: root = [4,2,5,1,3], target = 3.714286
Output: 4
Example 2:

Input: root = [1], target = 4.428571
Output: 1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.closest = float('inf')

        def helper(root):
            if not root:
                return
            if abs(root.val - target) < abs(self.closest - target):
                self.closest = root.val

            # Target should be located on left subtree
            if target < root.val:
                helper(root.left)

            # target should be located on right subtree
            if target > root.val:
                helper(root.right)

        helper(root)

        return self.closest
