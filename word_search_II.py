"""
212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
"""

from typing import List


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for each_word in words:
            trie.add(word=each_word)
        print(trie.root)
        visited = [[False for _ in row] for row in board]
        finalWords = {}
        r = len(board)
        c = len(board[0])

        for i in range(r):
            for j in range(c):
                self.dfs(i, j, board, visited, trie.root, finalWords, r, c)

        return list(finalWords.keys())

    def dfs(self, i, j, board, visited, trieNode, finalWords, r, c):

        if visited[i][j]:
            return
        letter = board[i][j]
        if letter not in trieNode:
            return

        trieNode = trieNode[letter]
        visited[i][j] = True
        if '*' in trieNode:
            finalWords[trieNode['*']] = True

        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            x_1, y_1 = i + x, j + y
            if self.isValid(x_1, y_1, r, c):
                self.dfs(x_1, y_1, board, visited, trieNode, finalWords, r, c)

        visited[i][j] = False

    def isValid(self, i, j, r, c):
        return 0 <= i < r and 0 <= j < c


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = '*'

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word


if __name__ == "__main__":
    s = Solution()
    print(s.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                      ["oath", "pea", "eat", "rain"]))

    print(s.findWords([["a", "a"]], ["aaa"]))
