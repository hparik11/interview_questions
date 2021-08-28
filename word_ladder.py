# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: word_ladder
# @Date:   9/10/20, Thu
"""
Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

from typing import List


# Time Complexity: O({M}^2 * N) where M is the length of each word and N is the total number of words in the input word list.
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if not beginWord or not endWord or not wordList:
            return 0

        count = 1
        if beginWord == endWord:
            return count

        visited = {}
        queue = [beginWord]
        visited[beginWord] = True
        wordList = set(wordList)

        while len(queue) > 0:
            for i in range(len(queue)):
                word = queue.pop(0)

                if word == endWord:
                    return count

                for each in self.findNeighbours(word, visited, wordList):
                    queue.append(each)

            count += 1

        return 0

    def findNeighbours(self, word, visited, wordList):

        neighbors = []

        for i, ch in enumerate(word):
            for j in range(26):
                newWord = word[:i] + chr(j + ord('a')) + word[i + 1:]
                if (newWord not in visited) and (newWord in wordList):
                    visited[newWord] = True
                    neighbors.append(newWord)

        return neighbors


if __name__ == '__main__':
    s = Solution()
    print(s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
