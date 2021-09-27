#!/usr/bin/env python
# coding:utf-8
"""
@FileName : inorder_successor_bt.py
@Author   : Harsh Parikh
@Date     : 7/14/21 11:22 AM
"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(node):
    # Write your code here.
    if node.right:
        return findLeftMostNode(node.right)

    return findRightMostParent(node)


def findRightMostParent(node):
    currentNode = node
    while currentNode.parent is not None and currentNode == currentNode.parent.right:
        currentNode = currentNode.parent

    return currentNode.parent


def findLeftMostNode(node):
    currentNode = node

    while currentNode.left is not None:
        currentNode = currentNode.left

    return currentNode


if __name__ == '__main__':
    """
            1
           / \
          2   3
         / \
        4   5
       /
      6  
    """
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.parent = root
    root.right = BinaryTree(3)
    root.right.parent = root
    root.left.left = BinaryTree(4)
    root.left.left.parent = root.left
    root.left.right = BinaryTree(5)
    root.left.right.parent = root.left
    root.left.left.left = BinaryTree(6)
    root.left.left.left.parent = root.left.left

    node = root.left.right  # 5

    print(findSuccessor(node).value)
