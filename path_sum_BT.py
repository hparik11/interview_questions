# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: path_sum_BT.py
# @Date:   8/14/20, Fri

"""
112. Path Sum
Given a binary tree and a sum, determine if the tree has a
root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Recursive
"""


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if root is None:
            return False

        if not root.left and not root.right:
            return sum == root.val
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


"""
Iterative
"""


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if not root:
            return False

        stack = [(root, sum - root.val)]

        while stack:
            node, sum = stack.pop()
            if not node.left and not node.right and sum == 0:
                return True
            if node.left:
                stack.append((node.left, sum - node.left.val))
            if node.right:
                stack.append((node.right, sum - node.right.val))
        return False
