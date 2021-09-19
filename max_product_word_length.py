"""
318. Maximum Product of Word Lengths

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
"""


class Solution(object):

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        word_bit = [0 for _ in range(len(words))]
        maxLen = 0
        for i, word in enumerate(words):
            for c in word:
                mask = 1 << ord(c) - ord('a')
                word_bit[i] |= mask

        for i in range(0, len(words) - 1):
            for j in range(i + 1, len(words)):
                if word_bit[i] & word_bit[j] == 0:
                    maxLen = max(len(words[i]) * len(words[j]), maxLen)

        return maxLen