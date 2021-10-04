"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

"""
from typing import List


class Solution:
    @staticmethod
    def jump(nums: List[int]) -> int:
        currIndex = 0
        lastIndex = len(nums) - 1
        prevMaxJump = 0
        maxJump = 0
        jumpCnt = 0

        while currIndex < lastIndex:
            if nums[currIndex] == 0 and maxJump <= currIndex:
                return jumpCnt

            if (currIndex + nums[currIndex]) > maxJump:
                maxJump = currIndex + nums[currIndex]

            if maxJump >= lastIndex:
                # Increase number of jumps when it reaches to final hop
                jumpCnt += 1
                return jumpCnt

            # Increase number of jumps only when it reaches to maxJump value
            if currIndex == prevMaxJump:
                # print(jumpCnt)
                jumpCnt += 1
                prevMaxJump = maxJump
            # print(currIndex, maxJump, jumpCnt)
            currIndex += 1

        return jumpCnt


if __name__ == "__main__":
    print(Solution().jump([7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]))
