#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_swap_LR_string.py
@Author   : Harsh Parikh
@Date     : 9/18/21 12:36 PM

777. Swap Adjacent in LR String

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL",
a move consists of either replacing one occurrence of "XL" with "LX", or
replacing one occurrence of "RX" with "XR". Given the starting string start
and the ending string end, return True if and only if there exists a sequence
of moves to transform one string to the other.



Example 1:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Example 2:

Input: start = "X", end = "L"
Output: false
Example 3:

Input: start = "LLR", end = "RRL"
Output: false
Example 4:

Input: start = "XL", end = "LX"
Output: true
Example 5:

Input: start = "XLLR", end = "LXLX"
Output: false
"""

from collections import Counter


class Solution:
    def canTransform(self, start: str, end: str) -> bool:

        if len(start) != len(end):
            return False

        startFreqDictn = Counter(start)
        endFreqDictn = Counter(end)

        if startFreqDictn.get('L', 0) != endFreqDictn.get('L', 0) \
                or startFreqDictn.get('X', 0) != endFreqDictn.get('X', 0) \
                or startFreqDictn.get('R', 0) != endFreqDictn.get('R', 0):
            return False

        startDictn = [(s, idx) for idx, s in enumerate(start) if s in ('L', 'R')]
        endDictn = [(e, idx) for idx, e in enumerate(end) if e in ('L', 'R')]

        for (s, i), (e, j) in zip(startDictn, endDictn):

            if s != e:
                return False

            elif s == 'L':
                if i < j:
                    return False
            elif s == 'R':
                if i > j:
                    return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canTransform(start="RXXLRXRXL", end="XRLXXRRLX"))
