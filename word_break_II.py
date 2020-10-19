# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: word_break_II.py
# @Date:   10/17/20, Sat
"""
140. Word Break II
Hard

2537

418

Add to List

Share
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""
from typing import List
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # def dfs(s, memo):
        #     if not s:
        #         return [[]]
        #
        #     if s in memo:
        #         return memo[s]
        #
        #     for word in wordDict:
        #         if s.startswith(word):
        #             for sub in dfs(s[len(word):], memo):
        #                 memo[s].append([word] + sub)
        #
        #     print(memo)
        #     return memo[s]
        #
        # return [" ".join(words) for words in dfs(s, defaultdict(list))]

        def isWordBreak(s, wordSet):

            dp = [False for _ in range(len(s) + 1)]
            dp[0] = True

            for i in range(len(s) + 1):
                for j in range(i):
                    if dp[j] and s[j: i] in wordSet:
                        dp[i] = True
                        break

            return dp

        def backtrack(s, idx, path, paths):
            # Before we backtrack, we check whether the remaining string
            # can be splitted by using the dictionary,
            # in this way we can decrease unnecessary computation greatly.
            if dp[idx+len(s)]: # if word break possible then only proceed
                if not s:
                    paths.append(' '.join(path))
                else:
                    for i in range(1, len(s) + 1):
                        if s[:i] in wordSet:
                            backtrack(s[i:], idx + i, path + [s[:i]], paths)

        wordSet = set(wordDict)

        dp = isWordBreak(s, wordSet)
        path = []
        paths = []
        backtrack(s, 0, path, paths)
        return paths


if __name__ == '__main__':
    s = Solution()
    # print(s.wordBreak("leetcode", ["leet", "code", "coe"]))
    print(s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
