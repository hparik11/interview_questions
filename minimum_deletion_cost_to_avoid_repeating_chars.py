#!/usr/bin/env python
# coding:utf-8
"""
@FileName : minimum_deletion_cost_to_avoid_repeating_chars.py
@Author   : Harsh Parikh
@Date     : 9/8/21 11:21 PM

1578. Minimum Deletion Cost to Avoid Repeating Letters

Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.



Example 1:

Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).
Example 2:

Input: s = "abc", cost = [1,2,3]
Output: 0
Explanation: You don't need to delete any character because there are no identical letters next to each other.
Example 3:

Input: s = "aabaa", cost = [1,2,3,4,1]
Output: 2
Explanation: Delete the first and the last character, getting the string ("aba").

"""


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = prev = 0  # index of previously retained letter

        for i in range(1, len(s)):
            """
            if current is not same as prev character then simply update previous to current
            else find out which is minimum between current and previous, add cost to final answer
            but now, check if my current is higher than previous then move previous pointer to current because 
            we already added min cost of previous char deletion and vice-versa 
            """
            if s[prev] != s[i]:
                prev = i
            else:
                ans += min(cost[prev], cost[i])

                if cost[prev] < cost[i]:
                    prev = i
        return ans
