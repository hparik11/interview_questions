"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        start = 0
        maxLen = 0
        charDict = {}

        for i, ch in enumerate(s):
            if ch in charDict:
                maxLen = max(maxLen, i - start)
                start = max(start, charDict[ch] + 1)
                charDict[ch] = i
            else:
                charDict[ch] = i

        if start != 0:
            return max(maxLen, i + 1 - start)
        else:
            return max(maxLen, i + 1)


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring('abcabcbb'))
    print(Solution().lengthOfLongestSubstring('bbbbb'))
    print(Solution().lengthOfLongestSubstring('pwwkew'))
    print(Solution().lengthOfLongestSubstring(' '))
    print(Solution().lengthOfLongestSubstring('au'))
    print(Solution().lengthOfLongestSubstring('aab'))
    print(Solution().lengthOfLongestSubstring('abba'))
