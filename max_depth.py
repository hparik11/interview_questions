# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: max_depth.py
# @Date:   8/13/20, Thu

"""
104. Maximum Depth of Binary Tree
Easy

2692

78

Add to List

Share
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = deque([root])
        depth = 0
        node_level = 1
        while stack:
            node = stack.popleft()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node_level -= 1
            if node_level == 0:
                depth += 1
                node_level = len(stack)

        return depth