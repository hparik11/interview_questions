#!/usr/bin/env python
# coding:utf-8
"""
@FileName : complex_number_multiplication.py
@Author   : Harsh Parikh
@Date     : 7/30/21 6:20 PM

537. Complex Number Multiplication

A complex number can be represented as a string on the form "real+imaginaryi" where:

real is the real part and is an integer in the range [-100, 100].
imaginary is the imaginary part and is an integer in the range [-100, 100].
i2 == -1.
Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.



Example 1:

Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:

Input: num1 = "1+-1i", num2 = "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
"""


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a = ComplexNum(num1)
        b = ComplexNum(num2)

        real = a.real * b.real - (a.imaginary * b.imaginary)
        imaginary = a.real * b.imaginary + a.imaginary * b.real

        return str(real) + '+' + str(imaginary) + 'i'


class ComplexNum:
    def __init__(self, strr):
        parsed = strr.split('+')

        self.real = int(parsed[0])
        self.imaginary = int(parsed[1][:-1])