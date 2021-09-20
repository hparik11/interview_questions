"""
261. Graph Valid Tree

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

Example 1:

Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
"""


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = list(range(n))
        self.ranks = [0 for _ in range(n)]

    def find(self, u):

        while self.parents[u] != u:
            u = self.parents[u]

        return u

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.ranks[root_v] < self.ranks[root_u]:
            self.parents[root_v] = root_u
            self.ranks[root_u] += 1
        else:
            self.parents[root_u] = root_v
            self.ranks[root_v] += 1

        return True


from collections import defaultdict, deque


class Solution:
    """
    Complexity Analysis

    Let E be the number of edges, and N be the number of nodes.

    α(N) is the Inverse Ackermann Function.

    Time Complexity : O(N⋅α(N)).

    Space Complexity : O(N).

    """
    def validTree_unionfind(self, n: int, edges) -> bool:

        uf = UnionFind(n)

        for edge in edges:
            if not uf.union(*edge):
                return False

        return len(edges) == n - 1

    def validTree_bfs(self, n: int, edges) -> bool:

        graph = defaultdict(list)
        for edge in edges:
            u, v = edge[0], edge[1]
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        queue = deque([0])
        # initialize a parent list
        parent = defaultdict(int)

        while queue:
            v = queue.popleft()
            visited.add(v)
            for neighbor in graph[v]:
                if neighbor not in visited:
                    parent[neighbor] = v
                    queue.append(neighbor)
                elif neighbor != parent[v]:
                    return False

        # If the graph is connected then all vertices must be visited
        return len(visited) == n
