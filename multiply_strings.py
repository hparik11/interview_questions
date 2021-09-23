#!/usr/bin/env python
# coding:utf-8
"""
@FileName : multiply_strings.py
@Author   : Harsh Parikh
@Date     : 7/29/21 12:55 PM

43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.



Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #         res = [0] * (len(num1)+len(num2))
        #         for i in range(len(num1)-1, -1, -1):
        #             carry = 0
        #             for j in range(len(num2)-1, -1, -1):
        #                 tmp = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0')) + carry
        #                 carry = (res[i+j+1]+tmp) // 10
        #                 res[i+j+1] = (res[i+j+1]+tmp) % 10
        #             res[i] += carry

        #         res = ''.join(map(str, res))

        #         return '0' if not res.lstrip('0') else res.lstrip('0')

        product = [0] * (len(num1) + len(num2))
        pos = len(product) - 1

        for i in range(len(num1) - 1, -1, -1):
            tempPos = pos
            for j in range(len(num2) - 1, -1, -1):
                currProduct = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                product[tempPos] += currProduct
                product[tempPos - 1] += product[tempPos] // 10
                product[tempPos] %= 10
                tempPos -= 1

            pos -= 1

        res = ''.join(map(str, product))

        return '0' if not res.lstrip('0') else res.lstrip('0')