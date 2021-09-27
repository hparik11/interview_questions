#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_convert_BST_to_DLL.py
@Author   : Harsh Parikh
@Date     : 7/22/21 12:50 AM

426. Convert Binary Search Tree to Sorted Doubly Linked List

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor
and successor pointers in a doubly-linked list. For a circular doubly linked list,
the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation,
the left pointer of the tree node should point to its predecessor,
and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.



Example 1:



Input: root = [4,2,5,1,3]


Output: [1,2,3,4,5]

Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

Example 2:

Input: root = [2,1,3]
Output: [1,2,3]
Example 3:

Input: root = []
Output: []
Explanation: Input is an empty tree. Output is also an empty Linked List.
Example 4:

Input: root = [1]
Output: [1]

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class DoubleLinkedListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = DoubleLinkedListNode()
        self.tail = DoubleLinkedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        prevNode = self.tail.prev
        prevNode.next = node
        self.tail.prev = node

        node.next = self.tail
        node.prev = prevNode

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = node.next
        nextNode.prev = node.prev


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        if not root:
            return root

        first = None
        last = None

        stack = [root]
        curr = root.left

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
                continue

            # print(stack)
            if stack:
                curr = stack.pop()

                if not first:
                    first = curr

                if last:
                    last.right = curr
                    curr.left = last

                last = curr

                curr = curr.right

        first.left = last
        last.right = first

        return first
