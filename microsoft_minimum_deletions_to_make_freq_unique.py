#!/usr/bin/env python
# coding:utf-8
"""
@FileName : microsoft_minimum_deletions_to_make_freq_unique.py
@Author   : Harsh Parikh
@Date     : 7/29/21 5:49 PM

1647. Minimum Deletions to Make Character Frequencies Unique
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.



Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
"""

from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:

        characterFreq = Counter(s)

        FreqToChar = set()
        deleteOps = 0

        for ch, freq in characterFreq.items():
            if freq in FreqToChar:
                while freq > 0 and freq in FreqToChar:
                    freq -= 1
                    deleteOps += 1

            FreqToChar.add(freq)

        return deleteOps


if __name__ == '__main__':
    s = Solution()
    print(s.minDeletions("ceabaacb"))