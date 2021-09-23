#!/usr/bin/env python
# coding:utf-8
"""
@FileName : uber_minesweeper.py
@Author   : Harsh Parikh
@Date     : 8/20/21 11:47 PM

529. Minesweeper

Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.


Example 1:


Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
Example 2:


Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

"""


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        R, C = len(board), len(board[0])
        r, c = click

        directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        visited = set()

        def valid(r, c):
            return 0 <= r < R and 0 <= c < C

        def get_adjacent_mines(r, c):
            mine_count = 0
            for dr, dc in directions:
                if valid(r + dr, c + dc) and board[r + dr][c + dc] == 'M':
                    mine_count += 1
            return mine_count

        def bfs(r, c):
            queue = collections.deque([(r, c)])
            while queue:
                r, c = queue.popleft()
                visited.add((r, c))
                if not valid(r, c) or board[r][c] != 'E':
                    continue

                mine_count = get_adjacent_mines(r, c)
                if mine_count > 0:
                    board[r][c] = str(mine_count)
                else:
                    board[r][c] = 'B'
                    for dr, dc in directions:
                        if (r + dr, c + dc) not in visited:
                            queue.append((r + dr, c + dc))

        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        bfs(r, c)

        return board


if __name__ == '__main__':
    s = Solution()
    print(s.updateBoard(
        [["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"], ["E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E"]],
        [3, 0]))
