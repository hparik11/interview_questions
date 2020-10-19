# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: amazon_parition_label.py
# @Date:   10/18/20, Sun

"""
763. Partition Labels
Medium

3431

140

Add to List

Share
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.



Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.


Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.

"""
from collections import defaultdict
class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        dictn = defaultdict(int)
        for i, ch in enumerate(S):
            dictn[ch] = i

        startIndex = 0
        lastIndex = 0
        lengths = []
        for i, ch in enumerate(S):
            lastIndex = max(lastIndex, dictn[ch])
            if i == lastIndex:
                substringLength = lastIndex - startIndex + 1
                lengths.append(substringLength)
                startIndex = i + 1

        return lengths
