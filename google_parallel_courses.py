#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_parallel_courses.py
@Author   : Harsh Parikh
@Date     : 10/4/21 12:08 PM

1136. Parallel Courses

You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.

In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.



Example 1:


Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 1 and 2.
In the second semester, you can take course 3.
Example 2:


Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: No course can be studied because they are prerequisites of each other.
"""

import collections


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        in_degree = {i: 0 for i in range(1, n + 1)}  # or in-degree

        for start_node, end_node in relations:
            graph[start_node].append(end_node)
            in_degree[end_node] += 1

        queue = collections.deque()
        # we use list here since we are not
        # popping from front the this code
        for node in graph:
            if in_degree[node] == 0:
                queue.append(node)

        step = 0
        studied_count = 0
        # start learning with BFS
        while queue:
            # start new semester
            step += 1
            total_elems = len(queue)

            for _ in range(total_elems):
                node = queue.popleft()
                studied_count += 1
                end_nodes = graph[node]
                for end_node in end_nodes:
                    in_degree[end_node] -= 1
                    # if all prerequisite courses learned
                    if in_degree[end_node] == 0:
                        queue.append(end_node)

        return step if studied_count == n else -1
