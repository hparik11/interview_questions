#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_flip_binary_trees.py
@Author   : Harsh Parikh
@Date     : 10/1/21 12:22 PM

951. Flip Equivalent Binary Trees

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivelent or false otherwise.



Example 1:

Flipped Trees Diagram
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Example 2:

Input: root1 = [], root2 = []
Output: true
Example 3:

Input: root1 = [], root2 = [1]
Output: false
Example 4:

Input: root1 = [0,null,1], root2 = []
Output: false
Example 5:

Input: root1 = [0,null,1], root2 = [0,1]
Output: true
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        Complexity Analysis

        Time Complexity: O(min(N_1, N_2))

        Space Complexity: O(min(H_1, H_2))

        """
        def dfs(node1, node2):

            if not node1 and not node2:
                return True

            if not node1 or not node2 or node1.val != node2.val:
                return False

            no_flip = dfs(node1.left, node2.left) and dfs(node1.right, node2.right)

            with_flip = dfs(node1.left, node2.right) and dfs(node1.right, node2.left)

            return no_flip or with_flip

        return dfs(root1, root2)
