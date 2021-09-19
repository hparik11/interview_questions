#!/usr/bin/env python
# coding:utf-8
"""
@FileName : invert_binary_tree.py
@Author   : Harsh Parikh
@Date     : 7/5/21 9:24 PM

226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.


Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
"""

from collections import deque


def invertBinaryTree1(tree):
    # Write your code here.
    if not tree:
        return

    swapnode(tree)
    invertBinaryTree1(tree.left)
    invertBinaryTree1(tree.right)


def invertBinaryTree2(tree):
    # Write your code here.
    if not tree:
        return None

    queue = deque([tree])

    while queue:
        elem = queue.popleft()
        if elem is None:
            continue

        swapnode(elem)
        if elem.left:
            queue.append(elem.left)

        if elem.right:
            queue.append(elem.right)


def swapnode(node):
    node.left, node.right = node.right, node.left


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return root

        stack = [root]

        while stack:
            node = stack.pop()

            node.left, node.right = node.right, node.left

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return root
