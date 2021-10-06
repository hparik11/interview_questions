#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_maximal_rectangle_in_2D.py
@Author   : Harsh Parikh
@Date     : 10/5/21 12:47 PM

85. Maximal Rectangle
Hard

5175

94

Add to List

Share
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.



Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = []
Output: 0
Example 3:

Input: matrix = [["0"]]
Output: 0
Example 4:

Input: matrix = [["1"]]
Output: 1
Example 5:

Input: matrix = [["0","0"]]
Output: 0

"""


class Solution:

    # Get the maximum area in a histogram given its heights
    def leetcode84(self, heights):
        stack = []
        max_area = heights[0]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                if stack:
                    current_width = i - stack[-1] - 1
                else:
                    current_width = i
                max_area = max(max_area, current_height * current_width)

            stack.append(i)

        while stack:
            current_height = heights[stack.pop()]
            if stack:
                current_width = len(heights) - stack[-1] - 1
            else:
                current_width = len(heights)
            max_area = max(max_area, current_height * current_width)

        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        maxarea = 0
        dp = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # update the state of this row's histogram using the last row's histogram
                # by keeping track of the number of consecutive ones
                print(i, dp)
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0

            # update maxarea with the maximum area from this row's histogram
            maxarea = max(maxarea, self.leetcode84(dp))

        return maxarea
