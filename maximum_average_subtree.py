#!/usr/bin/env python
# coding:utf-8
"""
@FileName : maximum_average_subtree.py
@Author   : Harsh Parikh
@Date     : 8/2/21 11:27 PM

1120. Maximum Average Subtree

Given the root of a binary tree, find the maximum average value of any subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)

Example 1:

Input: [5,6,1]
Output: 6.00000
Explanation:
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_avg = float("-inf")

    def maximumAverageSubtree(self, root: TreeNode) -> float:
        if not root:
            return 0

        def dfs(node=root):

            # if node is None, return 0 as sum and 0 as no. of nodes
            if node is None:
                return 0, 0

            # go to left subtree and get total sum on that subtree, and the total nodes
            sum_left, node_cnt_left = dfs(node.left)

            # go to right subtree and get total sum on that subtree, and the total nodes
            sum_right, node_cnt_right = dfs(node.right)

            # calculate the total sum
            _total_sum = node.val + sum_left + sum_right
            # calculate the total no. of nodes
            _total_nodes = 1 + node_cnt_left + node_cnt_right
            # compute the avg
            _avg = _total_sum / _total_nodes

            # update max_avg if it is smaller than computed avg
            if _avg > self.max_avg:
                self.max_avg = _avg

            # return the total sum and total nodes to previous stack call.
            return _total_sum, _total_nodes

        # set a variable to track max_avg
        dfs(root)

        return self.max_avg
