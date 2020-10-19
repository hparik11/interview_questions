# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: combination_sum.py
# @Date:   9/13/20, Sun


"""
Combination Sum
Medium

4338

128

Add to List

Share
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target, start, candidates, path, paths):
            # print(target, start, path)
            if target == 0:
                paths.append(path)

                return True
            if target < 0:
                return
            for i in range(start, len(candidates)):
                dfs(target - candidates[i], i, candidates, path + [candidates[i]], paths)

        path = []
        paths = []

        dfs(target, 0, candidates, path, paths)
        return paths


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
    print(s.combinationSum([2, 3, 5], 8))
