# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: amazon_distance_between_nodes_binary_tree.py
# @Date:   9/24/20, Thu
"""
Given a list of unique integers nums,
construct a BST from it (you need to insert nodes one-by-one with the given order to get the BST)
and find the distance between two nodes node1 and node2.
Distance is the number of edges between two nodes. If any of the given nodes does not appear in the BST, return -1.

Example 1:

Input: nums = [2, 1, 3], node1 = 1, node2 = 3
Output: 2
Explanation:
     2
   /   \
  1     3

"""

from typing import Optional


# binary tree node
class Node:
    # Constructor to create new node
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution:
    def lowestCommonAncestor(self, root: Node, p: Node, q: Node) -> Optional[Node]:
        # found p and q?
        if not root or root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None: print("Left", left.val)
        if right is not None: print("Right", right.val)

        # p and q appears in left and right respectively, then their ancestor is root
        if left is not None and right is not None:
            return root

        # p and q not in left, then it must be in right, otherwise left
        if left is None:
            return right

        if right is None:
            return left

    def findLevel(self, lca, n1, level):
        if lca is None:
            return

        if lca.val == n1.val:
            return level

        return self.findLevel(lca.left, n1, level + 1) or self.findLevel(lca.right, n1, level + 1)

    def findDistance(self, root1, n1, n2):
        lca = self.lowestCommonAncestor(root1, n1, n2)

        return self.findLevel(lca, n1, 0) + self.findLevel(lca, n2, 0)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)

    s = Solution()

    print(s.findDistance(root, Node(6), Node(8)))
