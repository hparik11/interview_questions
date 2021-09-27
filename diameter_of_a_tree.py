#!/usr/bin/env python
# coding:utf-8
"""
@FileName : diameter_of_a_tree.py
@Author   : Harsh Parikh
@Date     : 7/24/21 12:12 PM

543. Diameter of Binary Tree
Share
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.



Example 1:


Input: root = [1,2,3,4,5]
        1
       / \
      2   3
    / \
   4   5
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeInfo:
    def __init__(self, diameter, depth):
        self.diameter = diameter
        self.depth = depth


def getTreeInfo(tree):
    if not tree:
        return TreeInfo(0, 0)

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPath = leftTreeInfo.depth + rightTreeInfo.depth
    maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)

    currentNodeDiameter = max(maxDiameterSoFar, longestPath)

    currentMaxDepth = 1 + max(leftTreeInfo.depth, rightTreeInfo.depth)

    return TreeInfo(currentNodeDiameter, currentMaxDepth)


def binaryTreeDiameter(tree):
    # Write your code here.
    return getTreeInfo(tree).diameter
