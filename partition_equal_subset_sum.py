#!/usr/bin/env python
# coding:utf-8
"""
@FileName : partition_equal_subset_sum.py
@Author   : Harsh Parikh
@Date     : 9/6/21 1:46 PM

416. Partition Equal Subset Sum

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Solution:
    def canPartition_dfs(self, nums: List[int]) -> bool:

        cache = {}

        # given idx, consider nums[idx:] returns true if
        # there are subset in nums[idx:] that adds up to left_sum
        def dfs(idx, left_sum):
            key = (idx, left_sum)
            if key in cache:
                return cache[key]

            if left_sum == 0:
                result = True

            elif left_sum < 0:
                result = False

            elif idx >= len(nums):
                result = False

            else:
                val = nums[idx]
                # either include val or not
                result = dfs(idx + 1, left_sum - val) or dfs(idx + 1, left_sum)

            cache[key] = result

            return result

        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False

        target = total_sum // 2

        return dfs(0, target)

    def canPartition_dp(self, nums: List[int]) -> bool:
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)

        # construct a dp table of size (n+1) x (subset_sum + 1)
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            curr = nums[i - 1]
            """
            dp[i][j] is true it satisfies one of the following conditions :
        
            Case 1) sum j can be formed without including ith element,
                if dp[i−1][j]==true
        
            Case 2) sum j can be formed including ith element,
                if dp[i−1][j−nums[i]]==true
            """
            for j in range(subset_sum + 1):
                if curr <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][subset_sum]


if __name__ == '__main__':
    s = Solution()
    print(s.canPartition_dp([1, 5, 11, 5]))
