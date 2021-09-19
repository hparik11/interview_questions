# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: concatenated_words.py
# @Date:   10/4/20, Sun
"""
Concatenated Words

Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
"""

from typing import List


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]

        node['*'] = True

    def search(self, word, start, end, count):
        node = self.root

        ch = word[start]
        if ch not in node:
            return False

        while start <= end and word[start] in node:
            ch = word[start]
            node = node[ch]

            print(start, end, ch, node, count)

            if '*' in node:

                if count > 1:
                    return True
                count += 1
                # print(count)
                if self.search(word, start, end, count):
                    return True
            start += 1
        return False


class Solution:
    # def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    #     words.sort(key=len)
    #     print(words)
    #     trie = Trie()
    #
    #     for word in words:
    #         trie.insert(word)
    #
    #     final_words = []
    #     for word in words:
    #         # print(word, trie.search(word, 0, len(word) - 1, 0))
    #         if trie.search(word, 0, len(word) - 1, 0):
    #             final_words.append(word)
    #
    #     return final_words

    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        preWords = set()

        # asc order of word length, since longer words are formed by shorter words
        words.sort(key=len)

        # for each short word start building preWords
        for word in words:
            if self.wordBreak(word, preWords):
                res.append(word)
            preWords.add(word)

        return res

    # Word Break I template
    def wordBreak(self, string, words):
        if not words:
            return False

        dp = [False] * (len(string) + 1)
        dp[0] = True

        for i in range(len(string) + 1):
            for j in range(i):
                if dp[j] and string[j:i] in words:
                    dp[i] = True
                    break

        return dp[-1]

    def findAllConcatenatedWordsInADict1(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d = set(words)

        def dfs(currWord):
            for i in range(1, len(currWord)):
                prefix = currWord[:i]
                suffix = currWord[i:]

                if prefix in d and suffix in d:
                    return True

                if prefix in d and dfs(suffix):
                    return True

            return False

        res = []
        for word in words:
            if dfs(word):
                res.append(word)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findAllConcatenatedWordsInADict(
        ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]))
    # print(s.findAllConcatenatedWordsInADict(["cat", "dog", "catdog"]))
