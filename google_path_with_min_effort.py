"""
1631. Path With Minimum Effort

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.



Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells,
which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
"""

import heapq
import math


# Time Complexity : O(m⋅n(log(m⋅n))) | Dijkstra
class Solution:
    def minimumEffortPath(self, heights) -> int:

        def is_inbound(r, c, rows, cols):
            return 0 <= r < rows and 0 <= c < cols

        m, n = len(heights), len(heights[0])

        efforts = [[math.inf] * n for _ in range(m)]

        efforts[0][0] = 0
        heap = [(0, 0, 0)]

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while heap:
            effort, x, y = heapq.heappop(heap)
            if (x, y) == (m - 1, n - 1):
                return effort

            for dir_x, dir_y in directions:
                new_x = x + dir_x
                new_y = y + dir_y

                if is_inbound(new_x, new_y, m, n):

                    next_effort = max(effort, abs(heights[new_x][new_y] - heights[x][y]))

                    if efforts[new_x][new_y] > next_effort:
                        efforts[new_x][new_y] = next_effort
                        heapq.heappush(heap, (next_effort, new_x, new_y))

    # O(log(10^6 * m*n) = O(m*n)
    def minimumEffortPath1(self, heights) -> int:
        row = len(heights)
        col = len(heights[0])

        def canReachDestinaton(mid):
            visited = [[False] * col for _ in range(row)]
            queue = [(0, 0)]  # x, y
            while queue:
                x, y = queue.pop(0)
                if x == row - 1 and y == col - 1:
                    return True
                visited[x][y] = True
                for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    adjacent_x = x + dx
                    adjacent_y = y + dy
                    if 0 <= adjacent_x < row and 0 <= adjacent_y < col and not visited[adjacent_x][adjacent_y]:
                        current_difference = abs(
                            heights[adjacent_x][adjacent_y] - heights[x][y])
                        if current_difference <= mid:
                            visited[adjacent_x][adjacent_y] = True
                            queue.append((adjacent_x, adjacent_y))

        left = 0
        right = 10000000
        while left < right:
            mid = (left + right) // 2
            if canReachDestinaton(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
