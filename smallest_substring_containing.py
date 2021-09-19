# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: smallest_substring_containing
# @Date:   9/5/20, Sat

from collections import Counter


def smallestSubstringContaining(bigString, smallString):
    # Write your code here.
    smallStringHashmap = Counter(smallString)
    dp = {}
    i = -1
    minLength = float('inf')
    startSub = 0
    endSub = 0
    while i < len(bigString) - len(smallString) + 1:
        i += 1
        if i in dp:
            continue
        j = i

        tempHashmap = smallStringHashmap.copy()
        start = -1
        while j < len(bigString):
            if bigString[j] in tempHashmap:
                if start == -1:
                    start = j
                tempHashmap[bigString[j]] -= 1

                if tempHashmap[bigString[j]] == 0:
                    del tempHashmap[bigString[j]]
                if not tempHashmap:
                    end = j
                    dp[start] = end

                    if minLength > end - start + 1:
                        minLength = end - start + 1
                        startSub = start
                        endSub = end

                    start = -1

            j += 1
    if startSub == 0 and endSub == 0:
        return ""
    return bigString[startSub: endSub + 1]


if __name__ == '__main__':
    print(smallestSubstringContaining("abcd$ef$axb$c$", "$$abf"))
