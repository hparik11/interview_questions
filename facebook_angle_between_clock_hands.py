#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_angle_between_clock_hands.py
@Author   : Harsh Parikh
@Date     : 9/17/21 1:33 AM

1344. Angle Between Hands of a Clock
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

Example 1:

Input: hour = 12, minutes = 30
Output: 165
Example 2:

Input: hour = 3, minutes = 30
Output: 75
Example 3:

Input: hour = 3, minutes = 15
Output: 7.5
Example 4:

Input: hour = 4, minutes = 50
Output: 155
Example 5:

Input: hour = 12, minutes = 0
Output: 0
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        one_min_angle = 6
        one_hour_angle = 30

        minutes_angle = one_min_angle * minutes
        hour_angle = (hour % 12 + minutes / 60) * one_hour_angle

        diff = abs(hour_angle - minutes_angle)
        return min(diff, 360 - diff)