# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: amamzon_analyze_user_website_visit_pattern.py
# @Date:   10/18/20, Sun
"""
1152. Analyze User Website Visit Pattern

We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.)

Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.



Example 1:

Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation:
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.
"""

import heapq
from collections import defaultdict
from itertools import combinations
from typing import List


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        heap = []
        for i in range(len(timestamp)):
            heapq.heappush(heap, (timestamp[i], website[i], username[i]))

        users = defaultdict(list)

        while heap:
            timeStamp, webSite, userName = heapq.heappop(heap)
            users[userName].append(webSite)

        count = defaultdict(int)
        maximum = 0
        result = tuple()

        for key in users:
            combos = combinations(users[key], 3)
            for sequence in set(combos):
                count[sequence] += 1
                if count[sequence] > maximum:
                    maximum = count[sequence]
                    result = sequence
                elif count[sequence] == maximum:
                    if sequence < result:
                        result = sequence

        return list(result)


if __name__ == '__main__':
    s = Solution()
    print(s.mostVisitedPattern(["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
                               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                               ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]))
