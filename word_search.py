"""
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of the sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

from typing import List


class Solution(object):
    def checkValid(self, row, col):
        if row < 0 or row >= self.row or col < 0 or col >= self.col:
            return False
        return True

    def checkChars(self, board, row, col, word, index):
        if index == len(word):
            return True
        for m, n in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            x = row + m
            y = col + n

            if self.checkValid(x, y) and board[x][y] == word[index] and self.visited[x][y] is False:
                self.visited[x][y] = True
                index += 1
                if self.checkChars(board, x, y, word, index):
                    return True
                self.visited[x][y] = False
                index -= 1

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        print(board, word)
        row = len(board)
        col = len(board[0])

        self.row = row
        self.col = col

        print(row, col)

        if not row or not col:
            return False

        self.visited = [[False for _ in range(col)] for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    # print(i, j)
                    self.visited[i][j] = True
                    # print(self.visited[i][j])
                    if self.checkChars(board, i, j, word, 1):
                        # print("Here")
                        return True

                    self.visited[i][j] = False
        print(self.visited)
        return False


if __name__ == "__main__":
    s = Solution()
    # print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    print(s.exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"))
