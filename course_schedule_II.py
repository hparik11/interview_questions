# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: course_schedule_II.py
# @Date:   9/24/20, Thu
"""
210. Course Schedule II
Medium

2708

143

Add to List

Share
There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
"""

from typing import List
import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        def add_edge(graph, u, v):
            graph[u].append(v)

        def dfs(node, graph, visited, visiting, stack):
            if visited[node]:
                return True
            if visiting[node]:
                return False

            visiting[node] = True

            for preq in graph[node]:
                if not dfs(preq, graph, visited, visiting, stack):
                    return False

            visited[node] = True
            visiting[node] = False
            stack.append(node)

            return True

        graph = collections.defaultdict(list)

        for each in prerequisites:
            add_edge(graph, each[0], each[1])

        visited = {i: False for i in range(numCourses)}
        visiting = {i: False for i in range(numCourses)}
        stack = []

        for key in range(numCourses):
            if not dfs(key, graph, visited, visiting, stack):
                return []

        return stack


if __name__ == '__main__':
    s = Solution()
    print(s.findOrder(2, [[1, 0]]))
    print(s.findOrder(2, [[1, 0],[0,1]]))
    print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(s.findOrder(1, []))
    print(s.findOrder(2, []))
