#!/usr/bin/env python
# coding:utf-8
"""
@FileName : robot_bounding_in_circle.py
@Author   : Harsh Parikh
@Date     : 7/25/21 3:42 PM

1041. Robot Bounded In Circle

On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.



Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.
Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = (0, 1)
        start = [0, 0]

        # Rotate four times to confirm that you're in same cycle
        for _ in range(4):
            for x in instructions:
                if x == 'G':
                    start[0] += direction[0]
                    start[1] += direction[1]
                elif x == 'L':
                    direction = (-direction[1], direction[0])
                elif x == 'R':
                    direction = (direction[1], -direction[0])

        return start == [0, 0]


if __name__ == '__main__':
    s = Solution()
    print(s.isRobotBounded("GGLLGG"))
