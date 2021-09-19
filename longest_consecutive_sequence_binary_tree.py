#!/usr/bin/env python
# coding:utf-8
"""
@FileName : longest_consecutive_sequence_binary_tree.py
@Author   : Harsh Parikh
@Date     : 8/7/21 6:59 PM

Given a tree, write a function to find the length of the longest branch of nodes in increasing consecutive order.

         0
       /  \
      1    2
     / \  / \
    3  2  1  3

Output = 0->1->2

"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:

    def find_consecutive_path(self, node, parentValue, length):
        if not node:
            return length

        if node.value == parentValue + 1:
            leftLength = self.find_consecutive_path(node.left, node.value, length + 1)
            rightLength = self.find_consecutive_path(node.right, node.value, length + 1)
        else:
            leftLength = self.find_consecutive_path(node.left, node.value, 1)
            rightLength = self.find_consecutive_path(node.right, node.value, 1)

        return max(leftLength, rightLength, length)

    def find_consecutive_order_binary_tree(self, root):
        if not root:
            return 0

        return max(self.find_consecutive_path(root.left, root.value, 1),
                   self.find_consecutive_path(root.right, root.value, 1))


if __name__ == '__main__':
    root = BinaryTree(0)
    root.left = BinaryTree(1)
    root.right = BinaryTree(2)
    root.left.left = BinaryTree(3)
    root.left.left.left = BinaryTree(4)
    root.left.left.left.left = BinaryTree(5)

    root.left.right = BinaryTree(2)
    root.left.right.right = BinaryTree(3)

    root.right.left = BinaryTree(1)
    root.right.right = BinaryTree(3)

    s = Solution()
    print(s.find_consecutive_order_binary_tree(root))
