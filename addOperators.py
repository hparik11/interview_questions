#!/usr/bin/env python
# coding:utf-8
"""
@FileName : addOperators.py
@Author   : Harsh Parikh
@Date     : 7/9/21 12:05 AM

282. Expression Add Operators

Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.



Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []

"""


# Time - N * 4^N | Space - O(N)
class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # use dfs with curr_total and prev_val, add four expressions in expr. Time O(n*3^n)
        result, expr = [], ''
        curr_total, prev_val = 0, 0
        pos = 0
        self.dfs(num, target, pos, curr_total, prev_val, expr, result)
        return result

    # dfs helper
    def dfs(self, num, target, pos, curr_total, prev_val, expr, result):
        # stop criteria
        if pos == len(num) and curr_total == target:
            result.append(expr)
        else:
            val = 0
            for i in range(pos, len(num)):  # use for loop
                val = val * 10 + ord(num[i]) - ord('0')
                if pos == 0:  # corner case, no operation before first digit
                    self.dfs(num, target, i + 1, curr_total + val, val, expr + str(val), result)
                else:
                    # case '+'
                    self.dfs(num, target, i + 1, curr_total + val, val, expr + '+' + str(val), result)
                    # case '-'
                    self.dfs(num, target, i + 1, curr_total - val, -val, expr + '-' + str(val), result)
                    # case '*'
                    """
                    For someone who tries to figure why we use last,
                    Imagine you are currently evaluating the expression 5 + 2 * 3, the dfs method has last = 2, cur= 7,
                    To evaluate expression A + B * C, it should be read with multiplication taking precedence, A + (B * C), so result should be 5 + (2 * 3) => 11. Without last, one could end up calculating result as (5+2)*3 => 21
                    
                    Hence the expression, cur - last + last * val => 7-2 + (2 * 3) = 11
                    """
                    self.dfs(num, target, i + 1, curr_total - prev_val + prev_val * val, prev_val * val,
                             expr + '*' + str(val), result)
                    # can also extend to '/' case
                    # self.dfs(num, target, i+1, curr_total - prev_val + prev_val * 1.0 / val, prev_val * 1.0 / val, expr + '/' + str(val), result)
                if num[pos] == '0':  # deal with '025' case, string starts with '0'
                    break


if __name__ == '__main__':
    s = Solution()
    print(s.addOperators("232", 8))
