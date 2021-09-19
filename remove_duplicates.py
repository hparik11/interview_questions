"""
80. Remove Duplicates from Sorted Array II

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if len(nums) < 2:
            return length
        i = 1

        dup_cnt = 0
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                dup_cnt += 1
                if dup_cnt > 1:
                    length -= 1
                    del nums[i]
                    i -= 1
            else:
                dup_cnt = 0
            i += 1

        return length


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
    print(s.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
