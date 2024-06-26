"""
973. K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

"""
from typing import List


class Solution:
    def euclidean_distance(self, x, y):
        return math.sqrt((x) ** 2 + (y) ** 2)

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        #         heap = []
        #         for each in points:
        #             # print(each)
        #             if len(heap) == K:
        #                 heapq.heappushpop(heap, (-1.0 * self.euclidean_distance(each[0], each[1]), each[0], each[1]))
        #             else:
        #                 heapq.heappush(heap, (-1.0 * self.euclidean_distance(each[0], each[1]), each[0], each[1]))

        #             # print(heap)

        #         # print(heap)
        #         return [(x,y) for (dist,x, y) in heap]

        if K >= len(points):
            return points

        return sorted(points, key=lambda i: self.euclidean_distance(i[0], i[1]))[:K]
