# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: word_break.py
# @Date:   9/20/20, Sun
"""
139. Word Break
Medium

4965

246

Add to List

Share
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
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


class Solution:
    """
    def wordBreak(self, s, wordDict):

        dp = [False for i in range(len(s) + 1)] #(1)
        dp[0] = True

        for i in range(len(s) + 1): #(2)
            for j in range(i):
                if dp[j] and s[j:i] in wordDict: #(3)
                    dp[i] = True
                    break #(4)

        return dp[len(s)] #(5)
    """

    def wordBreak(self, s, wordDict):

        wordSet = set(wordDict)
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True

        return dp[len(s)]

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:

        def dfs(string, wordSet, dp):
            if not string:
                return True

            if string in dp:
                return dp[string]

            if string in wordSet:
                dp[string] = True
                return True

            for i in range(1, len(string)):
                if string[:i] in wordSet:
                    if dfs(string[i:], wordSet, dp):
                        dp[string[i:]] = True
                        return True

            dp[string] = False
            return False

        dp = {}

        return dfs(s, set(wordDict), dp)

    def wordBreak3(self, s: str, wordDict: List[str]) -> bool:

        dp = [True] + [False] * len(s)

        if s:
            trie = Trie()
            for word in wordDict:
                trie.insert(word)

            for i in range(1, len(dp)):
                if dp[i - 1]:
                    root, j = trie.root, i
                    while j - 1 < len(s) and s[j - 1] in root:
                        root = root[s[j - 1]]
                        j += 1
                        if "*" in root:
                            dp[j - 1] = True
            return dp[-1]

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code", "coe"]))
    print(s.wordBreak("catsandog", ["cats", "dogs", "sand", "an", "cat"]))
