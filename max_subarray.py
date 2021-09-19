"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return -1
        currSum = nums[0]
        finalSum = nums[0]

        for i, num in enumerate(nums):
            if i == 0:
                continue
            # currSum = max(num + currSum, num)
            # finalSum = max(finalSum, currSum)
            if num + currSum < num:
                currSum = num
            else:
                currSum += num

            if currSum > finalSum:
                finalSum = currSum
        return finalSum


if __name__ == "__main__":
    # print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(Solution().maxSubArray([1, -3, 2, 1, -1]))
