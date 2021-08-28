# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: meeting_rooms.py
# @Date:   10/14/20, Wed
"""
Meeting Rooms

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
"""

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 1:
            return True
        sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        start, end = sorted_intervals[0][0], sorted_intervals[0][1]
        for index in range(1, len(sorted_intervals)):
            currStart, currEnd = sorted_intervals[index][0], sorted_intervals[index][1]
            if end > currStart:
                return False

            start, end = currStart, currEnd

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
