# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: min
# @Date:   8/13/20, Thu

"""
111. Minimum Depth of Binary Tree
Easy

1530

704

Add to List

Share
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        depth = 1
        node_level = 1
        while stack:
            node = stack.pop(0)
            if node.left is None and node.right is None:
                return depth
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node_level -= 1
            if node_level == 0:
                depth += 1
                node_level = len(stack)

        return depth
