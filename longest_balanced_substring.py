#!/usr/bin/env python
# coding:utf-8
"""
@FileName : longest_balanced_substring.py
@Author   : Harsh Parikh
@Date     : 8/28/21 10:38 PM

32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.



Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0

"""


# O(n) time and space
def longestBalancedSubstring(string):
    # Write your code here.
    maxLength = 0
    idxStack = [-1]

    for i in range(len(string)):
        if string[i] == "(":
            idxStack.append(i)
        else:
            idxStack.pop()
            if len(idxStack) == 0:
                idxStack.append(i)
            else:
                balancedSubstringStartIdx = idxStack[len(idxStack) - 1]
                currentLength = i - balancedSubstringStartIdx
                maxLength = max(maxLength, currentLength)
    return maxLength


# O(N) time and O(1) space
def longestBalancedSubstring2(string):
    # Write your code here.

    openParenthesis = 0
    closeParenthesis = 0
    maxLength = 0

    # Left to right
    for i, ch in enumerate(string):
        if ch == '(':
            openParenthesis += 1
        else:
            closeParenthesis += 1

        if openParenthesis == closeParenthesis:
            maxLength = max(maxLength, closeParenthesis * 2)
        elif closeParenthesis > openParenthesis:
            openParenthesis = 0
            closeParenthesis = 0

    # Now, we have to check right to left
    # in case we missed the substring when we had open paran > close
    openParenthesis = 0
    closeParenthesis = 0

    for i in range(len(string) - 1, -1, -1):
        ch = string[i]

        if ch == '(':
            openParenthesis += 1
        else:
            closeParenthesis += 1

        if openParenthesis == closeParenthesis:
            maxLength = max(maxLength, closeParenthesis * 2)

        elif openParenthesis > closeParenthesis:
            openParenthesis = 0
            closeParenthesis = 0

    return maxLength
