#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_find_replace_string.py
@Author   : Harsh Parikh
@Date     : 9/30/21 10:10 PM

833. Find And Replace in String

You are given a 0-indexed string s that you must perform k replacement operations on. The replacement operations are given as three 0-indexed parallel arrays, indices, sources, and targets, all of length k.

To complete the ith replacement operation:

Check if the substring sources[i] occurs at index indices[i] in the original string s.
If it does not occur, do nothing.
Otherwise if it does occur, replace that substring with targets[i].
For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the result of this replacement will be "eeecd".

All replacement operations must occur simultaneously, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will not overlap.

For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] will not be generated because the "ab" and "bc" replacements overlap.
Return the resulting string after performing all replacement operations on s.

A substring is a contiguous sequence of characters in a string.



Example 1:


Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
Output: "eeebffff"
Explanation:
"a" occurs at index 0 in s, so we replace it with "eee".
"cd" occurs at index 2 in s, so we replace it with "ffff".
Example 2:


Input: s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
Output: "eeecd"
Explanation:
"ab" occurs at index 0 in s, so we replace it with "eee".
"ec" does not occur at index 2 in s, so we do nothing.
"""

from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

        S_idx = 0
        new_string = []

        d = {}

        for i in range(len(indices)):
            idx, src, target = indices[i], sources[i], targets[i]
            d[idx] = (src, target)

        while S_idx < len(s):
            if S_idx in d:

                source, target = d[S_idx]

                if s[S_idx:S_idx + len(source)] == source:
                    new_string.append(target)
                    S_idx += len(source)
                    continue

            new_string.append(s[S_idx])
            S_idx += 1

        return ''.join(new_string)


if __name__ == '__main__':
    s = Solution()
    print(s.findReplaceString("abcd",
                              [0, 2],
                              ["a", "cd"],
                              ["eee", "ffff"]))
