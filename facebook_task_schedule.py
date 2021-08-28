#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_task_schedule.py
@Author   : Harsh Parikh
@Date     : 7/22/21 4:01 PM

621. Task Scheduler
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.



Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
"""

from collections import Counter
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        """
        The first thing you should be worried about is that no two same tasks can be within n distance of each other.

        The second thing is the ordering of these tasks. Naturally, if I have lesser unique tasks,
        I'll be worried about processor staying IDLE, which is bad.
        In other words I have to be concerned about tasks with higher frequencies.
        This makes it a perfect candidate for a Priority Queue, or a Max-Heap.

        """
        if n == 0:
            return len(tasks)

        tasksMap = Counter(tasks)

        q = []

        for task in tasksMap:
            heapq.heappush(q, (-1 * tasksMap[task], task))

        count = 0
        while q:
            k = n + 1
            temp = []
            while k > 0 and len(q) > 0:
                # len(q) actually represents the number of unique tasks
                # so we are checking either we run out of k, or num of unique tasks
                task = heapq.heappop(q)
                # print("EXEC " + task[1])
                temp.append((-1 * task[0], task[1]))
                k -= 1
                count += 1

            # print("temp = {}".format(temp))
            for task in temp:
                if task[0] > 1:
                    # decrease the frequency by 1
                    new_frequency = task[0] - 1
                    heapq.heappush(q, (-1 * new_frequency, task[1]))

            if len(q) == 0:
                break

            count += k  # if k > 0, then it means we need to be idle

        return count


if __name__ == '__main__':
    s = Solution()
    print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
