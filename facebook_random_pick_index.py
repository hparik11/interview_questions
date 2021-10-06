#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_random_pick_index.py
@Author   : Harsh Parikh
@Date     : 9/17/21 1:04 AM

398. Random Pick Index

Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.


Example 1:

Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]

Explanation
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
"""

import random


class Solution:

    def __init__(self, nums: List[int]):
        # self.d = defaultdict(list)
        # for i, n in enumerate(nums):
        #     self.d[n] += i,

        self.nums = nums

    def pick(self, target: int) -> int:
        # return random.choice(self.d[target])

        k, res = 1, None

        for i, n in enumerate(self.nums):
            if n == target:
                if random.random() < 1 / k:
                    res = i

                k += 1

        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
