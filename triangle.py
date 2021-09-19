#!/usr/bin/env python
# coding:utf-8
"""
@FileName : triangle.py
@Author   : Harsh Parikh
@Date     : 6/13/21 3:45 PM
"""

"""
120. Triangle
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
    
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
"""

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        res = [0 for _ in range(len(triangle[-1]))]
        res[0] = triangle[0][0]
        last_row = res[:]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    res[j] = last_row[j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    res[j] = last_row[j - 1] + triangle[i][j]
                else:
                    res[j] = min(last_row[j - 1], last_row[j]) + triangle[i][j]

            last_row = res[:]

        return min(res)


if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
