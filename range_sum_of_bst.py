"""
938. Range Sum of BST

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    total = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        def traverse(node):
            if not node:
                return

            if L <= node.val <= R:
                self.total += node.val

            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(root)

        return self.total


if __name__ == "__main__":
    print(Solution().rangeSumBST())
