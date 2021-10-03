#!/usr/bin/env python
# coding:utf-8
"""
@FileName : perfect_number.py
@Author   : Harsh Parikh
@Date     : 10/2/21 10:45 AM

507. Perfect Number
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.



Example 1:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
Example 2:

Input: num = 6
Output: true
Example 3:

Input: num = 496
Output: true
Example 4:

Input: num = 8128
Output: true
Example 5:

Input: num = 2
Output: false

"""


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        divs = {1}

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divs.add(num // i)
                divs.add(i)

        return sum(divs) == num


if __name__ == '__main__':
    s = Solution()
    print(s.checkPerfectNumber(28))
