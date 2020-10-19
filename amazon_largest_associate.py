# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: amazon_largest_associate.py
# @Date:   9/9/20, Wed

"""
https://leetcode.com/discuss/interview-question/782606/
"""
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        if v is None:
            self.graph[u] = []
        else:
            self.graph[u].append(v)
            self.graph[v].append(u)


class Solution:
    def largest_item_association(self, item_association):

        def dfs(node, graph, curr_group, visited):
            if node in visited:
                return
            visited[node] = True

            for neigh in graph[node]:
                if neigh not in visited:
                    curr_group.append(neigh)
                    dfs(neigh, graph, curr_group, visited)

        graph = Graph()
        for each in item_association:
            if len(each) == 1:
                graph.add_edge(each[0], None)
            else:
                graph.add_edge(each[0], each[1])

        graphDict = graph.graph

        visited = defaultdict(bool)
        largest_group = []

        for each in graph.graph:
            curr_group = []
            if each not in visited:
                curr_group.append(each)
                dfs(each, graphDict, curr_group, visited)

                if len(curr_group) > len(largest_group):
                    largest_group = sorted(curr_group)
                elif len(curr_group) == len(largest_group):
                    if sorted(curr_group)[0] < sorted(largest_group)[0]:
                        largest_group = sorted(curr_group)

        return largest_group


if __name__ == '__main__':
    s = Solution()

    print(s.largest_item_association([['item1', 'item2'], ['item3', 'item4'], ['item4', 'item5']]) == ["item3", "item4",
                                                                                                       "item5"])
    print(
        s.largest_item_association([['item1', 'item2'], ['item2', 'item5'], ['item3']]) == ['item1', 'item2', 'item5'])
    print(s.largest_item_association(
        [['item1', 'item2'], ['item2', 'item3'], ['item4', 'item5'], ['item5', 'item6']]) == ['item1', 'item2',
                                                                                              'item3'])
    print(s.largest_item_association([['A', 'B'], ['D', 'E'], ['C', 'D']]) == ['C', 'D', 'E'])
    print(s.largest_item_association([['A', 'B'], ['C', 'D'], ['F', 'E']]) == ['A', 'B'])
    print(s.largest_item_association([['A', 'B'], ['C', 'D'], ['D', 'E'], ['F', 'E']]) == ['C', 'D', 'E', 'F'])
    print(
        s.largest_item_association([['A', 'B'], ['C', 'D'], ['D', 'E'], ['F', 'E'], ['A', 'C']]) == ['A', 'B', 'C', 'D',
                                                                                                     'E', 'F'])
    print(s.largest_item_association([['A', 'B'], ['F', 'E'], ['G', 'K'], ['C', 'D'], ['D', 'E'],
                                      ['X', 'G'], ['X', 'N'], ['K', 'L'], ['L', 'M'], ['F', 'E'],
                                      ['A', 'C'], ]) == ['A', 'B', 'C', 'D', 'E', 'F'])
    print(s.largest_item_association([['item1', 'item2'], ['item3', 'item4'], ['item4', 'item5']]) == ['item3', 'item4',
                                                                                                       'item5'])
    print(
        s.largest_item_association([['item1', 'item2'], ['item2', 'item5'], ['item3']]) == ['item1', 'item2', 'item5'])
    print(s.largest_item_association(
        [['item1', 'item2'], ['item2', 'item3'], ['item4', 'item5'], ['item5', 'item6']]) == ['item1', 'item2',
                                                                                              'item3'])
    print(s.largest_item_association(
        [["item1", "item2"], ["item1", "item3"], ["item2", "item7"], ["item3", "item7"], ["item5", "item6"],
         ["item3", "item7"]]) == ['item1', 'item2', 'item3', 'item7'])
