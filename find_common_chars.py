"""
Find Common Characters

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""

from collections import Counter
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        """
            Without Duplicates
        """
        #         MAX_CHARS = 26

        #         prim_arr = [True for _ in range(MAX_CHARS)]

        #         for i in range(len(A)):
        #             sec_arr = [False for _ in range(MAX_CHARS)]
        #             for ch in A[i]:
        #                 # print(ord(ch)-ord('a'))
        #                 if prim_arr[ord(ch)-ord('a')]:
        #                     sec_arr[ord(ch)-ord('a')] = True

        #             prim_arr = sec_arr

        #         return [chr(i + ord('a')) for i, val in enumerate(prim_arr) if val]

        """
            With Duplicates
        """
        common_counter = Counter(A[0])
        for string in A[1:]:
            print(Counter(string))
            common_counter &= Counter(string)
        return list(common_counter.elements())


if __name__ == '__main__':
    s = Solution()
    print(s.commonChars(["cool", "lock", "cook"]))
