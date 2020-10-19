# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: shortest_word_distance_II.py
# @Date:   9/27/20, Sun
"""
Shortest Word Distance II
Medium

380

123

Add to List

Share
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
"""

from typing import List
from collections import defaultdict


class WordDistance:

    def __init__(self, words: List[str]):
        self.dictn = defaultdict(list)
        for i, word in enumerate(words):
            self.dictn[word].append(i)

    def findShortest(self, list1, list2):
        res = float('inf')

        for each in list1:
            left = 0
            right = len(list2) - 1

            while left <= right:
                mid = left + (right - left) // 2
                res = min(res, abs(each - list2[mid]))
                if each < list2[mid]:
                    right = mid - 1
                elif each > list2[mid]:
                    left = mid + 1

        return res

    def shortest(self, word1: str, word2: str) -> int:
        # return abs(self.dictn[word1] - self.dictn[word2])
        print(self.dictn)
        return self.findShortest(self.dictn[word1], self.dictn[word2])


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)

if __name__ == '__main__':
    s = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
    print(s.shortest("coding", "practice"))
    print(s.shortest("makes", "practice"))
    print(s.shortest("coding", "makes"))
    print(s.shortest("perfect", "coding"))
