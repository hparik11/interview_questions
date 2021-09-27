# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: min_coin_change.py
# @Date:   8/24/20, Mon

"""
322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
"""

from typing import List

### Brute force = amount^(no. of coins) 𝑂(A^n)

"""
DP: Time O(A * N)
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
            dp = [float('inf') for _ in range(amount + 1)]

            for i in range(len(coins)):
                for j in range(amount + 1):
                    if j == 0:
                        dp[j] = 0

                    if coins[i] <= j:
                        dp[j] = min(1 + dp[j - coins[i]], dp[j])

            print(dp)
            return dp[-1] if dp[-1] != float('inf') else -1


if __name__ == '__main__':
    s = Solution()
    assert s.coinChange([1, 2, 5], 11) == 3
    assert s.coinChange([2], 3) == -1
