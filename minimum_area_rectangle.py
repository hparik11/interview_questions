#!/usr/bin/env python
# coding:utf-8
"""
@FileName : minimum_area_rectangle.py
@Author   : Harsh Parikh
@Date     : 8/17/21 10:49 AM

939. Minimum Area Rectangle

You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.



Example 1:


Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:


Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
"""


class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        min_area = float('inf')
        points_hashset = set([tuple(point) for point in points])

        for x1, y1 in points:
            for x2, y2 in points:
                if x1 < x2 and y1 < y2:  # Skip looking at same point
                    if (x1, y2) in points_hashset and (x2, y1) in points_hashset:
                        min_area = min(min_area, abs(x1 - x2) * abs(y1 - y2))

        return 0 if min_area == float('inf') else min_area
