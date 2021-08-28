#!/usr/bin/env python
# coding:utf-8
"""
@FileName : inorder_successor_bst.py
@Author   : Harsh Parikh
@Date     : 7/1/21 12:07 AM

285. Inorder Successor in BST
https://leetcode.com/problems/inorder-successor-in-bst/

Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.



Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        """
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ
        """
        if not root:
            return TreeNode(None)

        lastRootElem = None

        while root:
            if root == p:
                if root.right:
                    return self.findLeftMostNode(root.right)

                return lastRootElem
            elif root.val < p.val:
                root = root.right
            else:
                lastRootElem = root
                root = root.left

    @staticmethod
    def findLeftMostNode(node):
        currentNode = node

        while currentNode.left is not None:
            currentNode = currentNode.left

        return currentNode


if __name__ == '__main__':

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    s = Solution()

    print(s.inorderSuccessor())

