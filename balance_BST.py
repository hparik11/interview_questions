#!/usr/bin/env python
# coding:utf-8
"""
@FileName : balance_BST.py
@Author   : Harsh Parikh
@Date     : 9/13/21 10:59 AM

1382. Balance a Binary Search Tree

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.



Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []

        def inorder(node, nums):
            """
            Convert BST to ascending sequence
            """
            if node:
                inorder(node.left, nums)
                nums.append(node.val)
                inorder(node.right, nums)

        # ----------------------------------------

        def sequence_to_balanced_BST(left, right, nums):
            """
            Convert ascending sequence to balanced BST
            """
            if left > right:
                # Base case:
                return None

            else:
                # General case:

                mid = left + (right - left) // 2

                root = TreeNode(nums[mid])

                root.left = sequence_to_balanced_BST(left, mid - 1, nums)
                root.right = sequence_to_balanced_BST(mid + 1, right, nums)

                return root

        # ----------------------------------------

        # Flatten original BST into a ascending sorted sequence.
        inorder(root, nums)

        # Convert ascending sorted sequence into Balanced BST by the algorithm in Leetcode #108
        return sequence_to_balanced_BST(left=0, right=len(nums) - 1, nums=nums)
