#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_remove_invalid_parenthesis.py
@Author   : Harsh Parikh
@Date     : 9/13/21 11:35 AM

301. Remove Invalid Parentheses
Hard

3851

183

Add to List

Share
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.



Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
Example 3:

Input: s = ")("
Output: [""]
"""


class Solution:
    def removeInvalidParentheses(self, s: str):

        def isValid(s):
            extraOpenParan = 0
            extraCloseParan = 0

            for i in range(len(s)):
                if s[i] == '(':
                    extraOpenParan += 1
                elif s[i] == ')':
                    if extraOpenParan > 0:
                        extraOpenParan -= 1
                    else:
                        extraCloseParan += 1

            return (extraOpenParan == 0 and extraCloseParan == 0), extraOpenParan, extraCloseParan

        def dfs(s, extraOpen, extraClose, results):
            visited.add(s)

            if extraOpen == 0 and extraClose == 0 and isValid(s)[0]:
                results.append(s)

            for i, ch in enumerate(s):

                if ch != '(' and ch != ')':
                    continue  # if it is any other char ignore.

                if (ch == '(' and extraOpen == 0) or (ch == ')' and extraClose == 0):
                    continue  # if extraOpen == 0 then removing '(' will only cause imbalance. Hence, skip.

                if (s[:i] + s[i + 1:]) not in visited:
                    if ch == '(':
                        dfs(s[:i] + s[i + 1:], extraOpen - 1, extraClose, results)
                    elif ch == ')':
                        dfs(s[:i] + s[i + 1:], extraOpen, extraClose - 1, results)

        valid_parenthesis, extraOpen, extraClose = isValid(s)

        if valid_parenthesis:
            return [s]

        results, visited = [], set()
        dfs(s, extraOpen, extraClose, results)

        return results


if __name__ == '__main__':
    s = Solution()
    print(s.removeInvalidParentheses("(a)())()"))