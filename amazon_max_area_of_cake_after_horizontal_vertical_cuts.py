#!/usr/bin/env python
# coding:utf-8
"""
@FileName : amazon_max_area_of_cake_after_horizontal_vertical_cuts.py
@Author   : Harsh Parikh
@Date     : 8/7/21 12:52 PM

1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays 
horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.



Example 1:


Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4
Explanation: The figure above represents the given rectangular cake. 
Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
Example 2:


Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9
"""


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        """
        Algorithm

            Find heights of pieces if we only perform the horizontal cuts. Say this array is heights[].
            Find lengths of pieces if we only perform the vertical cuts. Say this arrays is lengths[].
            Find max of heights[] and lengths[].
            Multiply those two max and take mod 10e7.
            Return the answer

        https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/discuss/661995/Do-you-like-visual-explanation-You-got-it.-%3A-)-With-2-code-variations.
        """

        maxHeight = float('-inf')
        maxWidth = float('-inf')

        horizontalCuts.sort()
        verticalCuts.sort()

        for i in range(len(horizontalCuts)):
            if i == 0:
                maxHeight = horizontalCuts[i]
            else:
                maxHeight = max(maxHeight, horizontalCuts[i] - horizontalCuts[i - 1])

        maxHeight = max(maxHeight, h - horizontalCuts[-1])

        for i in range(len(verticalCuts)):
            if i == 0:
                maxWidth = verticalCuts[i]
            else:
                maxWidth = max(maxWidth, verticalCuts[i] - verticalCuts[i - 1])

        maxWidth = max(maxWidth, w - verticalCuts[-1])

        return maxHeight % (10 ** 9 + 7) * maxWidth % (10 ** 9 + 7)

