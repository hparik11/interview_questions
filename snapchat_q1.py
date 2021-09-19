#!/usr/bin/env python
# coding:utf-8
"""
@FileName : snapchat_q1.py
@Author   : Harsh Parikh
@Date     : 7/2/21 10:40 AM

Print the content in a string in order based on the occurrence and alphabets.

geeksforgeeks:

output: e4 g2 k2 s2 f1 o1 r1
"""

from collections import Counter


def printStringContentBasedOnOccurrences(input_string):
    character_frequency = Counter(input_string)
    sorted_characters_by_freq = sorted(character_frequency.items(), key=lambda x: (-x[1], x[0]))

    result_string = ''
    for character, freq in sorted_characters_by_freq:
        result_string += character + str(freq) + " "

    return result_string.rstrip()


if __name__ == '__main__':
    print(printStringContentBasedOnOccurrences("geeksforgeeks"))
