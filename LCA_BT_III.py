#!/usr/bin/env python
# coding:utf-8
"""
@FileName : LCA_BT_III.py
@Author   : Harsh Parikh
@Date     : 7/23/21 8:04 PM

1650. Lowest Common Ancestor of a Binary Tree III

Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."



Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        def findDescendant(node, targetNode):
            if not node:
                return

            if node == targetNode:
                return True

            leftSide = findDescendant(node.left, targetNode)
            rightSide = findDescendant(node.right, targetNode)

            if leftSide or rightSide:
                return True

            return False

        def findNodeDepth(node, depth):
            if node.parent is None:
                return depth

            return findNodeDepth(node.parent, depth + 1)

        if findDescendant(p, q):
            return p
        elif findDescendant(q, p):
            return q

        pDepth = findNodeDepth(p, 0)
        qDepth = findNodeDepth(q, 0)

        # Move the lower pointer up so that they are each at the same level.
        # For the smaller depth (p_depth < q_depth or q_depth < p_depth),
        # the loop will be skipped and the pointer will stay at the same depth.
        for _ in range(pDepth - qDepth):
            p = p.parent
        for _ in range(qDepth - pDepth):
            q = q.parent

        # Now that they are at the same depth, move them up the tree in parallel until they meet
        while p != q:
            p = p.parent
            q = q.parent

        return p
