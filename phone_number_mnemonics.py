#!/usr/bin/env python
# coding:utf-8
"""
@FileName : phone_number_mnemonics.py
@Author   : Harsh Parikh
@Date     : 9/4/21 12:21 AM
"""


# Time: O(n * 4^n) | Space = O(n * 4^n )
# n is total digit in phone number
# 4 ^ n because max we need to do 4 calls for digits(7, 9)
def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    phoneDictn = {
        '0': ['0'],
        '1': ['1'],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def dfs(phoneNumber, idx, phoneDictn, path, paths):
        if idx == len(phoneNumber):
            paths.append("".join(path))
            return

        for letter in phoneDictn[phoneNumber[idx]]:
            dfs(phoneNumber, idx + 1, phoneDictn, path + [letter], paths)

    path = []
    paths = []
    dfs(phoneNumber, 0, phoneDictn, path, paths)

    return paths

