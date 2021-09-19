"""
392. Is Subsequence
Easy

3087

251

Add to List

Share
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""

import bisect
from collections import defaultdict


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        letter_indices_table = defaultdict(list)

        for i, ch in enumerate(t):
            letter_indices_table[ch].append(i)

        curr_matching_idx = -1

        for ch in s:
            if ch not in letter_indices_table:
                return False

            all_indices = letter_indices_table[ch]

            first_matching_idx = bisect.bisect_right(all_indices, curr_matching_idx)

            if first_matching_idx == len(all_indices):
                return False
            else:
                curr_matching_idx = all_indices[first_matching_idx]

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isSubsequence("acb", "ahbgdc"))
