#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_ropes_and_bricks.py
@Author   : Harsh Parikh
@Date     : 8/25/21 10:57 AM

Given a zero-inexed array H of height of buildings, number of bricks b and number of ropes r. You start your journey from buiding 0 and move to adjacent building either using rope or bricks. You have limited number of bricks and ropes.
While moving from ith building to (i+1)th building,

if next building's height is less than or equal to the current buiding's height, you do not need rope or bricks.
if next building's height is greater than current buiding's height, you can either use one rope or (h[i+1] - h[i]) bricks.
So, question is How far can you reach from 0th buiding if you use bricks and ropes optimally? return index of building till which you can move.

Example 1:

Input : H = [4,2,7,6,9,11,14,12,8], b = 5, r = 2
Output: 8
Explanation: use rope to move from index 1 to index 2.
use 3 bricks to move from index 3 to index 4.
use 2 bricks to move from index 4 to index 5.
use rope to move from index 5 to index 6.
so we can reach at the end of the array using 2 ropes and 5 bricks.
Example 2:

Input : H = [4,2,7,6,9,11,14,12,8], b = 5, r = 1
Output: 5
Explanation: use rope to move from index 1 to index 2.
use 3 bricks to move from index 3 to index 4.
use 2 bricks to move from index 4 to index 5.
so we can reach at index 5 using 1 ropes and 5 bricks.
"""


class Solution:
    def jump_bricks_dfs(self, heights, bricks, ropes):

        def solve(idx: int, bricks: int, ropes: int) -> int:
            if idx == len(heights) - 1 or (ropes == 0 and bricks < heights[idx + 1] - heights[idx]):
                return idx
            if idx in dp:
                return dp[idx]

            DIFF = heights[idx + 1] - heights[idx]
            # next house is smaller; move forward at no cost
            if DIFF <= 0:
                return solve(idx + 1, bricks, ropes)
            else:
                r_res = solve(idx + 1, bricks, ropes - 1) if ropes > 0 else float("-inf")
                b_res = solve(idx + 1, bricks - DIFF, ropes) if bricks >= DIFF else float("-inf")

                dp[idx] = max(r_res, b_res)

                return dp[idx]

        dp = {}
        return solve(0, bricks, ropes)

    @staticmethod
    def jump_bricks_bfs(heights, b, r):
        initial = (0, b, r)
        q = collections.deque()
        q.append(initial)
        curr = 0

        while q:
            curr, bricks, ropes = q.popleft()
            if curr >= len(heights) - 1:
                return curr
            diff = heights[curr + 1] - heights[curr]
            if diff <= 0:
                q.append((curr + 1, bricks, ropes))
            else:
                if bricks >= diff:
                    q.append((curr + 1, bricks - diff, ropes))
                if ropes > 0:
                    q.append((curr + 1, bricks, ropes - 1))

        return curr


if __name__ == '__main__':
    s = Solution()
    print(s.jump_bricks_dfs([4, 2, 7, 6, 9, 11, 14, 12, 8], 5, 2))
    print(s.jump_bricks_dfs([4, 2, 7, 6, 9, 11, 14, 12, 8], 5, 1))
