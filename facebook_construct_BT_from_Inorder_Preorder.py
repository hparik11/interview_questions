#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_construct_BT_from_Inorder_Preorder.py
@Author   : Harsh Parikh
@Date     : 7/17/21 8:27 PM

105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

5982

145

Add to List

Share
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.



Example 1:

      3
     / \
    9   20
       /  \
      15   7
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            rootValue = preorder.pop(0)

            ind = inorder.index(rootValue)

            root = TreeNode(rootValue)

            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])

            return root


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    s = Solution()
    print(s.buildTree(preorder, inorder))
