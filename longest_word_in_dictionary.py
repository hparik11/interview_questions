#!/usr/bin/env python
# coding:utf-8
"""
@FileName : longest_word_in_dictionary.py
@Author   : Harsh Parikh
@Date     : 8/6/21 5:56 PM

720. Longest Word in Dictionary

Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.



Example 1:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

"""

from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:

        def dfs(currWord, wordSet, dp):
            if len(currWord) == 1:
                return True

            if currWord in dp:
                return dp[currWord]

            for i in range(len(currWord)):
                newWord = currWord[:i] + currWord[i + 1:]

                if newWord in wordSet:
                    if dfs(newWord, wordSet, dp):
                        dp[newWord] = True
                        return True
                    dp[newWord] = False

            return False

        wordSet = set(words)
        words = sorted(wordSet, key=lambda x: (-len(x), x))

        dp = {}

        for word in words:
            if dfs(word, wordSet, dp):
                return word

        return ""


if __name__ == '__main__':
    s = Solution()
    print(s.longestWord(["w", "wo", "wor", "worl", "world"]))
    print(s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
