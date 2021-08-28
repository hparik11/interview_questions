#!/usr/bin/env python
# coding:utf-8
"""
@FileName : serialize_deserialize_BT.py
@Author   : Harsh Parikh
@Date     : 8/28/21 12:14 PM

297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.



Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,2]
Output: [1,2]

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        nodes = [str(root.val)]

        queue = deque([root])
        while queue:
            node = queue.popleft()

            if node.left:
                nodes.append(str(node.left.val))
                queue.append(node.left)
            else:
                nodes.append("None")

            if node.right:
                nodes.append(str(node.right.val))
                queue.append(node.right)
            else:
                nodes.append("None")

        # print(nodes)
        return ",".join(nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        data = data.split(",")
        root_node = TreeNode(data[0])
        queue = deque([root_node])

        cur_pos = 1

        while len(queue) > 0:
            cur = queue.popleft()

            if data[cur_pos] != "None":
                cur.left = TreeNode(data[cur_pos])
                queue.append(cur.left)

            cur_pos += 1

            if data[cur_pos] != "None":
                cur.right = TreeNode(data[cur_pos])
                queue.append(cur.right)

            cur_pos += 1

        return root_node

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))