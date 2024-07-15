# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: amazon_populate_next_right_node_tree.py
# @Date:   10/3/20, Sat
"""
Populating Next Right Pointers in Each Node II

Share
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, 
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        while len(queue) > 0:
            children = len(queue)
            prev = None
            for _ in range(children):
                node = queue.pop(0)

                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            prev.next = None

        return root
