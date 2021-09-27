# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: consecutive_pattern.py
# @Date:   8/29/20, Sat

"""
5499. Detect Pattern of Length M Repeated K or More Times

Given an array of positive integers arr,  find a pattern of length m that is repeated k or more times.

A pattern is a subarray (consecutive sub-sequence) that consists of one or more values,
repeated multiple times consecutively without overlapping. A pattern is defined by its length and the number of repetitions.

Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false.



Example 1:

Input: arr = [1,2,4,4,4,4], m = 1, k = 3
Output: true
Explanation: The pattern (4) of length 1 is repeated 4 consecutive times. Notice that pattern can be repeated k or more times but not less.
Example 2:

Input: arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
Output: true
Explanation: The pattern (1,2) of length 2 is repeated 2 consecutive times. Another valid pattern (2,1) is also repeated 2 times.
Example 3:

Input: arr = [1,2,1,2,1,3], m = 2, k = 3
Output: false
Explanation: The pattern (1,2) is of length 2 but is repeated only 2 times. There is no pattern of length 2 that is repeated 3 or more times.
Example 4:

Input: arr = [1,2,3,1,2], m = 2, k = 2
Output: false
Explanation: Notice that the pattern (1,2) exists twice but not consecutively, so it doesn't count.
Example 5:

Input: arr = [2,2,2,2], m = 2, k = 3
Output: false
Explanation: The only pattern of length 2 is (2,2) however it's repeated only twice. Notice that we do not count overlapping repetitions.

"""

from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        count = 0
        i = 0
        while i <= len(arr) - 2 * m:
            if arr[i: i + m] == arr[i + m: i + 2 * m]:
                count += 2
                i += m
                if count == k:
                    return True
                while count < k and arr[i: i + m] == arr[i + m: i + 2 * m]:
                    count += 1
                    i += m
                if count < k:
                    count = 0
            else:
                i += 1
        return count >= k


if __name__ == '__main__':
    s = Solution()
    print(s.containsPattern([1, 2, 4, 4, 4, 4], 1, 3))
    print(s.containsPattern([1, 2, 4, 5, 4, 5], 2, 2))
    print(s.containsPattern([2, 2, 2, 2], m=2, k=3))
    print(s.containsPattern([1, 2, 1, 2, 1, 1, 1, 3], m=2, k=2))
