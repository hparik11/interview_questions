#!/usr/bin/env python
# coding:utf-8
"""
@FileName : microsoft_partial_K_equal_subsets.py
@Author   : Harsh Parikh
@Date     : 7/30/21 7:44 PM

698. Partition to K Equal Sum Subsets

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false
"""


class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:

        # trivial case one subset
        if k == 1:
            return True
        # trivial case, k must be k<=n
        n = len(nums)

        if k > n:
            return False

        total = sum(nums)

        if total % k:
            return False

        target = total // k
        seen = [0] * n

        nums.sort(reverse=True)

        def dfs(k, index, current_sum):
            # trivial, one group
            if k == 1:
                return True

            # found one group, need more k-1 groups
            if current_sum == target:
                return dfs(k - 1, 0, 0)

            # group can start with any number
            for i in range(index, n):
                # if we have not tried it before, and adding it
                # to current sum does not exceed target then
                if not seen[i] and current_sum + nums[i] <= target:
                    # we have seen it
                    seen[i] = 1
                    # recursively build group from i+1
                    if dfs(k, i + 1, current_sum + nums[i]):
                        return True

                    seen[i] = 0

            return False

        return dfs(k, 0, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
