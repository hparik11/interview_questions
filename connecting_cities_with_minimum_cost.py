#!/usr/bin/env python
# coding:utf-8
"""
@FileName : connecting_cities_with_minimum_cost.py
@Author   : Harsh Parikh
@Date     : 8/9/21 4:14 PM

1135. Connecting Cities With Minimum Cost

There are n cities labeled from 1 to n. You are given the integer n and an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi.

Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1,

The cost is the sum of the connections' costs used.



Example 1:


Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: Choosing any 2 edges will connect all cities so we choose the minimum 2.
Example 2:


Input: n = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: There is no way to connect all cities even if all edges are used.
"""

from collections import defaultdict
from typing import List
import heapq

# O(ELogV)
"""
        Prim's Algorithm:
        1) Initialize a tree with a single vertex, chosen
        arbitrarily from the graph.
        2) Grow the tree by one edge: of the edges that
        connect the tree to vertices not yet in the tree,
        find the minimum-weight edge, and transfer it to the tree.
        3) Repeat step 2 (until all vertices are in the tree).
"""


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:

        adj_metrics = defaultdict(list)

        # Build the undirected graph:
        for city, neigh, cost in connections:
            adj_metrics[city].append((neigh, cost))
            adj_metrics[neigh].append((city, cost))

        # Creat our heap and add our starting cost and location (0 cost to start).
        # Run Prim's algo on a random node
        heap = [(0, 1)]

        seen = set()
        total_cost = 0

        while heap:
            cost, city = heapq.heappop(heap)
            # If we haven't visited the city yet.
            if city not in seen:
                # Add it to seen (we got here via the lowest cost path) and add the cost to our total.
                seen.add(city)
                total_cost += cost

                if len(seen) == n:
                    break
                # For the current nodes neighboring cities
                for nei, cst in adj_metrics[city]:
                    # Push the neis on the heap so we select the lowest cost nei next.
                    heapq.heappush(heap, (cst, nei))

        # Return our cost if we have visited all N nodes.
        # the design of prim's algo makes sure that resulting MST is acyclic inherently
        # becuase you only add an edge (or the cost of that edge) if you didn't see it before
        return total_cost if len(seen) == n else -1


"""
Kruskal's Algorithm:
        1) Create a forest F (a set of trees), where each vertex in 
        the graph is a separate tree.
        2) Create a set S containing all the edges in the graph.
        3) While S is nonempty and F is not yet spanning (fully connected):
            3A) Remove an edge with minimum weight from S
            3B) If the removed edge connects two different trees then 
            add it to the forest F, combining two trees into a single tree.
"""


class Solution1:
    # O(ElogE + E) where "ElogE" is the time it takes to sort all
    # the edges to non-decreasing order, and "E" is the time it takes to form the MST with union find.
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:

        connections.sort(key=lambda x: x[2])

        uf = UnionFind(n)
        i = 0
        total_cost = 0
        total_connections = 0

        while i < len(connections):
            city = connections[i][0]
            neigh = connections[i][1]
            cost = connections[i][2]

            if uf.union(city, neigh):
                total_cost += cost
                total_connections += 1

            i += 1

        # Can connect n nodes (without cycles) iff there are n-1 valid edges
        return total_cost if total_connections == n - 1 else -1


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n + 1))
        self.rank = [0 for _ in range(n + 1)]

    def find(self, a):
        while self.parents[a] != a:
            a = self.parents[a]

        return a

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)

        if parent_a == parent_b:
            return False

        elif self.rank[parent_a] < self.rank[parent_b]:
            self.parents[parent_a] = parent_b
            self.rank[parent_b] += 1
        else:
            self.parents[parent_b] = parent_a
            self.rank[parent_a] += 1

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.minimumCost(3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]]))
