#!/usr/bin/env python
# coding:utf-8
"""
@FileName : find_common_elements_in_two_BSTs.py
@Author   : Harsh Parikh
@Date     : 9/11/21 2:11 PM
"""

from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def listCommonElements_iterative(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stk1 = []
        stk2 = []
        res = []
        while (root1 or stk1) and (root2 or stk2):
            while root1:
                stk1.append(root1)
                root1 = root1.left
            while root2:
                stk2.append(root2)
                root2 = root2.left
            if not stk1 or not stk2:
                break
            if stk1[-1].val < stk2[-1].val:
                root1 = stk1.pop()
                root1 = root1.right
            elif stk1[-1].val > stk2[-1].val:
                root2 = stk2.pop()
                root2 = root2.right
            elif stk1[-1].val == stk2[-1].val:
                res.append(stk1[-1].val)
                root2 = stk2.pop().right
                root1 = stk1.pop().right
        return res

    def listCommonElements_recursive(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def traverse(node1, node2):
            nonlocal common_elements

            if not node1 or not node2:
                return

            if node1.val == node2.val:
                common_elements.append(node1.val)
                traverse(node1.left, node2.left)
                traverse(node1.right, node2.right)

            elif node1.val < node2.val:
                traverse(node1, node2.left)
                traverse(node1.right, node2)
            elif node1.val > node2.val:
                traverse(node1.left, node2)
                traverse(node1, node2.right)

        common_elements = []
        traverse(root1, root2)
        return common_elements


if __name__ == "__main__":
    s = Solution()
    root1 = TreeNode(3)
    root1.left = TreeNode(2)
    root1.right = TreeNode(4)
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    print(s.listCommonElements_iterative(root1, root2))
    print(s.listCommonElements_recursive(root1, root2))
