# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: amazon_merge_intervals.py
# @Date:   9/24/20, Thu

"""
56. Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) <= 1:
            return intervals
        intervals = sorted(intervals)

        results = []

        start = -1
        end = -1

        for each in intervals:
            currStart = each[0]
            currEnd = each[1]

            if start == -1 or end == -1:
                start = currStart
                end = currEnd
            elif end >= currStart:
                end = max(end, currEnd)
                start = min(start, currStart)
            else:
                results.append([start, end])
                start = currStart
                end = currEnd

        results.append([start, end])

        return results


if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
