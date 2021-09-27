#!/usr/bin/env python
# coding:utf-8
"""
@FileName : candy.py
@Author   : Harsh Parikh
@Date     : 8/9/21 9:23 PM

135. Candy

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.



Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
"""

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:

        left2right = [1 for _ in ratings]
        right2left = [1 for _ in ratings]

        # left to right
        for idx in range(1, len(ratings)):
            if ratings[idx - 1] < ratings[idx]:
                left2right[idx] += left2right[idx - 1]

        # right to left
        for idx in range(len(ratings) - 2, -1, -1):
            if ratings[idx] > ratings[idx + 1]:
                right2left[idx] += right2left[idx + 1]

        minimum_candies = 0

        for idx in range(len(ratings)):
            minimum_candies += max(left2right[idx], right2left[idx])

        return minimum_candies


if __name__ == '__main__':
    s = Solution()
    print(s.candy([1, 2, 2]))
