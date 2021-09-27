#!/usr/bin/env python
# coding:utf-8
"""
@FileName : amazon_consecutive_numbers_sum.py
@Author   : Harsh Parikh
@Date     : 9/4/21 7:25 PM

829. Consecutive Numbers Sum

Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.



Example 1:

Input: n = 5
Output: 2
Explanation: 5 = 2 + 3
Example 2:

Input: n = 9
Output: 3
Explanation: 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: n = 15
Output: 4
Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

"""


class Solution:

    # O(n^2)
    def consecutiveNumbersSum(self, n: int) -> int:

        nums = list(range(1, n // 2 + 2))

        ways = 1

        for i in range(len(nums) - 1):
            runningSum = nums[i]
            j = i + 1
            while j < len(nums):
                runningSum += nums[j]
                if runningSum == n:
                    ways += 1
                    break

                if runningSum > n:
                    break

                j += 1

        return ways

    # Time O(n)
    def consecutiveNumbersSum1(self, n: int) -> int:

        if n == 1:
            return 1

        # Initialize sum to 0
        _sum = 0

        # Start window at 1
        start = 1

        # Initialize count to 0
        count = 1

        # Iterate over the range 1 to N and calculate the running sum
        for i in range(1, math.ceil(n / 2) + 1):
            _sum += i
            # If the sum exceeds K, shrink the window
            while _sum > n:
                _sum -= start
                start += 1

            # If the sum equals N, add one to the count
            if _sum == n:
                count += 1
        return count
