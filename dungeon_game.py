#!/usr/bin/env python
# coding:utf-8
"""
@FileName : dungeon_game.py
@Author   : Harsh Parikh
@Date     : 7/22/21 12:04 AM

174. Dungeon Game

The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.



Example 1:


Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
Example 2:

Input: dungeon = [[0]]
Output: 1

"""

from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        n = len(dungeon)
        m = len(dungeon[0])

        INF = float("inf")

        dp = [[INF for i in range(m + 1)] for j in range(n + 1)]

        def dfs(i, j):
            """
            Base case : we have crossed the matrix, ie. out of bound
            if current row crosses then my row is below the princess or
            if current column crosses then my column is ahead the column of princess
            and beacause we can go only down and right so we wont be able reach princess

            Base Case : we have reached our destination ie. last cell
            we reached princess , cheers return this cost;
            """

            if (i, j) == (n - 1, m - 1):
                if dungeon[i][j] > 0:
                    return 1
                else:
                    return 1 - dungeon[i][j]

            if i > (n - 1) or j > (m - 1):
                return INF

            if dp[i][j] != INF:
                return dp[i][j]

            downPathHealth = dfs(i + 1, j)
            rightPathHealth = dfs(i, j + 1)

            # min of either values and then cost of this cell
            minHealthRequired = min(downPathHealth, rightPathHealth) - dungeon[i][j]

            """
            before returning the values, we must store the answers for this cell which we hacve calculated
            in next recursive call this value will be used to save some computation, 
            aka repetitive work which we are doing.
            """
            dp[i][j] = max(1, minHealthRequired)

            return dp[i][j]

        return dfs(0, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
