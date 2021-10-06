#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_merge_interval_with_labels.py
@Author   : Harsh Parikh
@Date     : 10/5/21 3:46 PM

Google | Onsite | Merge Intervals With Labels


Given a set of inputs which represents [from, to, comment] in google docs.
Transform the input with overlapping offsets & unique comments to non overlapping offsets and duplicate comments.

Example 1:

Input:
(0, 3): A
(2, 4): B
(5, 6): C

Output:
(0, 2): [A]
(2, 3): [A, B]
(3, 4): [B]
(5, 6): [C]
Example 2:

Input:
(0, 3): A
(0, 3): B
(2, 4): C
(5, 6): D

Output:
(0, 2): [A, B]
(2, 3): [A, B, C]
(3, 4): [C]
(5, 6): [D]
"""


def mergeIntervalsLabeled2(intervals):
    events = []

    for st, end, label in intervals:
        events.append((st, 1, label))
        events.append((end, 0, label))

    activeSet = set()
    events.sort()
    output = []
    prevX = None

    for x, isStart, label in events:
        if prevX is not None and prevX != x and activeSet:
            output.append((prevX, x, list(activeSet)))

        if isStart:
            activeSet.add(label)
        else:
            activeSet.remove(label)

        prevX = x

    return output


if __name__ == '__main__':
    print(mergeIntervalsLabeled2([[0, 3, 'A'], [2, 4, 'B'], [5, 6, 'C']]))
