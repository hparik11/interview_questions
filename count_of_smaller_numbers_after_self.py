#!/usr/bin/env python
# coding:utf-8
"""
@FileName : count_of_smaller_numbers_after_self.py
@Author   : Harsh Parikh
@Date     : 7/13/21 2:18 AM

315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].



Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]
"""

from typing import List
import bisect


class SpecialBST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.leftSubTrees = 0

    def insert(self, value, idx, rightSmallerCounts, numSmallerAtInsertTime=0):
        if value < self.value:
            self.leftSubTrees += 1

            if self.left is None:
                rightSmallerCounts[idx] = numSmallerAtInsertTime
                self.left = SpecialBST(value)
            else:
                self.left.insert(value, idx, rightSmallerCounts, numSmallerAtInsertTime)

        else:
            numSmallerAtInsertTime += self.leftSubTrees

            if value > self.value:
                numSmallerAtInsertTime += 1

            if self.right is None:
                rightSmallerCounts[idx] = numSmallerAtInsertTime
                self.right = SpecialBST(value)
            else:
                self.right.insert(value, idx, rightSmallerCounts, numSmallerAtInsertTime)


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        if len(nums) == 1:
            return [0]
        rightSmallerCounts = [0 for _ in range(len(nums))]

        tree = SpecialBST(nums[-1])
        for idx in range(len(nums) - 2, -1, -1):
            tree.insert(nums[idx], idx, rightSmallerCounts, 0)

        return rightSmallerCounts

    def countSmaller1(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        if len(nums) == 1:
            return [0]

        rightSmallerCounts = []
        sorted_arr = []
        for idx in range(len(nums) - 1, -1, -1):
            positionAfterSorting = bisect.bisect_left(sorted_arr, nums[idx])
            rightSmallerCounts.append(positionAfterSorting)
            sorted_arr.insert(positionAfterSorting, nums[idx])

        return rightSmallerCounts[::-1]


if __name__ == '__main__':
    s = Solution()

    print(s.countSmaller([5, 2, 6, 1]))
    print(s.countSmaller1([5, 2, 6, 1]))

"""
class SpecialBST:
    
    def __init__(self, val, left = None, right = None):
        
        self.val = val
        self.left = left
        self.right = right
        self.leftSubTreeSize = 0

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []
        
        res = []
        
        def bstInsert(node, val, numSmallerElements):
            
            if not node:
                res.append(numSmallerElements)
                return SpecialBST(val)
            
            else:
                
                if val > node.val:
                    node.right = bstInsert(node.right, val, numSmallerElements + 1 + node.leftSubTreeSize)
                    
                elif val == node.val:
                    node.right = bstInsert(node.right, val, numSmallerElements + node.leftSubTreeSize)
                    
                else:
                    
                    node.leftSubTreeSize += 1
                    node.left = bstInsert(node.left, val, numSmallerElements)
                    
                return node
            
        res = [0]
        
        root = SpecialBST(nums[-1])
        
        for i in range(len(nums) - 2, -1, -1):
            bstInsert(root, nums[i], 0)
        return res[::-1]
"""
