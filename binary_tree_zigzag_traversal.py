#!/usr/bin/env python
# coding:utf-8
"""
@FileName : binary_tree_zigzag_traversal.py
@Author   : Harsh Parikh
@Date     : 7/24/21 12:44 PM

103. Binary Tree Zigzag Level Order Traversal
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        levelOrderQueue = deque([root])
        leftSide = True
        zigZagOrder = []

        while levelOrderQueue:
            totalElementsAtCurrentLevel = len(levelOrderQueue)
            tempArray = []
            for _ in range(totalElementsAtCurrentLevel):
                currentNode = levelOrderQueue.popleft()
                if currentNode.left:
                    levelOrderQueue.append(currentNode.left)
                if currentNode.right:
                    levelOrderQueue.append(currentNode.right)

                tempArray.append(currentNode.val)

            if leftSide:
                zigZagOrder.append(tempArray)
            else:
                zigZagOrder.append(tempArray[::-1])

            leftSide = not leftSide

        return zigZagOrder
