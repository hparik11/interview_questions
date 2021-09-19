# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: course_schedule_II.py
# @Date:   9/24/20, Thu
"""
210. Course Schedule II

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

from collections import defaultdict


class Graph:
    def __init__(self):
        self.adjacency_matrix = defaultdict(list)

    def add_edge(self, u, v):
        self.adjacency_matrix[u].append(v)


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = Graph()

        for each in prerequisites:
            graph.add_edge(each[0], each[1])

        def dfs(adjacency_matrix, visited, visiting, course, order_of_courses):
            if course in visited:
                return True

            if course in visiting:
                return False

            visiting[course] = True

            for prereq in adjacency_matrix[course]:
                if not dfs(adjacency_matrix, visited, visiting, prereq, order_of_courses):
                    return False

            visited[course] = True
            visiting[course] = False

            order_of_courses.append(course)

            return True

        visited = {}
        visiting = {}
        order_of_courses = []

        for course in range(numCourses):
            if not dfs(graph.adjacency_matrix, visited, visiting, course, order_of_courses):
                return []

        return order_of_courses


if __name__ == '__main__':
    s = Solution()
    print(s.findOrder(2, [[1, 0]]))
    print(s.findOrder(2, [[1, 0],[0,1]]))
    print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(s.findOrder(1, []))
    print(s.findOrder(2, []))
