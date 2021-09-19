#!/usr/bin/env python
# coding:utf-8
"""
@FileName : amazon_power_of_2.py
@Author   : Harsh Parikh
@Date     : 8/4/21 6:23 PM

Give a number, return True or False if it is a power of 2.
"""

"""
is bitwise problem. All powers of 2, written in binary, will have only the most significant bit set (e.g. 2 -> 10, 4 -> 100, 8 -> 1000, 16 -> 10000). When you subtract 1 from a power of two, you get the bits flipped:
10 - 1 = 01
100 - 1 = 011
1000 - 1 = 0111
10000 - 1 = 01111
So if you do n & (n - 1), (aka & a power of 2 with itself minus one), you will get 0:
10 & 01 = 0
100 & 011 = 0
1000 & 0111 = 0
10000 & 01111 = 0

If you don't get a 0 from doing this, then it's not a power of 2.
"""