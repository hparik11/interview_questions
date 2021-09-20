"""
269. Alien Dictionary

There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.



Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
"""

from collections import defaultdict, Counter, deque


class Solution:
    def alienOrder(self, words) -> str:

        # create data structures + the in_degree of each unique letter to 0.
        indegree = Counter({c: 0 for word in words for c in word})
        adj_list = defaultdict(list)

        for firstWord, secondWord in zip(words, words[1:]):
            i = 0
            j = 0
            areAllCharactersMatch = True
            while i < len(firstWord) and j < len(secondWord):
                c = firstWord[i]
                d = secondWord[j]

                if c != d:
                    if d not in adj_list[c]:
                        indegree[d] += 1
                        adj_list[c].append(d)

                    areAllCharactersMatch = False
                    break

                i += 1
                j += 1

            # Check that second word isn't a prefix of first word.
            if areAllCharactersMatch and len(secondWord) < len(firstWord):
                return ""

        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.

        output = []
        queue = deque([ch for ch in indegree if indegree[ch] == 0])

        while queue:
            c = queue.popleft()
            output.append(c)

            for neigh in adj_list[c]:
                indegree[neigh] -= 1

                if indegree[neigh] == 0:
                    queue.append(neigh)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(indegree):
            return ""

        return "".join(output)


if __name__ == '__main__':
    s = Solution()
    print(s.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
