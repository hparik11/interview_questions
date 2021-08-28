#!/usr/bin/env python
# coding:utf-8
"""
@FileName : zigzag_conversion.py
@Author   : Harsh Parikh
@Date     : 8/13/21 11:24 PM

6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 0:
            return ""

        if numRows == 1:
            return s

        rows = [''] * numRows

        i = 0
        rowIdx = 0
        step = 1

        while i < len(s):
            rows[rowIdx] += s[i]

            if rowIdx == numRows - 1:
                step = -1
            elif rowIdx == 0:
                step = 1

            rowIdx += step

            i += 1

        return ''.join(rows)


if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 4))
