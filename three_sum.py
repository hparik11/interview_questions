"""

15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) >= 3:
            nums.sort()
            l = len(nums)
            finalList = set()
            for i in range(l - 2):
                left = i + 1
                right = l - 1
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                while left < right:
                    leftNum, num, rightNum = nums[left], nums[i], nums[right]
                    sum = leftNum + num + rightNum

                    if sum > 0:
                        right -= 1
                    elif sum < 0:
                        left += 1
                    else:
                        finalList.add(tuple([num, leftNum, rightNum]))
                        left, right = left + 1, right - 1

            return [list(i) for i in finalList]


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([0, 0, 0]))
    print(s.threeSum([-2, 0, 0, 2, 2]))
