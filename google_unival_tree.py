#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_unival_tree.py
@Author   : Harsh Parikh
@Date     : 9/13/21 5:22 PM
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


def count_unival_trees(root):
    if not root:
        return 0
    elif not root.left and not root.right:
        return 1
    elif not root.left and root.data == root.right.data:
        return 1 + count_unival_trees(root.right)
    elif not root.right and root.data == root.left.data:
        return 1 + count_unival_trees(root.left)

    child_counts = count_unival_trees(root.left) + count_unival_trees(root.right)
    current_node_count = 0
    if root.data == root.left.data and root.data == root.left.data:
        current_node_count = 1

    return current_node_count + child_counts


if __name__ == '__main__':
    node_a = Node('0')
    node_b = Node('1')
    node_c = Node('0')
    node_d = Node('1')
    node_e = Node('0')
    node_f = Node('1')
    node_g = Node('1')
    node_a.left = node_b
    node_a.right = node_c
    node_c.left = node_d
    node_c.right = node_e
    node_d.left = node_f
    node_d.right = node_g

    print(count_unival_trees(node_a))
