#!/usr/bin/env python
# coding:utf-8
"""
@FileName : dropbox_pair_songs_with_duration_divisible_by_60.py
@Author   : Harsh Parikh
@Date     : 7/13/21 10:04 PM

1010. Pairs of Songs With Total Durations Divisible by 60
Medium

1525

88

Add to List

Share
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.



Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
"""


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        remainders = collections.defaultdict(int)

        ret = 0
        for t in time:
            if t % 60 == 0:  # check if a%60==0 && b%60==0
                ret += remainders[0]
            else:  # check if a%60+b%60==60
                ret += remainders[60 - t % 60]

            remainders[t % 60] += 1  # remember to update the remainders

        return ret
