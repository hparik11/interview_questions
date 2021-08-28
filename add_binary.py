#!/usr/bin/env python
# coding:utf-8
"""
@FileName : add_binary.py
@Author   : Harsh Parikh
@Date     : 7/24/21 12:08 AM

67. Add Binary

Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if not a:
            return b
        if not b:
            return a

        i = len(a) - 1
        j = len(b) - 1

        summation = ""
        carry = 0

        while i >= 0 or j >= 0:
            if j < 0:
                currSum = carry + int(a[i])
            elif i < 0:
                currSum = carry + int(b[j])
            else:
                currSum = carry + int(a[i]) + int(b[j])

            if currSum > 1:
                carry = 1
            else:
                carry = 0

            if currSum % 2 == 0:
                currSum = 0
            else:
                currSum = 1

            summation += str(currSum)

            i -= 1
            j -= 1

        if carry:
            summation += str(carry)

        return "".join(reversed(summation))


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("11", "1"))
