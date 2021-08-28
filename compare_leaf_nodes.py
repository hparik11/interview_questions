#!/usr/bin/env python
# coding:utf-8
"""
@FileName : compare_leaf_nodes.py
@Author   : Harsh Parikh
@Date     : 6/23/21 11:54 PM
"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def getLeafNodes(node, path):
    if not node:
        return
    if node.left is None and node.right is None:
        path.append(node.value)
    else:
        getLeafNodes(node.left, path)
        getLeafNodes(node.right, path)


def compareLeafTraversal(tree1, tree2):
    # Write your code here.
    path1 = []
    path2 = []

    getLeafNodes(tree1, path1)
    getLeafNodes(tree2, path2)

    return path1 == path2


