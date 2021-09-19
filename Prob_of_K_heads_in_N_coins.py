# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: Prob_of_K_heads_in_N_coins.py
# @Date:   10/13/20, Tue
"""
Probability of getting K heads in N coin tosses
Last Updated: 12-05-2020

Given two integers N and R. The task is to calculate the probability of getting exactly r heads in n successive tosses.

A fair coin has an equal probability of landing a head or a tail on each toss.

Examples:

Input : N = 1, R = 1
Output : 0.500000

Input : N = 4, R = 3
Output : 0.2500

https://www.geeksforgeeks.org/probability-of-getting-k-heads-in-n-coin-tosses/

"""


# Python3 program to find probability
# of getting K heads in N coin tosses

# Function to calculate factorial
def fact(n):
    res = 1
    for i in range(2, n + 1):
        res = res * i
    return res


# Applying the formula
def count_heads(n, r):
    output = fact(n) / (fact(r) * fact(n - r))
    output = output / (pow(2, n))
    return output


# Driver code
n = 4
r = 3

# Call count_heads with n and r
print(count_heads(n, r))
