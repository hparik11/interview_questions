#!/usr/bin/env python
# coding:utf-8
"""
@FileName : shortest_distance_from_all_buildings.py
@Author   : Harsh Parikh
@Date     : 8/23/21 12:24 AM

317. Shortest Distance from All Buildings

You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.



Example 1:


Input: grid = [ [1,0,2,0,1],
                [0,0,0,0,0],
                [0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.
Example 2:

Input: grid = [[1,0]]
Output: 1
Example 3:

Input: grid = [[1]]
Output: -1
"""


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return -1

        num_rows, num_cols, buildings = len(grid), len(grid[0]), sum(val for line in grid for val in line if val == 1)

        buildings_reached, distSum = [[0] * num_cols for _ in range(num_rows)], [[0] * num_cols for _ in range(num_rows)]

        def BFS(start_x, start_y):
            visited = [[False] * num_cols for _ in range(num_rows)]
            visited[start_x][start_y] = True
            count1 = 1
            queue = collections.deque([(start_x, start_y, 0)])

            while queue:
                x, y, dist = queue.popleft()
                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= i < num_rows and 0 <= j < num_cols and not visited[i][j]:
                        visited[i][j] = True
                        if not grid[i][j]:
                            queue.append((i, j, dist + 1))
                            buildings_reached[i][j] += 1
                            distSum[i][j] += dist + 1
                        elif grid[i][j] == 1:
                            count1 += 1

            return count1 == buildings

        for x in range(num_rows):
            for y in range(num_cols):
                if grid[x][y] == 1:
                    if not BFS(x, y):
                        return -1

        return min([distSum[i][j] for i in range(num_rows) for j in range(num_cols) if
                    not grid[i][j] and buildings_reached[i][j] == buildings] or [-1])
