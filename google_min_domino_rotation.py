#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_min_domino_rotation.py
@Author   : Harsh Parikh
@Date     : 10/5/21 10:00 PM

1007. Minimum Domino Rotations For Equal Row
Medium

1429

198

Add to List

Share
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.



Example 1:


Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.
"""


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # A solution exists for a number k when the total amount of k at different indexes
        # in both tops and bottoms are bigger or equal to length of tops / bottoms.
        # In such case, just switch all dominos at whichever row has smaller amount of k

        # Therefore, we maintain a counter for both tops and bottoms, also a counter
        # when same number appear at same index, to avoid double counting for same indexes

        topsCount = {k: 0 for k in range(0, 7)}
        bottomsCount = {k: 0 for k in range(0, 7)}
        sameCount = {k: 0 for k in range(0, 7)}

        length = len(tops)

        # Initiate the counters
        for i in range(length):
            if tops[i] == bottoms[i]:
                sameCount[tops[i]] += 1

            topsCount[tops[i]] += 1
            bottomsCount[bottoms[i]] += 1

        ans = float('inf')

        # Go through all potential solutions and update global minima
        # Note that we need to minus sameCount to avoid double counting those at the same indexes
        for i in range(0, 7):
            if topsCount[i] + bottomsCount[i] - sameCount[i] >= length:
                ans = min(ans, length - max(topsCount[i], bottomsCount[i]))

        if ans == float('inf'):
            return -1

        return ans
