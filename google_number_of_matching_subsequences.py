"""
792. Number of Matching Subsequences

Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".


Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
"""

from collections import defaultdict
import bisect


class Solution:
    def numMatchingSubseq(self, s: str, words) -> int:
        """
         Let n be length of s and m be total length of all words in words. Then we can                   precompute all places for each symbol in s and then use binary search to find if word.

         Time complexity is O(m*log n + n), because we do at most m binary searches and we need O(n) to evaluate places.
         Space complexity is O(n).


        """
        places = defaultdict(list)

        for i, symbol in enumerate(s):
            places[symbol].append(i)

        def is_sequence(places, word):
            curr_matching_sequence = -1

            for ch in word:
                if ch not in places:
                    return False

                all_matching_indices = places[ch]

                first_matching_index = bisect.bisect_right(all_matching_indices, curr_matching_sequence)

                if first_matching_index == len(all_matching_indices):
                    return False
                else:
                    curr_matching_sequence = all_matching_indices[first_matching_index]

            return True

        num_matching_subsequences = 0

        for word in words:
            if is_sequence(places, word):
                num_matching_subsequences += 1

        return num_matching_subsequences


if __name__ == '__main__':
    s = Solution()
    print(s.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))
