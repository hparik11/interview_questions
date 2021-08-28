#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_next_permutation.py
@Author   : Harsh Parikh
@Date     : 8/2/21 12:15 AM

31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.



Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        1243 5 7643
             k    j
             6 7543

        """
        i = j = len(nums) - 1

        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # After completion of the first loop, there will be two cases
        # 1. Our i becomes zero (This will happen if the given array is sorted decreasingly).
        # In this case, we'll simply reverse the sequence and will return

        if i == 0:  # nums are in descending order
            nums.reverse()
            return

        # 2. If it's not zero then we'll find the first number grater then nums[i-1] starting from end
        k = i - 1  # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1

        # Now our pointer is pointing at two different positions
        # i. first non-ascending number from end
        # j. first number greater than nums[i-1]

        # We'll swap these two numbers
        nums[k], nums[j] = nums[j], nums[k]

        # We'll reverse a sequence starting from i to end
        l, r = k + 1, len(nums) - 1  # reverse the second part

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.nextPermutation([1, 2, 3]))
    print(s.nextPermutation([3, 2, 1]))
