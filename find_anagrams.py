"""
438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        input_dict = [0] * 26
        input_str = [0] * 26

        for ch in p:
            input_dict[ord(ch) - ord('a')] += 1

        idx = 0
        result = []
        while idx < len(s):
            input_str[ord(s[idx]) - ord('a')] += 1
            if input_str == input_dict:
                result.append(idx + 1 - len(p))

            if idx + 1 >= len(p):
                input_str[ord(s[idx + 1 - len(p)]) - ord('a')] -= 1

            idx += 1

        return result


if __name__ == "__main__":
    print(Solution().findAnagrams('abab', 'ab'))
