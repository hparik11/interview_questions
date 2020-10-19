# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: kmp.py
# @Date:   9/5/20, Sat


def knuthMorrisPrattAlgorithm(string, substring):
    # Write your code here.
    result = buildSubStringArray(substring)

    i = 0
    j = 0
    while i < len(string) and j < len(substring):
        if string[i] == substring[j]:
            i += 1
            j += 1
        else:
            if j > 0:
                j = result[j - 1] + 1
            else:
                i += 1
    return j == len(substring)


def buildSubStringArray(substring):
    i = 1
    j = 0

    alist = [-1 for _ in range(len(substring))]

    while i < len(substring):
        if substring[i] == substring[j]:
            alist[i] = j
            i += 1
            j += 1
        else:
            if alist[j - 1] == -1:
                j = 0
                i += 1
            else:
                j = alist[j - 1] + 1
                alist[i] = j

    return alist


if __name__ == '__main__':
    knuthMorrisPrattAlgorithm("aefaefaefaedaefaedaefaefa", "aefaedaefaef")
    knuthMorrisPrattAlgorithm("abxabcabcaby", "abcaby")
