# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: all_nodes_with_k_distances.py
# @Date:   10/19/20, Mon
"""
863. All Nodes Distance K in Binary Tree
Medium


Share
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        parents = {}
        self.get_parents(root, None, parents)

        def bfs(start):
            ans = []
            queue = deque()
            queue.append((start, 0))
            visited = set()
            while len(queue):
                node, level = queue.popleft()
                visited.add(node.val)
                if level == K:
                    ans.append(node.val)
                else:
                    if node.left is not None and node.left.val not in visited:
                        queue.append((node.left, level + 1))
                    if node.right is not None and node.right.val not in visited:
                        queue.append((node.right, level + 1))
                    if parents[node.val] is not None and parents[node.val].val not in visited:
                        queue.append((parents[node.val], level + 1))
            return ans

        return bfs(target)

    def get_parents(self, cur, parent, parents):
        if cur is None:
            return
        parents[cur.val] = parent
        self.get_parents(cur.left, cur, parents)
        self.get_parents(cur.right, cur, parents)
