# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: queue_reconstruction_by_height.py
# @Date:   8/8/20, Sat

"""
406. Queue Reconstruction by Height

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""
import heapq
from typing import List


class Person:
    def __init__(self, h, k):
        self.h = h
        self.k = k

    def __lt__(self, other):
        # if self.k == other.k:
        #     return self.h < other.h
        # elif self.h == other.h:
        #     return self.k < other.k
        # elif self.k < other.k:
        #     return self.k < other.k
        # else:
        #     return self.h < other.h

        if self.h == other.h:
            return self.k < other.k
        else:
            return self.h < other.h


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
        output = []
        for p in people:
            output.insert(p[1], p)
        return output


if __name__ == '__main__':
    s = Solution()
    print(s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2], [5, 1]]))
