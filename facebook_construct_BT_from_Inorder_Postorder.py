#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_construct_BT_from_Inorder_Preorder.py
@Author   : Harsh Parikh
@Date     : 7/17/21 8:27 PM

106. Construct Binary Tree from Inorder and Postorder Traversal
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder) > 0 and len(inorder) > 0:
            rootValue = postorder.pop()

            ind = inorder.index(rootValue)

            root = TreeNode(rootValue)

            root.right = self.buildTree(inorder[ind + 1:], postorder)

            root.left = self.buildTree(inorder[0:ind], postorder)

            return root


if __name__ == '__main__':
    postorder = [9, 15, 7, 20, 3]
    inorder = [9, 3, 15, 20, 7]

    s = Solution()
    print(s.buildTree(inorder, postorder))
