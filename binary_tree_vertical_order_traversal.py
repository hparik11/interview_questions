#!/usr/bin/env python
# coding:utf-8
"""
@FileName : binary_tree_vertical_order_traversal.py
@Author   : Harsh Parikh
@Date     : 7/22/21 11:06 AM

314. Binary Tree Vertical Order Traversal

Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
Example 4:

Input: root = []
Output: []
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        idToNode = defaultdict(list)

        queue = deque([(root, 0)])
        vertical_traversal_list = []

        while queue:
            curr, idx = queue.popleft()
            idToNode[idx].append(curr.val)

            if curr.left is None and curr.right is None:
                continue

            if curr.left:
                queue.append((curr.left, idx - 1))

            if curr.right:
                queue.append((curr.right, idx + 1))

        for idx, values in sorted(idToNode.items()):
            vertical_traversal_list.append(values)

        return vertical_traversal_list
