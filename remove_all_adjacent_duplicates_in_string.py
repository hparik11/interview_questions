#!/usr/bin/env python
# coding:utf-8
"""
@FileName : remove_all_adjacent_duplicates_in_string.py
@Author   : Harsh Parikh
@Date     : 9/5/21 12:18 PM

1047. Remove All Adjacent Duplicates In String

You are given a string s consisting of lowercase English letters.
A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.
It can be proven that the answer is unique.


Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return ""

        final_string = []

        for ch in s:
            if final_string and ch == final_string[-1]:
                final_string.pop()
            else:
                final_string.append(ch)

        return "".join(final_string)


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates("abbaca"))
