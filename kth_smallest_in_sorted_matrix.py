#!/usr/bin/env python
# coding:utf-8
"""
@FileName : kth_smallest_in_sorted_matrix.py
@Author   : Harsh Parikh
@Date     : 9/12/21 4:02 PM

378. Kth Smallest Element in a Sorted Matrix
Medium

4608

208

Add to List

Share
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.



Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
"""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        result, heap = None, []
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        added = set()

        while k > 0 and heap:
            result, i, j = heapq.heappop(heap)

            if j < len(matrix) - 1 and (i, j + 1) not in added:
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
                added.add((i, j + 1))

            if i < len(matrix) - 1 and (i + 1, j) not in added:
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
                added.add((i + 1, j))

            k -= 1

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
