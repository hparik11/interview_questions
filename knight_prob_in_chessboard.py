# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: knight_prob_in_chessboard.py
# @Date:   8/30/20, Sun
"""
Knight Probability in Chessboard

On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
"""

from copy import deepcopy


class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp = [[0 for _ in range(N)] for _ in range(N)]
        dp[r][c] = 1
        mem = [[0 for _ in range(N)] for _ in range(N)]
        directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

        def is_inside(x, y, row, col):
            return 0 <= x < row and 0 <= y < col

        for _ in range(K):
            for i in range(N):
                for j in range(N):
                    if dp[i][j] > 0:
                        for x, y in directions:
                            if is_inside(i + x, j + y, N, N):
                                mem[i + x][j + y] += 1 / 8 * dp[i][j]

            dp = deepcopy(mem)
            mem = [[0] * N for _ in range(N)]

        print(dp)

        res = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                res += dp[i][j]

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.knightProbability(3, 2, 0, 0))
