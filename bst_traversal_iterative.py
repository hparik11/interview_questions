# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: bst_traversal_iterative.py
# @Date:   8/15/20, Sat

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

    def inorderTraversal1(self, root):
        stack = [(False, root)]
        res = []

        while stack:
            flag, val = stack.pop()
            if val:
                if not flag:
                    stack.append((False, val.right))
                    stack.append((True, val))
                    stack.append((False, val.left))
                else:
                    res.append(val.val)
        return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        from collections import deque
        res = []
        d = deque([root])
        while d:
            cur = d.popleft()
            if cur:
                res.append(cur.val)
                d.appendleft(cur.right)
                d.appendleft(cur.left)
        return res

    def postorderTraversal(self, root):
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]
