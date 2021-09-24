#!/usr/bin/env python
# coding:utf-8
"""
@FileName : brace_expansion.py
@Author   : Harsh Parikh
@Date     : 8/7/21 12:09 AM

1087. Brace Expansion
You are given a string s representing a list of words. Each letter in the word has one or more options.

If there is one option, the letter is represented as is.
If there is more than one option, then curly braces delimit the options. For example, "{a,b,c}" represents options ["a", "b", "c"].
For example, if s = "a{b,c}", the first character is always 'a', but the second character can be 'b' or 'c'. The original list is ["ab", "ac"].

Return all words that can be formed in this manner, sorted in lexicographical order.



Example 1:

Input: s = "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
Example 2:

Input: s = "abcd"
Output: ["abcd"]
"""

from typing import List


class Solution:
    def expand(self, s: str) -> List[str]:

        result = ['']
        i = 0

        while i < len(s):
            currentCharacter = s[i]

            # just append the character outside of {}
            if currentCharacter.isalpha():
                result = [res + currentCharacter for res in result]

            # cross multiplication of inside {} with our result array elements
            # ab{c, d} -> abc, abd
            elif currentCharacter == '{':
                charactersInsideBraces = []

                while s[i] != '}':
                    if s[i].isalpha():
                        charactersInsideBraces.append(s[i])

                    i += 1

                result = [res + char for res in result for char in charactersInsideBraces]

            i += 1

        return sorted(result)


if __name__ == '__main__':
    s = Solution()
    print(s.expand("{a,b}c{d,e}f"))
