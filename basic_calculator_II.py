#!/usr/bin/env python
# coding:utf-8
"""
@FileName : basic_calculator_II.py
@Author   : Harsh Parikh
@Date     : 7/8/21 6:03 PM

227. Basic Calculator II

Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
"""

import math


class Solution:
    def calculate(self, s):
        if not s:
            return 0
        operators = {'+', '-', '*', '/'}
        stack, num, sign = [], 0, "+"

        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if (s[i] in operators) or i == len(s) - 1:
                self.append_result_to_stack(sign, num, stack)
                sign = s[i]
                num = 0

        return sum(stack)

    @staticmethod
    def append_result_to_stack(sign, num, stack):
        if sign == "-":
            stack.append(-num)
        elif sign == "+":
            stack.append(num)
        elif sign == "*":
            stack.append(stack.pop() * num)
        else:
            div_result = stack.pop() / num
            if div_result < 0:
                stack.append(math.ceil(div_result))
            else:
                stack.append(math.floor(div_result))


if __name__ == '__main__':
    s = Solution()
    print(s.calculate("2 + 4/2"))
