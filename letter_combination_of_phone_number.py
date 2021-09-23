#!/usr/bin/env python
# coding:utf-8
"""
@FileName : letter_combination_of_phone_number.py
@Author   : Harsh Parikh
@Date     : 7/14/21 8:25 PM

17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""

from itertools import product
from typing import  List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # digit_mapping = {0:"", 1:"", 2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        number_to_letter_dictn = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }

        if not digits:
            return []
        mappings = []
        for each_character in digits:
            mappings.append(number_to_letter_dictn[int(each_character)])

        if len(mappings) == 1:
            return mappings[0]

        return ["".join(each) for each in list(product(*mappings))]

    def letterCombinations_dfs(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_mapping = {'0': "", 1: "", '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs",
                         '8': "tuv", '9': "wxyz"}

        def dfs(digit_mapping, digits, idx, combination, combinations):
            if idx == len(digits):
                combinations.append(combination)
                return

            for ch in digit_mapping[digits[idx]]:
                dfs(digit_mapping, digits, idx + 1, combination + ch, combinations)

        combinations = []
        dfs(digit_mapping, digits, 0, "", combinations)

        return combinations


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations_dfs("23"))
