#!/usr/bin/env python
# coding:utf-8
"""
@FileName : english_words_to_integer.py
@Author   : Harsh Parikh
@Date     : 8/1/21 2:28 PM

English to Integer
Example: One hundred twenty three --> 123

Example 1:

Input: "Three hundred million"
Output: 300,000,000
Example 2:

Input: "Five Hundred Thousand"
Output: 500,000

"""


def english_words_to_integer(words):
    smallNums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
                 "ten": 10,
                 "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
                 "seventeen": 17, "eighteen": 18, "nineteen": 19,
                 "twenty": 20,
                 "thirty": 30,
                 "forty": 40,
                 "fifty": 50,
                 "sixty": 60,
                 "seventy": 70,
                 "eighty": 80,
                 "ninety": 90}

    bigNums = {"hundred": 100, "thousand": 1000, "million": 1000000, "billion": 1000000000}

    words_list = words.split()
    finalNum = 0
    tempNum = 0
    for word in words_list:
        word = word.lower()
        if word in smallNums:
            tempNum += smallNums[word]
        elif word == "hundred":
            tempNum *= 100
        elif word in bigNums:
            tempNum *= bigNums[word]
            finalNum += tempNum
            tempNum = 0

    finalNum += tempNum
    return finalNum


if __name__ == '__main__':
    print(english_words_to_integer("One hundred twenty three"))
    print(english_words_to_integer("One thousand two hundred twenty three"))
    print(english_words_to_integer("Three hundred million five thousand forty five"))
    print(english_words_to_integer("Forty Six Million Eighty One"))
