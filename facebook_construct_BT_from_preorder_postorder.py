#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_construct_BT_from_preorder_postorder.py
@Author   : Harsh Parikh
@Date     : 9/6/21 9:16 PM

889. Construct Binary Tree from Preorder and Postorder Traversal

Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.



Example 1:

      3
     / \
    9   20
       /  \
      15   7

pre = [3, 9, 20, 15, 7]
post = [9, 15, 7, 20, 3]
Output = [3,9,20,null,null,15,7]

Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def helper(pre, post):
            print('pre is: ', pre, 'post is: ', post)

            if not pre:
                return None

            if len(pre) == 1:
                return TreeNode(post.pop())

            node = TreeNode(post.pop())  # 3
            ind = pre.index(post[-1])  # 4

            node.right = helper(pre[ind:], post)  # 1
            node.left = helper(pre[1:ind], post)  # 2

            return node

        return helper(preorder, postorder)