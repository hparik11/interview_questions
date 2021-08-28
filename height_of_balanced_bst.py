#!/usr/bin/env python
# coding:utf-8
"""
@FileName : height_of_balanced_bst.py
@Author   : Harsh Parikh
@Date     : 6/19/21 9:08 PM
"""

import unittest


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, height, isbalanced):
        self.height = height
        self.isbalanced = isbalanced


def heightOfTree(node):
    if not node:
        return TreeInfo(0, True)

    leftSubTreeHeightTreeInfo = heightOfTree(node.left)
    rightSubTreeHeightTreeInfo = heightOfTree(node.right)
    isBalanced = False

    if (abs(leftSubTreeHeightTreeInfo.height - rightSubTreeHeightTreeInfo.height) <= 1) \
            and leftSubTreeHeightTreeInfo.isbalanced \
            and rightSubTreeHeightTreeInfo.isbalanced:
        isBalanced = True

    return TreeInfo(1 + max(leftSubTreeHeightTreeInfo.height, rightSubTreeHeightTreeInfo.height), isBalanced)


def heightBalancedBinaryTree(tree):
    # Write your code here.

    if not tree:
        return True

    treeInfo = heightOfTree(tree)
    print(treeInfo.height)

    return treeInfo.isbalanced


if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.right = BinaryTree(6)
    root.left.right.left = BinaryTree(7)
    root.left.right.right = BinaryTree(8)

    actual = heightBalancedBinaryTree(root)

    print(actual)
