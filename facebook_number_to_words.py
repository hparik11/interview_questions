#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_number_to_words.py
@Author   : Harsh Parikh
@Date     : 7/17/21 1:27 AM

273. Integer to English Words

Convert a non-negative integer num to its English words representation.



Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

"""


class Solution:
    m = {1000000000: 'Billion', 1000000: 'Million', 1000: 'Thousand'}

    n = {100: 'Hundred',
         90: 'Ninety',
         80: 'Eighty',
         70: 'Seventy',
         60: 'Sixty',
         50: 'Fifty',
         40: 'Forty',
         30: 'Thirty',
         20: 'Twenty',
         19: 'Nineteen',
         18: 'Eighteen',
         17: 'Seventeen',
         16: 'Sixteen',
         15: 'Fifteen',
         14: 'Fourteen',
         13: 'Thirteen',
         12: 'Twelve',
         11: 'Eleven',
         10: 'Ten',
         9: 'Nine',
         8: 'Eight',
         7: 'Seven',
         6: 'Six',
         5: 'Five',
         4: 'Four',
         3: 'Three',
         2: 'Two',
         1: 'One'
         }

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        return self.convert_higher_numbers_into_word(num).strip()

    def convert_higher_numbers_into_word(self, number):
        words = []
        if number >= 1000:
            for each in self.m:
                if number >= each:
                    quotient, number = divmod(number, each)

                    words.extend(self.convert_hundreds_into_word(quotient))
                    words.append(self.m[each])

        words.extend(self.convert_hundreds_into_word(number))

        return " ".join(words)

    def convert_hundreds_into_word(self, number1):
        words = []

        if number1 >= 100:
            quotient, number1 = divmod(number1, 100)
            words.extend([self.n[quotient], self.n[100]])

        for j in self.n:
            if number1 >= j:
                words.append(self.n[j])
                number1 -= j

        return words


if __name__ == '__main__':
    s = Solution()

    print(s.convert_higher_numbers_into_word(1_111_123_122))
