#!/usr/bin/env python
# coding:utf-8
"""
@FileName : cheapest_flight_within_k_stops.py
@Author   : Harsh Parikh
@Date     : 8/30/21 2:12 AM

787. Cheapest Flights Within K Stops

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.



Example 1:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
"""


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        flights_graph = collections.defaultdict(list)

        for source, dest, cost in flights:
            flights_graph[source].append((dest, cost))

        def bfs(graph, city, stops):

            queue = collections.deque([(city, 0, stops + 1)])

            minimum_cost = float('inf')
            visited = {src: 0}

            while queue:
                city, curr_cost, stops = queue.popleft()

                if stops < 0:
                    continue

                if city == dst:
                    minimum_cost = min(curr_cost, minimum_cost)

                for neigh, neigh_cost in graph[city]:
                    if (neigh not in visited) or \
                            (neigh in visited and visited[neigh] > (curr_cost + neigh_cost)):
                        visited[neigh] = curr_cost + neigh_cost
                        queue.append((neigh, curr_cost + neigh_cost, stops - 1))

            return -1 if minimum_cost == float('inf') else minimum_cost

        return bfs(flights_graph, src, k)

    # Dijkstra
    def findCheapestPrice1(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = collections.defaultdict(list)

        for source, dest, cost in flights:
            graph[source].append((dest, cost))

        visited = [0] * n
        heap = [(0, src, k + 1)]

        while heap:
            cost, city, stops = heapq.heappop(heap)

            if city == dst:
                return cost
            """
            Prevent unnecessary exploration of certain nodes, 
            by keeping tracking of how many stops it took to reach that node when it was visited earlier. 
            On subsequent visits, if number of steps it took to reach the node previously, 
            was lesser than the current visit, we can safely ignore the current visit.

For. e.g if Node_5 was visited earlier (it means that a previous path to Node_5 cost lesser than the current path), and we stored the number of stops it took to reach Node_5 as 7. Now, say we are have popped Node_5 again, (remember, this path is costlier), and consider two cases:
a) Number of steps is 15 (greater than 7), so there's no point exploring this further (why? We have already explored a cheaper path that took less steps)
b) Number of steps is 4 (less than 7), so there is a possibility that this path could lead us to solution (why? The earlier path may have been cheaper, but eventually may have have taken longer steps, and hence been invalid)
            """
            if visited[city] >= stops:
                continue

            visited[city] = stops

            for neigh, neigh_cost in graph[city]:
                heapq.heappush(heap, (cost + neigh_cost, neigh, stops - 1))

        return -1

