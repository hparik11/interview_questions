#!/usr/bin/env python
# coding:utf-8
"""
@FileName : best_time_buy_sell_stock_iV.py
@Author   : Harsh Parikh
@Date     : 6/27/21 11:21 PM

188. Best Time to Buy and Sell Stock IV

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

"""

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        currProfits = [0 for _ in range(len(prices))]
        prevProfits = [0 for _ in range(len(prices))]

        for t in range(1, k + 1):
            maxSoFar = float('-inf')
            for d in range(1, len(prices)):
                maxSoFar = max(maxSoFar, prevProfits[d - 1] - prices[d - 1])
                currProfits[d] = max(currProfits[d - 1], maxSoFar + prices[d])

            prevProfits = currProfits[:]

        return currProfits[-1]
