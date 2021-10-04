#!/usr/bin/env python
# coding:utf-8
"""
@FileName : binary_tree_upside_down.py
@Author   : Harsh Parikh
@Date     : 10/2/21 7:30 PM

156. Binary Tree Upside Down

Given the root of a binary tree, turn the tree upside down and return the new root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.

The mentioned steps are done level by level. It is guaranteed that every right node has a sibling (a left node with the same parent) and has no children.



Example 1:


Input: root = [1,2,3,4,5]
Output: [4,5,2,null,null,3,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        stack = []
        while root:
            stack.append(root)
            root = root.left

        dummy = TreeNode(None)
        curr = dummy

        while stack:
            node = stack.pop()
            curr.left = node.right
            curr.right = node

            curr = curr.right

        curr.left = None
        curr.right = None

        return dummy.right
