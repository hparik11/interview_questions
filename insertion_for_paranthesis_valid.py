# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: insertion_for_paranthesis_valid.py
# @Date:   9/15/20, Tue
"""
Minimum Add to Make Parentheses Valid
Medium

810

60

Add to List

Share
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.



Example 1:

Input: "())"
Output: 1
Example 2:

Input: "((("
Output: 3
Example 3:

Input: "()"
Output: 0
Example 4:

Input: "()))(("
Output: 4
"""


class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        if not S:
            return 0
        if len(S) == 1:
            return 1

        stack = 0
        count = 0

        for ch in S:
            if ch == '(':
                stack += 1
            elif ch == ')':
                if stack == 0:
                    count += 1
                else:
                    stack -= 1

        return count + stack


if __name__ == '__main__':
    s = Solution()
    print(s.minAddToMakeValid("())"))
    print(s.minAddToMakeValid(")("))
    print(s.minAddToMakeValid("(())"))
    print(s.minAddToMakeValid("((("))
    print(s.minAddToMakeValid(""))
