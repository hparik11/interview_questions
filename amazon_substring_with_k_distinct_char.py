# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: amazon_substring_with_k_distinct_char.py
# @Date:   9/23/20, Wed

"""
Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

Example 1:

Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]
Example 2:

Input: s = "abacab", k = 3
Output: ["bac", "cab"]
Example 3:

Input: s = "awaglknagawunagwkwagl", k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
Explanation:
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl"
"wagl" is repeated twice, but is included in the output once.
Constraints:

The input string consists of only lowercase English letters [a-z]
0 ≤ k ≤ 26

"""


class Solution:
    def uniqueSubstringSizeK(self, string, k):
        substrings = set()
        charHashMap = {}
        i = 0
        start = 0
        while i < len(string):
            currCh = string[i]

            if currCh in charHashMap:
                if charHashMap[currCh] >= start:
                    start = charHashMap[currCh] + 1

            charHashMap[currCh] = i

            if i - start + 1 == k:
                substrings.add(string[start: i + 1])
                start += 1

            i += 1

        return substrings


if __name__ == '__main__':
    s = Solution()
    print(s.uniqueSubstringSizeK("abcabc", 3))
    print(s.uniqueSubstringSizeK("abacab", 3))
