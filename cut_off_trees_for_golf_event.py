#!/usr/bin/env python
# coding:utf-8
"""
@FileName : cut_off_trees_for_golf_event.py
@Author   : Harsh Parikh
@Date     : 8/6/21 11:22 PM

675. Cut Off Trees for Golf Event
You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:

0 means the cell cannot be walked through.
1 represents an empty cell that can be walked through.
A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.
In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.

You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).

Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.

You are guaranteed that no two trees have the same height, and there is at least one tree needs to be cut off.



Example 1:


Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
Output: 6
Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
Example 2:


Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
Output: -1
Explanation: The trees in the bottom row cannot be accessed as the middle row is blocked.
Example 3:

Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
Output: 6
Explanation: You can follow the same path as Example 1 to cut off all the trees.
Note that you can cut off the first tree at (0, 0) before making any steps.
"""

from typing import List
import heapq
import collections


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # print("forest at start: \n{}".format(np.array(forest)))
        m = len(forest)
        n = len(forest[0])

        # store all trees in priority queue in (height,x,y) format
        pq = []
        for x in range(m):
            for y in range(n):
                height = forest[x][y]
                if height > 1:
                    heapq.heappush(pq, (height, x, y))

        # print("heap: {}".format(pq))

        # takes in starting position and next tree position, returns min steps to get to that next tree position
        def bfs(x, y, nextX, nextY) -> int:
            queue = collections.deque([(x, y, 0)])
            seen = {(x, y)}
            # print("starting at: ({},{})".format(x,y))
            # keep BFS searching until we find target tree or tried all paths
            while queue:
                x, y, steps = queue.popleft()

                if x == nextX and y == nextY:
                    # found the next tree, chop it down and return depth
                    forest[x][y] = 1
                    # print("ending at: ({},{}) after {} steps".format(x,y,steps))
                    return steps

                # append adjacent nodes (if they are a valid position i.e. height >= 1, within bounds of forest, and not already used)
                for dx, dy in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                    adjX, adjY = x + dx, y + dy
                    if (0 <= adjX < m and 0 <= adjY < n) and (forest[adjX][adjY] >= 1) and ((adjX, adjY) not in seen):
                        queue.append((adjX, adjY, steps + 1))
                        seen.add((adjX, adjY))

            # no such path exists
            return -1

        # start from 0,0 and have next be the first smallest tree, and use BFS for the others
        x, y = 0, 0
        steps = 0
        # while there are still trees to cut
        while pq:
            _, nextX, nextY = heapq.heappop(pq)

            # find the shortest path to the next tree
            shortestPath = bfs(x, y, nextX, nextY)
            if shortestPath == -1:
                return -1
            steps += shortestPath
            x, y = nextX, nextY

        # print("forest at end: \n{}".format(np.array(forest)))
        return steps


if __name__ == '__main__':
    s = Solution()
    print(s.cutOffTree([[2, 3, 4], [0, 0, 5], [8, 7, 6]]))
