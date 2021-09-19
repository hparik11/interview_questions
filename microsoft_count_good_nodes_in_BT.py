#!/usr/bin/env python
# coding:utf-8
"""
@FileName : microsoft_count_good_nodes_in_BT.py
@Author   : Harsh Parikh
@Date     : 7/30/21 12:32 AM

1448. Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        maxValueSoFar = float('-inf')
        queue = deque([(root, maxValueSoFar)])
        goodNodes = 0

        while queue:
            node, maxValueSoFar = queue.popleft()

            if node.val >= maxValueSoFar:
                goodNodes += 1
                maxValueSoFar = node.val

            if node.left:
                queue.append((node.left, maxValueSoFar))

            if node.right:
                queue.append((node.right, maxValueSoFar))

        return goodNodes
