#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_alien_dictionary.py
@Author   : Harsh Parikh
@Date     : 7/21/21 11:20 AM

953. Verifying an Alien Dictionary

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
"""

from collections import defaultdict
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        orderDictn = defaultdict(int)

        for i, ch in enumerate(order):
            orderDictn[ch] = i

        for i in range(len(words) - 1):
            firstWord = words[i]
            for j in range(i + 1, len(words)):
                secondWord = words[j]
                k = 0
                l = 0

                while k < len(firstWord) and l < len(secondWord):
                    # Break when we find order of first-word letter is less than order of second-word letter
                    if orderDictn[firstWord[k]] < orderDictn[secondWord[l]]:
                        break

                    # return false when we find otherwise
                    elif orderDictn[firstWord[k]] > orderDictn[secondWord[l]]:
                        return False
                    # if we find same order for both words letter than simply increase the pointer
                    else:
                        k += 1
                        l += 1

                # At last check, if first word has still few letters left but second word not then return False
                if k < len(firstWord) and l == len(secondWord):
                    return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isAlienSorted(["apple", "app"],
                          "abcdefghijklmnopqrstuvwxyz"))

    print(s.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
