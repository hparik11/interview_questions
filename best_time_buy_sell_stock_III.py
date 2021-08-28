#!/usr/bin/env python
# coding:utf-8
"""
@FileName : best_time_buy_sell_stock_III.py
@Author   : Harsh Parikh
@Date     : 6/27/21 11:13 PM


123. Best Time to Buy and Sell Stock III

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Example 4:

Input: prices = [1]
Output: 0
"""


def maxProfit(prices):
    max_total_profit = 0
    first_profits = [0] * len(prices)
    min_price = float('inf')

    # Forward phase
    for i in range(len(prices)):
        min_price = min(min_price, prices[i])
        profit = prices[i] - min_price
        max_total_profit = max(max_total_profit, profit)
        first_profits[i] = max_total_profit

    max_price = float('-inf')

    # Backward phase
    for j in range(len(prices) - 1, 0, -1):
        max_price = max(max_price, prices[j])
        profit = max_price - prices[j]
        max_total_profit = max(max_total_profit, first_profits[j - 1] + profit)

    return max_total_profit


def maxProfit1(self, prices: List[int]) -> int:
    """
        3, 3, 5, 0, 0, 3, 1, 4
      0 0  0  0  0  0  0  0  0
      1 0  0  2  2  2  3  3  4
      2 0. 0  2  2. 2  5. 5  6

    """

    currProfits = [0 for _ in range(len(prices))]
    prevProfits = [0 for _ in range(len(prices))]

    for t in range(1, 3):
        maxSoFar = float('-inf')
        for d in range(1, len(prices)):
            maxSoFar = max(maxSoFar, prevProfits[d - 1] - prices[d - 1])
            currProfits[d] = max(currProfits[d - 1], maxSoFar + prices[d])

        prevProfits = currProfits[:]

    # print(currProfits)
    return currProfits[-1]
