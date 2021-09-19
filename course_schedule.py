"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""
from collections import defaultdict

"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def add_edge(graph, u, v):
            graph[u].append(v)
        
        def dfs(node, graph, visited, visiting):
            if visited[node]:
                return True
            if visiting[node]:
                return False
            
            visiting[node] = True
            
            for preq in graph[node]:
                if not visited[preq]:
                    if not dfs(preq, graph, visited, visiting):
                        return False
            
            visited[node] = True
            visiting[node] = False
            
            return True
                    
        graph = collections.defaultdict(list)
        
        for each in prerequisites:
            add_edge(graph, each[0], each[1])
        
        visited = {i:False for i in range(numCourses)}
        visiting = {i:False for i in range(numCourses)}
        
        for key in list(graph):
            if not dfs(key, graph, visited, visiting):
                return False
        
        return True
"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses < 2 or len(prerequisites) == 0:
            return True

        self.graph = defaultdict(list)  # dictionary containing adjacency List

        for i, j in prerequisites:
            self.graph[i].append(j)

        print(self.graph)
        # visited set will track vertices seen while exploring the current vertex
        self.visited = [0 for _ in range(numCourses)]
        print(self.visited)

        # For every vertex that has not been explored, visit it
        for i in list(self.graph):
            if not self.dfs(i):
                return False

        # when all the vertices have been explored without cycles, we can return True
        return True

    def dfs(self, v):
        """
        if node v has not been visited, then mark it as 0.
        if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
        if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.
        """
        if self.visited[v] == -1:
            return False
        if self.visited[v] == 1:
            return True
        # mark the current vertex as visited
        self.visited[v] = -1

        for i in self.graph[v]:
            if not self.dfs(i):
                return False

        self.visited[v] = 1

        return True


if __name__ == '__main__':
    s = Solution()
    # print(s.canFinish(6, [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]))
    # print(s.canFinish(2, [[1, 0]]))
    # print(s.canFinish(2, [[1, 0], [0, 1]]))
    print(s.canFinish(3, [[1, 0], [2, 0]]))
