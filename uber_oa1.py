# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: uber_oa1.py
# @Date:   9/10/20, Thu
"""
Subtract the Product and Sum of Digits of an Integer

Given an integer number n, return the difference between the product of its digits and the sum of its digits.


Example 1:

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21
"""

from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        numbers = []
        while True:
            value = n % 10
            numbers.insert(0, value)
            n = n // 10
            if n == 0:
                break

        return reduce(lambda x, y: x * y, numbers) - reduce(lambda x, y: x + y, numbers)


if __name__ == '__main__':
    s = Solution()
    print(s.subtractProductAndSum(4421) == 21)
