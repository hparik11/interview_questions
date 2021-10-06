"""
332. Reconstruct Itinerary

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.



Example 1:


Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
Example 2:


Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
"""

import heapq
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets):
        # edge cases
        if not tickets:
            return []

        # if there is only 1 ticket in the itinerary
        if len(tickets) == 1:
            return tickets[0]

        # adjacency "list" will be maintained as a MIN heap
        # since we want the lexically smaller destinations to be on top
        # i.e., to be popped first
        adj = defaultdict(list)
        for orig, dest in tickets:
            heapq.heappush(adj[orig], dest)

        stack = ['JFK']

        result = []

        while stack:
            # analyze top of stack
            orig = stack[-1]

            # if destination list from current origin
            # is empty, then add that origin to the result list
            if not adj[orig]:
                result.append(orig)
                # pop out that origin from the list
                # since all its destinations have been processed
                stack.pop()
            else:
                # pop the top destination on the MIN heap
                dest = heapq.heappop(adj[orig])
                # add it to be the next in line to be processed
                stack.append(dest)

                # because of the DFS-style (with stack),
        # JFK is processed last
        # hence, reverse the order
        return result[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
