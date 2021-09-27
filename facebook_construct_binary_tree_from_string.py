#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_construct_binary_tree_from_string.py
@Author   : Harsh Parikh
@Date     : 7/17/21 9:03 PM

536. Construct Binary Tree from String

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis.
The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.


Example 1:


Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]
Example 2:

Input: s = "4(2(3)(1))(6(5)(7))"
Output: [4,2,6,3,1,5,7]
Example 3:

Input: s = "-4(2(3)(1))(6(5)(7))"
Output: [-4,2,6,3,1,5,7]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:

        """
        Every time an opening brace is seen
        If a number is present in num, Create a TreeNode and append it to the stack.
        Every time a closing brace is seen, If a number is present in num, Create a TreeNode, check if the parent at the top of the stack has a left child, if true, attach the node to the parent's left child, if false, attach the node to the parent's right child

        If a number is not present in num, it means that the node at the top of the stack has already been assigned its children
        Pop the node from the stack
        Check if the current topmost element of stack has a left child
        if true, attach the node to the left
        if false, attch the node to the right

        return top most element of the stack

        Time Complexity: O(n) where n is the length of the string
        Space Complexity: O(N) where N is the number of Nodes in the Tree (or the number of integers in the string)

        """
        num = ''
        stack = []
        for i in s:
            if i.isdigit() or i == '-':
                num += i
            elif i == '(':
                if num:
                    node = TreeNode(num)
                    num = ''
                    stack.append(node)
            else:
                if num:
                    node = TreeNode(num)
                    num = ''
                else:
                    node = stack.pop()

                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

        return stack[-1] if stack else TreeNode(num) if s else None

    def str2tree(self, s: str) -> TreeNode:
        if not s:
            return None
        stack, number = [], ''
        for c in s:
            if c in '()':
                if c == '(' and number:
                    stack.append(TreeNode(number))
                    number = ''
                elif c == ')':
                    if number:
                        node, parent = TreeNode(number), stack[-1]
                        number = ''
                    else:
                        node, parent = stack.pop(), stack[-1]
                    if parent.left:
                        parent.right = node
                    else:
                        parent.left = node
            else:
                number += c
        if number:
            stack = [TreeNode(number)]
        return stack[0]