#!/usr/bin/env python
# coding:utf-8
"""
@FileName : amazon_k_closest_point_from_origin.py
@Author   : Harsh Parikh
@Date     : 7/20/21 5:39 PM

973. K Closest Points to Origin

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).


Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
"""

import heapq
import math
from typing import List


class Solution:
    @staticmethod
    def euclidean_distance(x, y):
        return math.sqrt(x ** 2 + y ** 2)

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        
        for each in points:
            if len(heap) == K:
                heapq.heappushpop(heap, (-1.0 * self.euclidean_distance(each[0], each[1]), each[0], each[1]))
            else:
                heapq.heappush(heap, (-1.0 * self.euclidean_distance(each[0], each[1]), each[0], each[1]))

            print(list(heap))
        return [(x,y) for (dist,x, y) in heap]

        # if K >= len(points):
        #     return points

        # return sorted(points, key=lambda i: self.euclidean_distance(i[0], i[1]))[:K]


if __name__ == '__main__':
    s = Solution()
    print(s.kClosest([[1,3],[-2,2]], 1))