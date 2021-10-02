#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_max_value_of_equation.py
@Author   : Harsh Parikh
@Date     : 10/1/21 4:07 PM

1499. Max Value of Equation
Hard

625

25

Add to List

Share
You are given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

Return the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length.

It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.



Example 1:

Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
Output: 4
Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.
Example 2:

Input: points = [[0,0],[3,0],[9,2]], k = 3
Output: 3
Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
"""

import heapq
from typing import List

"""
Explanation
Because xi < xj,
yi + yj + |xi - xj| = (yi - xi) + (yj + xj)

So for each pair of (xj, yj),
we have xj + yj, and we only need to find out the maximum yi - xi.
To find out the maximum element in a sliding window,
we can use priority queue or stack.


Solution 1: Priority Queue
Time O(NlogN)
Space O(N)

"""

import collections


class Solution:
    # O(nlogn)
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:

        maxEq = float('-inf')

        heap = []
        for xj, yj in points:
            while heap and abs(xj - heap[0][1]) > k:
                heapq.heappop(heap)

            if heap:
                maxEq = max(maxEq, -heap[0][0] + xj + yj)

            heapq.heappush(heap, (-(yj - xj), xj))

        return maxEq

    # O(n^2)
    def findMaxValueOfEquation1(self, points: List[List[int]], k: int) -> int:
        ans = float('-inf')
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if abs(points[i][0] - points[j][0]) <= k:
                    ans = max(ans, points[i][1] - points[i][0] + points[j][0] + points[j][1])
                else:
                    break
        return ans

    # O(N) monotonic stack
    def findMaxValueOfEquation2(self, points: List[List[int]], k: int) -> int:
        stack = collections.deque()  # (x, y-x)
        ans = float('-inf')

        for xj, yj in points:
            while stack and abs(stack[0][0] - xj) > k:
                stack.popleft()

            if stack:
                ans = max(ans, xj + yj + stack[0][1])

            while stack and stack[-1][1] <= yj - xj:
                last_pair = stack.pop()  # (x, y-x)
                ans = max(ans, xj + yj + last_pair[1])

            stack.append((xj, yj - xj))

        return ans
