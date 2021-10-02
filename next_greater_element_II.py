#!/usr/bin/env python
# coding:utf-8
"""
@FileName : next_greater_element_II.py
@Author   : Harsh Parikh
@Date     : 10/1/21 11:33 PM

503. Next Greater Element II
Medium

3320

108

Add to List

Share
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.



Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
"""

'''
The idea here is to store the indexes of the elements that we haven't seen a greater than value for them yet
we do this because if you stored the values you wouldn't be able to easily know where a value is at so you
can set it accordingly. This comes in handy in the second loop.

The values in the stack when we enter the second loop will always be decending, this is an important part of knowing that 
we are setting the indexes to their correct value. Since we always will set the index's left in the stack to the smallest
number when reiterating over the stack, ensuring a correct answer. 
'''


class Solution(object):
    def nextGreaterElements(self, nums):
        stack = []
        result = [-1] * len(nums)

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                result[stack.pop()] = nums[i]

            stack.append(i)

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                result[stack.pop()] = nums[i]

        return result
