"""
953. Verifying an Alien Dictionary

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.



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


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dictn = defaultdict(int)

        for i, ch in enumerate(order):
            order_dictn[ch] = i

        for i in range(len(words) - 1):
            first_word = words[i]
            for j in range(i + 1, len(words)):
                second_word = words[j]
                k = 0
                l = 0
                while k < len(first_word) and l < len(second_word):
                    # print(first_word[k], second_word[l])
                    if order_dictn[first_word[k]] < order_dictn[second_word[l]]:
                        break
                    elif order_dictn[first_word[k]] > order_dictn[second_word[l]]:
                        return False
                    else:
                        k += 1
                        l += 1

                if k < len(first_word) and l == len(second_word):
                    return False

        return True