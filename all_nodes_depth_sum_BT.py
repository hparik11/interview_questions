#!/usr/bin/env python
# coding:utf-8
"""
@FileName : all_nodes_depth_sum_BT.py
@Author   : Harsh Parikh
@Date     : 8/8/21 1:14 PM

          1
       /     \
      2       3
    /   \   /   \
   4     5 6     7
 /   \
8     9

"""


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution1:
    # Time O(nlong) | Space O(n)
    def allKindsOfNodeDepths(self, root):
        # Write your code here.

        def findDepth(node, depth):
            if node is None:
                return 0
            return depth + findDepth(node.left, depth + 1) + findDepth(node.right, depth + 1)

        stack = [root]
        depth_sum = 0
        while len(stack) > 0:
            node = stack.pop()
            depth_sum += findDepth(node, 0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return depth_sum


class Solution2:
    # O(N) time and O(H) space
    def allKindsOfNodeDepths(self, root):
        # Write your code here.
        return self.getTreeInfo(root).sumOfAllDepths

    @classmethod
    def getTreeInfo(cls, tree):
        if tree is None:
            return TreeInfo(0, 0, 0)

        leftTreeInfo = cls.getTreeInfo(tree.left)
        rightTreeInfo = cls.getTreeInfo(tree.right)

        sumOfLeftDepths = leftTreeInfo.sumOfDepths + leftTreeInfo.numNodesInTree
        sumOfRightDepths = rightTreeInfo.sumOfDepths + rightTreeInfo.numNodesInTree

        numNodesInTree = 1 + leftTreeInfo.numNodesInTree + rightTreeInfo.numNodesInTree
        sumOfDepths = sumOfLeftDepths + sumOfRightDepths
        sumOfAllDepths = sumOfDepths + leftTreeInfo.sumOfAllDepths + rightTreeInfo.sumOfAllDepths

        return TreeInfo(numNodesInTree, sumOfDepths, sumOfAllDepths)


class TreeInfo:
    def __init__(self, numNodesInTree, sumOfDepths, sumOfAllDepths):
        self.numNodesInTree = numNodesInTree
        self.sumOfDepths = sumOfDepths
        self.sumOfAllDepths = sumOfAllDepths
