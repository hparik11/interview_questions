# Definition for a binary search tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, minVal, maxVal):
            if root is None:
                return True

            if root.val <= minVal or root.val >= maxVal:
                return False

            return helper(root.left, minVal, root.val) and helper(root.right, root.val, maxVal)

        return helper(root, float('-inf'), float('inf'))
