"""
654. Maximum Binary Tree
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1

"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) > 0:
            maxNum = max(nums)
            rootIndex = nums.index(maxNum)
            root = TreeNode(maxNum)
            root.left = self.constructMaximumBinaryTree(nums[:rootIndex])
            root.right = self.constructMaximumBinaryTree(nums[rootIndex + 1:])
            return root
        else:
            return


if __name__ == "__main__":
    print(Solution().constructMaximumBinaryTree([2, 3, 1, 6, 0, 5]).left.right.val)
