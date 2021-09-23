#!/usr/bin/env python
# coding:utf-8
"""
@FileName : jump_game_VI.py
@Author   : Harsh Parikh
@Date     : 8/21/21 10:40 AM

1696. Jump Game VI

You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going
outside the boundaries of the array. That is, you can jump from index i to any index in the
range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.



Example 1:

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
Example 2:

Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
Example 3:

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0
"""

from typing import List
import heapq


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        score = nums[0]
        priority_queue = []
        # since heapq is a min-heap,
        # we use negative of the numbers to mimic a max-heap
        heapq.heappush(priority_queue, (-nums[0], 0))

        for i in range(1, n):
            # pop the old index

            # If the index of top of priority_queue is less than i-k, pop the top. Repeat.
            while priority_queue[0][1] < i - k:
                heapq.heappop(priority_queue)

            score = nums[i] - priority_queue[0][0]

            heapq.heappush(priority_queue, (-score, i))

        return score


if __name__ == '__main__':
    s = Solution()
    print(s.maxResult([1, -5, -20, 4, -1, 3, -6, -3], 2))
