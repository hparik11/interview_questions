#!/usr/bin/env python
# coding:utf-8
"""
@FileName : digit_sum_to_ten_nth_num.py
@Author   : Harsh Parikh
@Date     : 10/2/21 10:05 AM

n-th number whose sum of digits is ten
Difficulty Level : Easy
Last Updated : 26 Apr, 2021
Given an integer value n, find out the n-th positive integer whose sum is 10.
Examples:

Input: n = 2
Output: 28
The first number with sum of digits as
10 is 19. Second number is 28.

Input: 15
Output: 154
"""


# 19, 28, 37, 46, 55, ....
def find_nth_num_digit_sum_to_10(n):
    curr = 19

    if n == 1:
        return curr

    idx = 1
    while True:
        sum = 0

        x = curr
        while x != 0:
            x, quotient = divmod(x, 10)
            sum += quotient

        if sum == 10:
            if idx == n:
                return curr
            idx += 1

        curr += 9


if __name__ == '__main__':
    print(find_nth_num_digit_sum_to_10(3))
