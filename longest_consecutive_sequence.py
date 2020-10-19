# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: longest_consecutive_sequence.py
# @Date:   10/17/20, Sat
"""
128. Longest Consecutive Sequence
Hard

4089

203

Add to List

Share
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
from typing import  List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dictn = {}
        for num in nums:
            dictn[num] = True

        maxLength = 0
        i = 0

        while i < len(nums):
            currNum = nums[i]

            if dictn[currNum]:
                dictn[currNum] = False
                currLength = 1
                nextNum = currNum + 1
                while nextNum in dictn:
                    dictn[nextNum] = False
                    currLength += 1
                    nextNum += 1

                beforeNum = currNum - 1
                while beforeNum in dictn:
                    dictn[beforeNum] = False
                    currLength += 1
                    beforeNum -= 1

                if currLength > maxLength:
                    maxLength = currLength

            i += 1
        return maxLength

    def longestConsecutive1(self, nums: List[int]) -> int:
        nums = set(nums)

        maxLength = 0
        i = 0

        while nums:
            currNum = nums.pop()

            currLength = 1
            nextNum = currNum + 1
            while nextNum in nums:
                nums.remove(nextNum)
                currLength += 1
                nextNum += 1

            beforeNum = currNum - 1
            while beforeNum in nums:
                nums.remove(beforeNum)
                currLength += 1
                beforeNum -= 1

            if currLength > maxLength:
                maxLength = currLength

            i += 1
        return maxLength


if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))