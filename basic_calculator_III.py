#!/usr/bin/env python
# coding:utf-8
"""
@FileName : basic_calculator_III.py
@Author   : Harsh Parikh
@Date     : 7/8/21 6:06 PM

772. Basic Calculator III

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "1+1"
Output: 2
Example 2:

Input: s = "6-4/2"
Output: 4
Example 3:

Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
Example 4:

Input: s = "(2+6*3+5-(3*14/7+2)*5)+3"
Output: -12
Example 5:

Input: s = "0"
Output: 0
"""

import math


class Solution:
    def calculate(self, s):
        if not s:
            return 0
        operators = {'+', '-', '*', '/'}
        stack, currentNumber, sign = [], 0, "+"

        for i in range(len(s)):
            if s[i].isdigit():
                currentNumber = currentNumber * 10 + int(s[i])
            elif s[i] == '(':
                stack.append(sign)
                sign = '+'
            elif s[i] == ')':
                self.append_result_to_stack(sign, currentNumber, stack)
                # print(stack, currentNumber)
                currentNumber = 0
                # Calculating expression between parentheses
                while stack and stack[-1] not in operators:
                    currentNumber += stack.pop()

                sign = stack.pop()

            if (s[i] in operators) or i == len(s) - 1:
                self.append_result_to_stack(sign, currentNumber, stack)
                sign = s[i]
                currentNumber = 0

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
    print(s.calculate("(2+6*3+5-(3*14/7+2)*5)+3"))
