#!/usr/bin/env python
# coding:utf-8
"""
@FileName : best_time_buy_sell_stock.py
@Author   : Harsh Parikh
@Date     : 6/22/21 12:12 AM

121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


class Solution:

    def maxProfit(self, prices):
        length = len(prices)
        if length == 0:
            return 0
        minSoFar = float('inf')
        res = 0

        for i in range(0, len(prices)):
            minSoFar = min(minSoFar, prices[i])

            if prices[i] - minSoFar > res:
                res = prices[i] - minSoFar

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
