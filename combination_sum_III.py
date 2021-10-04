# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: combination_sum_III.py
# @Date:   9/13/20, Sun

"""
216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""

from typing import List

"""
Time 9Ck = 9!/(k! * (9-k)!)
   
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(target, start, candidates, path, paths):
            # print(target, start, path)
            if target == 0 and len(path) == k:
                paths.append(path)
                return True

            if target < 0:
                return

            for i in range(start, len(candidates)):
                dfs(target - candidates[i], i + 1, candidates, path + [candidates[i]], paths)

        path = []
        paths = []
        dfs(n, 0, range(1, 10), path, paths)
        return paths


if __name__ == '__main__':
    s = Solution()

    print(s.combinationSum3(3, 7))
    print(s.combinationSum3(3, 9))
