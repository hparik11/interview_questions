# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: ways_to_make_coin_changes.py
# @Date:   8/24/20, Mon

"""
518. Coin Change 2
Medium

2170

64

Add to List

Share
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.



Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for j in range(amount + 1):
                if coin <= j:
                    dp[j] = dp[j] + dp[j - coin]
        print(dp)
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.change(5, [1, 2, 5]))
