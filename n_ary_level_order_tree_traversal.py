# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: n_ary_level_order_tree_traversal.py
# @Date:   9/7/20, Mon

"""
N-ary Tree Level Order Traversal

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).


Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
Example 2:


Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        count = 1
        queue = deque([root])

        level = 0
        res = [[root.val]]
        while len(queue) > 0:

            count -= 1
            node = queue.popleft()

            for each in node.children:
                queue.append(each)

            if count == 0:
                count = len(queue)
                if count > 0:
                    res.append([each.val for each in queue])
                level += 1

        return res
