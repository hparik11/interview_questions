# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: all_paths_from_source_to_dest.py
# @Date:   9/21/20, Mon
"""
797. All Paths From Source to Target

Given a directed acyclic graph of N nodes. Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.


Constraints:

The number of nodes in the graph will be in the range [2, 15].
You can print different paths in any order, but you should keep the order of nodes inside one path.
"""

from typing import List


# Time = O(N * 2^N - 1) --> bcz there are total 2^n paths for any node
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        if not graph:
            return []
        path = [0]
        paths = []

        self.dfs(graph, 0, len(graph) - 1, path, paths)

        return paths

    def dfs(self, graph, node, target, path, paths):

        if node == target:
            paths.append(path)

        for each in graph[node]:
            self.dfs(graph, each, target, path + [each], paths)


class Solution1:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        stack = [(0, [0])]
        target = len(graph) - 1
        while stack:
            cur, route = stack.pop()
            if cur == target:
                result.append(route)
            else:
                for node in graph[cur]:
                    stack.append((node, route + [node]))
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
