# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: shortest_word_distance_III.py
# @Date:   9/27/20, Sun
"""
245. Shortest Word Distance III

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
"""
from typing import List
from collections import defaultdict


class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        dictn = defaultdict(list)
        for i, word in enumerate(words):
            dictn[word].append(i)

        return self.findShortest(dictn[word1], dictn[word2])

    def findShortest(self, list1, list2):
        res = float('inf')

        for each in list1:
            left = 0
            right = len(list2) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if abs(each - list2[mid]) > 0:
                    res = min(res, abs(each - list2[mid]))

                if each < list2[mid]:
                    right = mid - 1
                elif each >= list2[mid]:
                    left = mid + 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding") == 1)
    print(s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "makes") == 3)
    print(s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "make") == float('inf'))
