#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_largest_rectangle_in_histogram.py
@Author   : Harsh Parikh
@Date     : 10/5/21 12:14 PM

84. Largest Rectangle in Histogram
Hard

7294

118

Add to List

Share
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.



Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #         maxArea = 0

        #         for idx, currentBuilding in enumerate(heights):

        #             leftMostIdx = idx
        #             # Left traverse
        #             while leftMostIdx > 0 and heights[leftMostIdx - 1] >= currentBuilding:
        #                 leftMostIdx -= 1

        #             rightMostIdx = idx
        #             # Right traverse
        #             while rightMostIdx < len(heights) - 1 and heights[rightMostIdx + 1] >= currentBuilding:
        #                 rightMostIdx += 1

        #             maxArea = max(maxArea, currentBuilding * (rightMostIdx - leftMostIdx + 1))

        #         return maxArea

        stack = []
        max_area = heights[0]
        for i in range(len(heights)):
            print(heights[i], stack, max_area)
            while stack and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                if stack:
                    current_width = i - stack[-1] - 1
                else:
                    current_width = i
                max_area = max(max_area, current_height * current_width)

            stack.append(i)

        print(stack)
        while stack:
            current_height = heights[stack.pop()]
            if stack:
                current_width = len(heights) - stack[-1] - 1
            else:
                current_width = len(heights)
            max_area = max(max_area, current_height * current_width)

        return max_area
