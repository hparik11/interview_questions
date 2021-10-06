#!/usr/bin/env python
# coding:utf-8
"""
@FileName : uber_bus_stops.py
@Author   : Harsh Parikh
@Date     : 8/22/21 2:56 AM

815. Bus Routes

You are given an array routes representing bus routes where routes[i] is a
bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels
 in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially),
and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target.
Return -1 if it is not possible.



Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
"""

from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Base case
        if source == target:
            return 0

        # Creating graph or routes
        graph = defaultdict(set)

        # Since index represents bus_number on a route
        # suppose i is bus number and stops are the values present at that index
        for bus_number, stops in enumerate(routes):
            # for each stop adding buses going to that stop
            for stop in stops:
                graph[stop].add(bus_number)

        # Using bfs
        bfs = deque([(source, 0)])

        # visited stops
        seen_stops = set()
        # visited buses
        seen_buses = set()

        while bfs:
            stop, count = bfs.popleft()
            # Resulting case
            if stop == target:
                return count

            # Since our graph stores all buses going to a stop
            # We will iterate for every bus
            for bus_number in graph[stop]:
                # We dont want to travel in same bus as we might stuck into loop and reach nowhere
                if bus_number not in seen_buses:
                    seen_buses.add(bus_number)

                    # Now we are in a bus, so we will travel all
                    # the stops that bus goes to but again,
                    # we only want to go to stops we haven't visited
                    for stop in routes[bus_number]:
                        if stop not in seen_stops:
                            seen_stops.add(stop)
                            bfs.append((stop, count + 1))
        return -1
