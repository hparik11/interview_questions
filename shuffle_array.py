#!/usr/bin/env python
# coding:utf-8
"""
@FileName : shuffle_array.py
@Author   : Harsh Parikh
@Date     : 9/13/21 5:18 PM

384. Shuffle an Array

Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.


Example 1:

Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                       // Any permutation of [1,2,3] must be equally likely to be returned.
                       // Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

"""


class Solution:

    def __init__(self, nums):
        self.array = nums
        self.original = nums[:]

    def reset(self):
        self.array = self.original[:]
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randint(i, len(self.array) - 1)
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array
