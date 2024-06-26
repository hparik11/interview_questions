# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: kmp.py
# @Date:   9/5/20, Sat


def knuthMorrisPrattAlgorithm(string, substring):
    # Write your code here.
    pattern = buildSubStringArray(substring)

    i = 0
    j = 0
    while i < len(string) and j < len(substring):
        if string[i] == substring[j]:
            i += 1
            j += 1
        else:
            if j > 0:
                j = pattern[j - 1] + 1
            else:
                i += 1

    return j == len(substring)


def buildSubStringArray(substring):
    i = 1
    j = 0

    pattern = [-1 for _ in range(len(substring))]

    while i < len(substring):
        if substring[i] == substring[j]:
            pattern[i] = j
            i += 1
            j += 1
        else:
            if j > 0:
                j = pattern[j - 1] + 1
            else:
                i += 1

    return pattern


if __name__ == '__main__':
    # print(knuthMorrisPrattAlgorithm("aefaefaefaedaefaedaefaefa", "aefaedaefaef"))
    print(knuthMorrisPrattAlgorithm("abxabcabcaby", "abcaby"))
