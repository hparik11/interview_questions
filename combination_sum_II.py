# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: combination_sum_II.py
# @Date:   9/13/20, Sun

"""
Combination Sum II
Medium

1988

73

Add to List

Share
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target, start, candidates, path, paths):
            # print(target, start, path)
            if target == 0:
                paths.append(path)
                return True

            if target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                dfs(target - candidates[i], i+1, candidates, path + [candidates[i]], paths)

        path = []
        paths = []
        dfs(target, 0, sorted(candidates), path, paths)
        return paths

        """
        def dfs(target, start, candidates, path, paths):
            # print(target, start, path)
            if target == 0:
                paths.add(path)

                return True
            if target < 0:
                return
            for i in range(start, len(candidates)):
                dfs(target - candidates[i], i+1, candidates, path + (candidates[i], ), paths)

        path = ()
        paths = set()

        dfs(target, 0, candidates, path, paths)
        return [list(a) for a in paths]
        """


if __name__ == '__main__':
    s = Solution()
    # print(s.combinationSum2([2, 3, 6, 7], 7))
    # print(s.combinationSum2([2, 3, 5], 8))
    print(s.combinationSum2([2, 5, 2, 1, 2], 5))
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
