#!/usr/bin/env python
# coding:utf-8
"""
@FileName : the_maze.py
@Author   : Harsh Parikh
@Date     : 7/3/21 8:14 PM

490. The Maze
https://leetcode.com/problems/the-maze/

There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).


Example 1:


Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
start = [0,4], destination = [4,4]
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
Example 2:


Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: false
Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.
Example 3:

Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
Output: false
"""

from collections import deque


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        def is_valid(i, j, row, col):
            return 0 <= i < row and 0 <= j < col

        Q = deque([start])
        n = len(maze)
        m = len(maze[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while Q:
            i, j = Q.popleft()

            if maze[i][j] == 0:
                maze[i][j] = 2

                if destination == [i, j]:
                    return True

                for x, y in directions:
                    row = i + x
                    col = j + y

                    while is_valid(row, col, n, m) and maze[row][col] != 1:
                        row += x
                        col += y

                    row -= x
                    col -= y

                    if maze[row][col] == 0:
                        Q.append([row, col])

        return False

