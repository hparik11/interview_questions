# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: meeting_rooms_II.py
# @Date:   10/16/20, Fri
"""
253. Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
 find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""

from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        active_slots = 0
        meeting_queue = []
        intervals = sorted(intervals)
        for meeting in intervals:
            if len(meeting_queue) == 0:
                heapq.heappush(meeting_queue, meeting[1])
                active_slots += 1
            else:
                min_meeting = heapq.heappop(meeting_queue)
                # if the earliest end time is still greater than current meeting's start time,
                if min_meeting > meeting[0]:
                    active_slots += 1
                    heapq.heappush(meeting_queue, meeting[1])
                    heapq.heappush(meeting_queue, min_meeting)
                else:
                    heapq.heappush(meeting_queue, meeting[1])

        return active_slots


if __name__ == '__main__':
    s = Solution()
    print(s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
    print(s.minMeetingRooms([[1, 8], [8, 9], [8, 9]]))
    print(s.minMeetingRooms([[2, 15], [36, 45], [9, 29], [16, 23], [4, 9]]))
