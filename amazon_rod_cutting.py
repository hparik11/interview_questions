# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: amazon_rod_cutting.py
# @Date:   10/18/20, Sun
"""
Python Program for Cutting a Rod | DP-13
Last Updated: 12-12-2018
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n.
Determine the maximum value obtainable by cutting up the rod and selling the pieces.
For example, if length of the rod is 8 and the values of different pieces are given as following,
then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)


length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 3   5   8   9  10  17  17  20
"""

# A Naive recursive solution
# for Rod cutting problem
import sys


# Returns the best obtainable price for a rod of length n
# and price[] as prices of different pieces
def cutRod(price, n):
    if n <= 0:
        return 0
    max_val = -sys.maxsize - 1

    # Recursively cut the rod in different pieces
    # and compare different configurations
    for i in range(0, n):
        max_val = max(max_val, price[i] +
                      cutRod(price, n - i - 1))
    return max_val


def cutRod1(price, n):

    profit = [0 for _ in range(n + 1)]

    # Recursively cut the rod in different pieces
    # and compare different configurations
    for i in range(1, n + 1):
        max_price = float('-inf')
        for j in range(0, n + 1):
            if j < i:
                max_price = max(max_price, price[j] + profit[i - j - 1])

        profit[i] = max_price

    return profit[-1]


if __name__ == '__main__':
    arr = [1, 5, 8, 9, 10, 17, 17, 20]
    size = len(arr)
    print("Maximum Obtainable Value is", cutRod1(arr, size))
