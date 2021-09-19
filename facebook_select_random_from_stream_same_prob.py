#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_select_random_from_stream_same_prob.py
@Author   : Harsh Parikh
@Date     : 8/8/21 11:45 AM
"""

# An efficient python3 program
# to randomly select a number
# from stream of numbers.

"""
let’s attempt to solve using loop invariants. On the ith iteration of our loop to pick a random element, 
let’s assume we already picked an element uniformly from [0, i - 1]. 
In order to maintain the loop invariant, we would need to pick 
the ith element as the new random element at 1 / (i + 1) chance. 
For the base case where i = 0, let’s say the random element is the first one. Then we know it works because

For i = 0, we would’ve picked uniformly from [0, 0].
For i > 0, before the loop began, any element K in [0, i - 1] had 1 / i chance
of being chosen as the random element. We want K to have 1 / (i + 1) chance
of being chosen after the iteration. This is the case since the chance of having
being chosen already but not getting swapped with the ith element is
1 / i * (1 - (1 / (i + 1))) which is 1 / i * i / (i + 1) or 1 / (i + 1)
"""
import random


def pick(big_stream):
    random_element = None

    for idx, e in enumerate(big_stream):
        if idx == 0:
            random_element = e
        elif random.randint(1, idx + 1) == 1:
            random_element = e

    return random_element


# Driver Code
stream = [1, 2, 3, 4]
n = len(stream)
count = 0

# Use a different seed value
# for every run.
for i in range(n):
    print("Random number from first",
          (i + 1), "numbers is",
          pick(stream)
          )
