#!/usr/bin/env python
# coding:utf-8
"""
@FileName : find_k_largest_value_BST.py
@Author   : Harsh Parikh
@Date     : 7/3/21 9:18 PM
"""


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    elements = []
    reverseInOrderTraversal(tree, elements, k)
    return elements[k - 1]


def reverseInOrderTraversal(tree, elements, k):
    if not tree or len(elements) >= k:
        return

    # print(tree.value)
    reverseInOrderTraversal(tree.right, elements, k)
    elements.append(tree.value)
    reverseInOrderTraversal(tree.left, elements, k)


if __name__ == '__main__':
    root = BST(15)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.left.right = BST(3)
    root.left.right = BST(5)
    root.right = BST(20)
    root.right.left = BST(17)
    root.right.right = BST(22)

    k = 3

    print(findKthLargestValueInBst(root, k))
