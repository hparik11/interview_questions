"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        li = 0
        ri = len(nums) - 1
        pivot = 1
        index = 0

        while index <= ri:
            num = nums[index]
            if num < pivot:
                nums[index], nums[li] = nums[li], nums[index]
                li += 1
                index += 1
            elif num > pivot:
                nums[index], nums[ri] = nums[ri], nums[index]
                ri -= 1
            else:
                index += 1

        return nums


if __name__ == '__main__':
    s = Solution()
    # print(s.sortColors([2,0,2,1,1,0]))
    print(s.sortColors([0, 1, 2, 0, 2, 1, 1]))
