"""
213. House Robber II
Medium

3609

70

Add to List

Share
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
"""


class Solution:
    def rob(self, nums) -> int:
        ## RC ##
        ## APPROACH : DP ##
        ## LOGIC ##
        ## 1. Only 2 scenarios possible
        ##     a) Rob 1st and donot rob last
        ##     b) Rob last and donot rob first.
        ## We take maximum of both cases.

        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(N) ##

        if not nums:
            return 0

        def house_robber(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

            return max(dp[-1], dp[-2])

        if len(nums) <= 2:
            return max(nums)

        return max(house_robber(nums[1:]), house_robber(nums[:-1]))


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
