# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: score_of_paranthesis.py
# @Date:   10/17/20, Sat
"""
856. Score of Parentheses
Medium

1361

47

Add to List

Share
Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6

"""


class Solution:
    def scoreOfParentheses(self, S: str) -> object:
        """
        :type S: str
        :rtype: int
        """
        stack = []
        score = 0
        openParen = False
        for paren in S:
            if paren == '(':
                stack.append('(')
                openParen = True
            else:
                if openParen:
                    score += pow(2, len(stack) - 1)
                    stack.pop()
                    openParen = False
                else:
                    stack.pop()
        return score


if __name__ == '__main__':
    s = Solution()
    print(s.scoreOfParentheses("(()(()))"))
    print(s.scoreOfParentheses("(()())"))

