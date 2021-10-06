#!/usr/bin/env python
# coding:utf-8
"""
@FileName : split_array_largest_sum.py
@Author   : Harsh Parikh
@Date     : 8/31/21 11:34 PM

410. Split Array Largest Sum

Given an array nums which consists of non-negative integers and an integer m,
 you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.



Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9
Example 3:

Input: nums = [1,4,4], m = 3
Output: 4
"""

"""
Time complexity: O(n^m)
Space complexity: O(n). The  helper function adds a frame to the run-time stack for every element in the list, of which there are n.
"""


# BruteForce
class Solution(object):
    def helper(self, nums, m):
        if not nums:
            return 0
        elif m == 1:
            return sum(nums)
        else:
            min_result = float('inf')
            for j in range(1, len(nums) + 1):
                left, right = sum(nums[:j]), self.helper(nums[j:], m - 1)
                min_result = min(min_result, max(left, right))
            return min_result

    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        return self.helper(nums, m)


# Memoization (DP)
"""
Complexity Analysis

Time complexity: O(n^2 * m) The total number of states is O(n * m). 
To compute each state f[i][j], we need to go through the whole array to find the optimum k. 
This requires another O(n) loop. So the total time complexity is O(n ^ 2 * m)

Space complexity: O(n * m). The space complexity is equivalent to the number of states, which is O(n * m).
"""


class Solution2:
    def helper(self, idx, nums, m, cache):

        if idx == len(nums) or m == 0:
            return 0

        elif m == 1:
            return sum(nums[idx:])

        elif (idx, m) in cache:
            return cache[(idx, m)]
        else:
            min_result = float('inf')
            for j in range(1, len(nums) + 1):
                left, right = sum(nums[idx:idx + j]), self.helper(idx + j, nums, m - 1, cache)
                min_result = min(min_result, max(left, right))

            cache[(idx, m)] = min_result

            return cache[(idx, m)]

    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        cache = {}
        return self.helper(0, nums, m, cache)


# Complexity Analysis
#
# Time complexity: O(n * log(sum of array)). The binary search costs
# O(log(sum of array)), where sum of array is the sum of elements in nums.
# For each computation of F(x), the time complexity is O(n) since we only need
# to go through the whole array.
#
# Space complexity: O(1) space complexity without taking the output list into
# account, and O(n) to store the output list.
class Solution3:
    def splitArray(self, nums: List[int], m: int) -> int:
        # First, understand WHAT we are binary searching over
        # we are doing a binary search over the *search space of possible results*
        # What is the search space, aka what are all possible results?
        # For this, we need to know the minimum and maximum possible result
        #### minimum possible result - largest element in array. Since each element needs
        # to be part of some subarray, the smallest we can go is by taking the largest element
        # in a subarray by itself
        #### maximum possible result - sum of all elements in the array since we cannot form
        # a subarray larger than the array itself
        # Compute minResult and maxResult boundaries
        minResult, maxResult = max(nums), sum(nums)

        # now that we have our minResult and maxResult boundaries, we can begin searching within this space
        # What are we searching for?
        # The smallest value within this space such that we can form m subarrays from
        # nums and none of their sums exceed that value
        finalResult = float('inf')
        while minResult <= maxResult:
            # Start by checking if the value in the middle of the search space satisfies this desired outcome
            # If it does, we can discard all values to the right of this in our search space since we have
            # something better than those already. We only need to search values to the left to see if
            # we can find something better
            # If not, we only need to search values higher than mid
            mid = (minResult + maxResult) // 2
            if self.isPossibility(mid, nums, m):
                finalResult = mid
                # Once we find the solution, try to minimize it. That's why we are moving to left side
                maxResult = mid - 1
            else:
                # Here we will go right side to meet the requirement of m. so we could only divide in m times.
                minResult = mid + 1

        return finalResult

    # Checks to see if x is a valid possibility given the constraint of m subarrays
    def isPossibility(self, mid, nums, m):
        numSubarrays = 1
        subarraySum = 0

        for num in nums:
            # Greedily try to add this element to the current subarray
            # as long as the subarray's sum doesn't exceed our upper limit mid value
            if (num + subarraySum) <= mid:
                subarraySum += num
            # If sum would be exceeded by adding the current element,
            # we need to start a new subarray and put this element into that
            else:
                numSubarrays += 1
                subarraySum = num

        return numSubarrays <= m
