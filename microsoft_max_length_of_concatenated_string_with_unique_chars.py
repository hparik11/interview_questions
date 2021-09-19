#!/usr/bin/env python
# coding:utf-8
"""
@FileName : microsoft_max_length_of_concatenated_string_with_unique_chars.py
@Author   : Harsh Parikh
@Date     : 7/30/21 8:58 PM

1239. Maximum Length of a Concatenated String with Unique Characters

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
"""


class Solution:

    def maxLength(self, arr) -> int:

        ans = 0

        # Do a DFS on all the individual array elements
        def dfs(arr, path, l, r):
            nonlocal ans
            # If path has non-zero length then that means this is a potential solution
            if path:
                ans = max(ans, len(path))

            for i in range(l, r):
                if len(path + arr[i]) == len(set(path + arr[i])):
                    dfs(arr, path + arr[i], i + 1, r)

        path = ""

        arr.sort(key=len)

        dfs(arr, path, 0, len(arr))

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxLength(["un", "iq", "ue"]))
