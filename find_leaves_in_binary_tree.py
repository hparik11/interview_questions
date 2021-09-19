#!/usr/bin/env python
# coding:utf-8
"""
@FileName : find_leaves_in_binary_tree.py
@Author   : Harsh Parikh
@Date     : 7/5/21 3:54 PM

Find Leaves of Binary Tree
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.


Example 1:


Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
Example 2:

Input: root = [1]
Output: [[1]]
"""

"""
Time: O(N) - N because every time I traverse I remove the leaves so roughly the number of nodes in the tree reduce by two because in any Binary Tree, Half of the nodes are leaves.
So, the time complexit will be N+N/2+N/4+....+1 = 2N-1 (Proof: Link)
Not sure about time complexity but this is the best I could come up with. If anybody has a way to correct this or explain this then you're welcome.

Space: O(N) - using list to store the N nodes that are in the Binary Tree and then appending them to final list that is going to be returned.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def findLeafNodes(tree, leaves):
            if not tree:
                return

            if tree.left is None and tree.right is None:
                leaves.append(tree.val)
                return

            tree.left = findLeafNodes(tree.left, leaves)
            tree.right = findLeafNodes(tree.right, leaves)

            return tree

        final_ans = []
        while root:
            leaves = []
            root = findLeafNodes(root, leaves)
            final_ans.append(list(leaves))

        return final_ans

