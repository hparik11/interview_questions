# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: boggle_board.py
# @Date:   8/13/20, Thu

"""

"""


class Trie:
    def __init__(self):
        self.wordDict = {}
        self.endCharacter = '*'

    def insert(self, word):
        root = self.wordDict
        for ch in word:
            if ch not in root:
                root[ch] = {}

            root = root[ch]

        root[self.endCharacter] = word


def is_within_boundary(i, j, row, col):
    return 0 <= i < row and 0 <= j < col


def dfs(board, i, j, row, col, wordDict, visited, final_words):
    if (i, j) in visited:
        return

    if board[i][j] not in wordDict:
        return

    wordDict = wordDict[board[i][j]]

    if '*' in wordDict:
        final_words.add(wordDict['*'])

    visited.add((i, j))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for each in directions:
        new_x, new_y = i + each[0], j + each[1]

        if is_within_boundary(new_x, new_y, row, col):
            dfs(board, new_x, new_y, row, col, wordDict, visited, final_words)

    visited.remove((i, j))


def boggleBoard(board, words):
    # Write your code here.

    trie = Trie()

    for word in set(words):
        trie.insert(word)

    rows = len(board)
    cols = len(board[0])
    final_words = set()
    visited = set()

    for i in range(rows):
        for j in range(cols):

            if board[i][j] in trie.wordDict:
                dfs(board, i, j, rows, cols, trie.wordDict, visited, final_words)

    print(list(final_words))
    return list(final_words)
