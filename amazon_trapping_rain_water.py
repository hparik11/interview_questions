# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: amazon_trapping_rain_water.py
# @Date:   10/10/20, Sat
"""
42. Trapping Rain Water
Hard

8418

130

Add to List

Share
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        leftMaxArray = [0 for _ in range(len(height))]
        rightMaxArray = [0 for _ in range(len(height))]

        for i in range(1, len(height)):
            leftMaxArray[i] = max(leftMaxArray[i - 1], height[i - 1])

        for i in range(len(height) - 2, -1, -1):
            rightMaxArray[i] = max(rightMaxArray[i + 1], height[i + 1])

        i = 0
        total_water = 0
        while i < len(height):
            currHeight = height[i]
            minHeight = min(leftMaxArray[i], rightMaxArray[i])

            if currHeight < minHeight:
                total_water += minHeight - currHeight

            i += 1

        return total_water


if __name__ == '__main__':
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
