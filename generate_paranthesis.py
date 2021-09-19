#!/usr/bin/env python
# coding:utf-8
"""
@FileName : generate_parenthesis.py
@Author   : Harsh Parikh
@Date     : 7/29/21 10:36 AM

22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

"""


class Solution:
    def generateParenthesis(self, n: int):
        if not n:
            return []
        left, right, ans, path = n, n, [], ""

        self.backtracking(left, right, ans, path)

        return ans

    def backtracking(self, left, right, ans, path):
        if right < left:
            return

        if not left and not right:
            ans.append(path)
            return

        if left:
            self.backtracking(left - 1, right, ans, path + "(")

        if right:
            self.backtracking(left, right - 1, ans, path + ")")


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))