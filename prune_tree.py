# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: prune_tree.py
# @Date:   9/5/20, Sat
"""
Binary Tree Pruning

We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]

Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.


Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]



Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]



"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return root
        if not root.left and not root.right:
            if root.val == 0:
                return None
            else:
                return root

        root.left = self.pruneTree(root.left)

        root.right = self.pruneTree(root.right)

        if root.val == 0 and (not root.left and not root.right):
            return None
        else:
            return root
