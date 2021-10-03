#!/usr/bin/env python
# coding:utf-8
"""
@FileName : find_power.py
@Author   : Harsh Parikh
@Date     : 10/2/21 12:47 PM
"""


# time comp = log(base)
# return n^a
def find_power(base, power):
    # n = 3, a = 4
    # ans = 3 * 3 * 3 * 3
    # a = 4 = 100
    #
    ans = 1
    while power != 0:
        if power & 1 == 1:
            ans = ans * base

        # everytime multiply base with itself because we are left shifting
        base = base * base
        # left shift the power
        power >>= 1

    return ans


if __name__ == '__main__':
    print(find_power(3, 4))
