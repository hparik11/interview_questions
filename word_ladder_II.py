# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: word_ladder_II.py
# @Date:   10/20/20, Tue
"""
126. Word Ladder II

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

"""


## Solution 1
def findLadders(self, beginWord, endWord, wordList):
    if not endWord or not beginWord or not wordList or endWord not in wordList \
            or beginWord == endWord:
        return []

    L = len(beginWord)

    # Dictionary to hold combination of words that can be formed,
    # from any given word. By changing one letter at a time.
    all_combo_dict = collections.defaultdict(list)
    for word in wordList:
        for i in range(L):
            all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

    # Shortest path, BFS
    ans = []
    queue = collections.deque()
    queue.append((beginWord, [beginWord]))
    visited = set([beginWord])

    while queue and not ans:
        # print(queue)
        length = len(queue)
        # print(queue)
        localVisited = set()
        for _ in range(length):
            word, path = queue.popleft()
            for i in range(L):
                for nextWord in all_combo_dict[word[:i] + "*" + word[i + 1:]]:
                    if nextWord == endWord:
                        # path.append(endword)
                        ans.append(path + [endWord])
                    if nextWord not in visited:
                        localVisited.add(nextWord)
                        queue.append((nextWord, path + [nextWord]))
        visited = visited.union(localVisited)
    return ans
