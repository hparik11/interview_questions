#!/usr/bin/env python
# coding:utf-8
"""
@FileName : evaluate_division.py
@Author   : Harsh Parikh
@Date     : 9/11/21 1:50 PM

399. Evaluate Division
Medium

3985

320

Add to List

Share
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.



Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
"""

from typing import List
from collections import deque
from collections import defaultdict

"""
O(NM), where N is the number of equations (edges in a graph) and M is the number of queries:
"""


class Solution:
    def calcEquation_bfs(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(defaultdict)

        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        def backtracking(graph, visited, dividend, divisor):

            queue = deque([(dividend, 1)])

            while queue:
                curr_node, curr_product = queue.popleft()
                # print(curr_node, curr_product)
                visited.add(curr_node)

                for each in graph[curr_node]:
                    if each in visited:
                        continue

                    if each == divisor:
                        return curr_product * graph[curr_node][each]

                    queue.append((each, curr_product * graph[curr_node][each]))

            return -1

        results = []
        for query in queries:
            visited = set()
            dividend, divisor = query[0], query[1]
            if dividend not in graph or divisor not in graph:
                results.append(-1)
            elif dividend == divisor:
                results.append(1)
            else:
                results.append(backtracking(graph, visited, dividend, divisor))

        return results

    def calcEquation_dfs(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(set)

        for (dividend, divisor), value in zip(equations, values):
            graph[dividend].add((divisor, value))
            graph[divisor].add((dividend, 1 / value))

        def dfs(graph, visited, dividend, divisor):
            if dividend == divisor and graph[dividend]:
                return 1.0

            visited.add(dividend)

            for neigh, val in graph[dividend]:
                if neigh in visited:
                    continue

                tmp = dfs(graph, visited, neigh, divisor)
                if tmp > 0:
                    return val * tmp

            return -1.0

        results = []
        for query in queries:
            visited = set()
            dividend, divisor = query[0], query[1]
            if dividend not in graph or divisor not in graph:
                results.append(-1)
            elif dividend == divisor:
                results.append(1)
            else:
                results.append(dfs(graph, visited, dividend, divisor))

        return results


if __name__ == '__main__':
    s = Solution()
    print(s.calcEquation_bfs([["a", "b"], ["b", "c"]],
                             [2.0, 3.0],
                             [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
