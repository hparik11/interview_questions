# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: custom_sort_string.py
# @Date:   9/18/20, Fri

"""
791. Custom Sort String

S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input:
S = "cba"
T = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
"""

from collections import Counter


class Solution:
    def customSortString(self, S: str, T: str) -> str:

        if not T or not S:
            return S

        counterDict = Counter(T)

        resultString = ''

        for ch in S:
            resultString += ch * counterDict[ch]
            del counterDict[ch]

        for key, value in counterDict.items():
            resultString += key * value

        print(resultString)
        return resultString


if __name__ == '__main__':
    s = Solution()
    print(s.customSortString("cba", "aacssbcd"))
