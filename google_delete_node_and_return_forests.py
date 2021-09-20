"""
1110. Delete Nodes And Return Forest
Medium

2193

62

Add to List

Share
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.



Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root, to_delete):

        """
        Bottom up recursion
        Idea: When we delete a node it's children form two trees.

        Algorithm: If current node is to be deleted then add it's children after checking if they are not null.
        Spcially handle if root is to be deleted.

        """

        ans = []
        to_delete = set(to_delete)

        def helper(node):
            if not node:
                return None
            node.left = helper(node.left)
            node.right = helper(node.right)

            # add children of a node that is to be deleted
            if node.val in to_delete:
                if node.left:
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)

                return None

            return node

        helper(root)
        # if root is not to be deleted then add it
        if root.val not in to_delete:
            ans.append(root)

        return ans
