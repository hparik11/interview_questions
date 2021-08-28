# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: find_winner_tic_tac
# @Date:   10/4/20, Sun
"""
Find Winner on a Tic Tac Toe Game

Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.



Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"
Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO "
"   "    "   "    "   "    "   "    "   "    "O  "
Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"
Example 4:

Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "

"""
from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        row = {}
        col = {}
        diag = {}
        reverse_diag = {}

        for index, move in enumerate(moves):
            r, c = move
            player = "A" if index % 2 == 0 else "B"

            if r in row:
                if player in row[r]:
                    row[r][player] += 1
                    if row[r][player] == 3:
                        return player
                else:
                    row[r][player] = 1
            else:
                row[r] = {player: 1}

            if c in col:
                if player in col[c]:
                    col[c][player] += 1
                    if col[c][player] == 3:
                        return player
                else:
                    col[c][player] = 1
            else:
                col[c] = {player: 1}

            if r == c:
                diag[r] = player
                cnt = 0
                for j in range(3):
                    if j in diag and diag[j] == player:
                        cnt += 1

                if cnt == 3:
                    return player

            if r == 3 - c - 1:
                reverse_diag[r] = player
                cnt = 0
                for j in range(3):
                    if j in reverse_diag and reverse_diag[j] == player:
                        cnt += 1

                if cnt == 3:
                    return player

        return "Pending" if len(moves) != 9 else "Draw"


if __name__ == '__main__':
    s = Solution()
    print(s.tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))
    print(s.tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))
    print(s.tictactoe([[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]))
    print(s.tictactoe([[0, 0], [1, 1]]))
