# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: meeting_schedular.py
# @Date:   9/21/20, Mon
"""
1229. Meeting Scheduler

Given the availability time slots arrays slots1 and slots2 of
two people and a meeting duration duration,
return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end]
representing an inclusive time range from start to end.

It is guaranteed that no two availability slots of the same person
intersect with each other. That is, for any two time slots [start1, end1]
and [start2, end2] of the same person, either start1 > end2 or start2 > end1.



Example 1:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]
Example 2:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []
"""
from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        if not slots1 or not slots2:
            return []
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        i = 0
        j = 0

        while i < len(slots1) and j < len(slots2):
            start1 = slots1[i][0]
            end1 = slots1[i][1]

            start2 = slots2[j][0]
            end2 = slots2[j][1]

            if min(end1, end2) - max(start1, start2) >= duration:
                return [max(start1, start2), max(start1, start2) + duration]
            else:
                if start1 < start2:
                    i += 1
                elif start2 < start1:
                    j += 1
                else:
                    i += 1
                    j += 1
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.minAvailableDuration([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8))
    print(s.minAvailableDuration([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12))
