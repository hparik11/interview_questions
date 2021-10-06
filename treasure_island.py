# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: treasure_island.py
# @Date:   9/18/20, Fri

"""
https://leetcode.com/discuss/interview-question/347457/Amazon-or-OA-2019-or-Treasure-Island

You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

Example:

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
"""

from typing import List


class Solution:
    def treasureIsland(self, treasures: List[List[str]]) -> int:
        row = len(treasures)
        col = len(treasures[0])

        visited = {}
        steps = 0
        queue = [(0, 0)]
        while len(queue) > 0:
            for i in range(len(queue)):
                element = queue.pop()
                for x, y in self.get_neighbors(element[0], element[1], treasures, row, col, visited):

                    if treasures[x][y] == 'X':
                        return steps

                    queue.append((x, y))

            steps += 1

        return -1

    def get_neighbors(self, x, y, treasures, row, col, visited):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        neighbors = []
        visited[(x, y)] = True
        for each in directions:
            new_x, new_y = x + each[0], y + each[1]
            if self.is_valid(new_x, new_y, row, col) and (new_x, new_y) not in visited \
                    and treasures[new_x][new_y] != 'D':
                neighbors.append((new_x, new_y))

        return neighbors

    @staticmethod
    def is_valid(x, y, row, col):
        if x < 0 or x >= row or y < 0 or y > col:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.treasureIsland([['O', 'O', 'O', '0'],
                            ['D', 'D', 'O', 'O'],
                            ['O', 'O', 'O', 'O'],
                            ['X', 'O', 'O', 'O']]))
