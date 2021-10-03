#!/usr/bin/env python
# coding:utf-8
"""
@FileName : gcd_lcm.py
@Author   : Harsh Parikh
@Date     : 10/2/21 11:47 PM
"""


class gcd_lcm:
    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)

    def lcm(self, a, b):
        return a * b // self.gcd(a, b)


if __name__ == '__main__':
    s = gcd_lcm()
    print(s.gcd(2, 7))
    print(s.lcm(2, 7))
