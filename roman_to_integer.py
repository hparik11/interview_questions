#!/usr/bin/env python
# coding:utf-8
"""
Name : roman_to_integer.py.py
Author : Harsh Parikh
Time    : 6/13/21 12:13 AM
"""

"""
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Example 2:

Input: s = "IV"
Output: 4
Example 3:

Input: s = "IX"
Output: 9
Example 4:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        romanToIntIndex = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        decimal = 0
        for i, ch in enumerate(s):
            if i > 0 and romanToIntIndex[ch] > romanToIntIndex[s[i - 1]]:
                decimal += romanToIntIndex[ch] - 2 * romanToIntIndex[s[i - 1]]
            else:
                decimal += romanToIntIndex[ch]

        return decimal


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("III") == 3)
    print(s.romanToInt("IV") == 4)
    print(s.romanToInt("VII") == 7)
    print(s.romanToInt("CM") == 900)
    print(s.romanToInt("MC") == 1100)

