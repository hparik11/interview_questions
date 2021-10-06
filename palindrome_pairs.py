#!/usr/bin/env python
# coding:utf-8
"""
Name : palindrome_pairs.py
Author : Harsh Parikh
Time    : 6/13/21 11:35 AM
"""

"""
336. Palindrome Pairs


Share
Given a list of unique words, return all the pairs of the distinct indices (i, j) in 
the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

 

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
"""

from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word == word[::-1]

        palindrome_pairs = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if (len(words[i]) == 0 or len(words[j]) == 0) or words[i][0] == words[j][-1]:
                        if is_palindrome(words[i] + words[j]):
                            palindrome_pairs.append([i, j])

        return palindrome_pairs

    def palindromePairs1(self, words: List[str]) -> List[Tuple[int, int]]:
        """
        As we iterate through words, then, each word will possibly match another word in one of three ways:

        A blank string word will match on either side with any palindrome word. (e.g. "" will match with "abc" and vice versa)
        A full word will match on either side with its backwards version. (e.g. "abc" will match with "cba", and vice versa)
        A partial word will match its backwards version on the opposite side if the leftover portion of the word is a palindrome (e.g. "abcddd" will match with "cba" because "abc" matches with "cba" and "ddd" is a palindrome)
        The first check is easy to perform. If we find a blank string, we can iterate through the entire words list an extra time searching for palindromes to match. We just need to remember not to match the blank string with itself.

        For the second check, since we'll eventually iterate to the matching full word, we should only add the one pair at this time, rather than both, as we'll be able to add the second ordering of the same pair when we get to the second word.

        The third check is the most difficult. For this, we'll want to first reverse the current word to its backwards version (bw), since we'll be matching existing frontwards words in wmap. Then we should iterate through the indexes of the word itself, testing both sides of the dividing index (j) for being a palindrome.

        If a palindrome is found, then we can attempt to lookup the other portion of the word in wmap. If a match is found, we can push that pair to our answer array (ans). At the end of the iteration of words, we can return ans.

        Time Complexity: O(N * M^2) where N is the length of words and M is the average length of the words in words
        Space Complexity: O(N) for wmap


        """

        def is_palindrome(word1, start, end):
            if len(word1) < 2:
                return True

            while start < end:
                if word1[start] != word1[end]:
                    return False

                start += 1
                end -= 1

            return True

        palindrome_pairs = set()
        wordIndexDict = {}

        for i, word in enumerate(words):
            wordIndexDict[word] = i

        for i in range(len(words)):
            if words[i] == "":
                for j in range(len(words)):
                    if is_palindrome(words[j], 0, len(words[j]) - 1) and j != i:
                        palindrome_pairs.add((i, j))
                        palindrome_pairs.add((j, i))

            else:
                reverse_word = words[i][::-1]
                if (reverse_word in wordIndexDict) and (i != wordIndexDict[reverse_word]):
                    palindrome_pairs.add((i, wordIndexDict[reverse_word]))

                for j in range(1, len(reverse_word)):
                    if is_palindrome(reverse_word, 0, j - 1) and reverse_word[j:] in wordIndexDict:
                        palindrome_pairs.add((i, wordIndexDict[reverse_word[j:]]))

                    if is_palindrome(reverse_word, j, len(reverse_word) - 1) and reverse_word[:j] in wordIndexDict:
                        palindrome_pairs.add((wordIndexDict[reverse_word[:j]], i))

        return list(palindrome_pairs)


if __name__ == '__main__':
    s = Solution()
    print(s.palindromePairs1(["abcd", "dcba", "lls", "s", "sssll"]) == [[0, 1], [1, 0], [3, 2], [2, 4]])
    # print(s.palindromePairs1(["bat", "tab", "cat"]))
    # print(s.palindromePairs(["a", ""]))
