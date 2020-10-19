"""
Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currIndex = 0
        lastIndex = len(nums) - 1
        maxJump = 0
        while True:
            if maxJump >= lastIndex:
                return True
            elif nums[currIndex] == 0 and maxJump <= currIndex:
                return False

            if (currIndex + nums[currIndex]) > maxJump:
                maxJump = currIndex + nums[currIndex]

            currIndex += 1


if __name__ == "__main__":
    # print(Solution().canJump([3,0,8,2,0,0,1]))
    print(Solution().canJump([7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]))
