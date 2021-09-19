#!/usr/bin/env python
# coding:utf-8
"""
@FileName : pattern_matcher.py
@Author   : Harsh Parikh
@Date     : 7/15/21 12:56 AM

Given a pattern and a string s, return true if s matches the pattern.

A string s matches a pattern if there is some bijective mapping of single characters to strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.



Example 1:

Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"
Example 2:

Input: pattern = "aaaa", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "asd"
Example 3:

Input: pattern = "abab", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "a"
'b' -> "sdasd"
Note that 'a' and 'b' cannot both map to "asd" since the mapping is a bijection.
Example 4:

Input: pattern = "aabb", s = "xyzabcxzyabc"
Output: false
"""

from collections import defaultdict


def patternMatcher(pattern, string):
    # Write your code here.
    if len(string) < len(pattern):
        return []
    newPattern = getNewPattern(pattern)
    didSwitch = pattern[0] != newPattern[0]

    counts, firstPosOfY = getCountsAndFirstPositionOfY(newPattern)

    print(newPattern, counts, firstPosOfY)

    if firstPosOfY != -1:
        for lenOfX in range(1, len(string)):

            lenOfY = (len(string) - lenOfX * counts['x']) / counts['y']

            if lenOfY <= 0 or lenOfY % 1 != 0:
                continue

            lenOfY = int(lenOfY)

            firstYIdx = firstPosOfY * lenOfX
            x = string[:lenOfX]
            y = string[firstYIdx: firstYIdx + lenOfY]

            print(x, y)
            potentialMatch = map(lambda char: x if char == 'x' else y, newPattern)

            # print(string == "".join(potentialMatch))
            if string == "".join(potentialMatch):
                return [x, y] if not didSwitch else [y, x]

    else:
        lenOfX = len(string) / counts['x']
        if lenOfX % 1 == 0:
            lenOfX = int(lenOfX)
            x = string[:lenOfX]

            potentialMatch = map(lambda char: x, newPattern)
            if string == "".join(potentialMatch):
                return [x, ""] if not didSwitch else ["", x]

    return []


def getNewPattern(pattern):
    patternCharacters = list(pattern)
    if pattern[0] == 'x':
        return patternCharacters
    else:
        return list(map(lambda char: "x" if char == 'y' else 'y', patternCharacters))


def getCountsAndFirstPositionOfY(pattern):
    counts = defaultdict(int)
    firstPosOfy = -1

    for idx, character in enumerate(pattern):
        counts[character] += 1

        if character == 'y' and firstPosOfy == -1:
            firstPosOfy = idx

    return counts, firstPosOfy
