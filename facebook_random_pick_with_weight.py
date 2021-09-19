#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_random_pick_with_weight.py
@Author   : Harsh Parikh
@Date     : 8/1/21 11:43 PM

528. Random Pick with Weight

You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).

We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

More formally, the probability of picking index i is w[i] / sum(w).



Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. Since there is only one single element on the array the only option is to return the first element.
Example 2:

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It's returning the second element (index = 1) that has probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It's returning the first element (index = 0) that has probability of 1/4.

Since this is a randomization problem, multiple answers are allowed so the following outputs can be considered correct :
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
"""


class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefixSum = w
        for i in range(1, len(self.prefixSum)):
            self.prefixSum[i] = self.prefixSum[i] + self.prefixSum[i - 1]

    def pickIndex(self):
        """
        :rtype: int
        """

        """
        example:

        index: 0, 1, 2, 3
        weight: 1, 8, 10, 2
        prefixsum: 1, 9, 19, 21
        [1] [2,9] [10, 19] [20, 21]
        index=0 index=1 index=2 index=3
        
        """
        if len(self.prefixSum) == 0:
            return 0

        target = random.randint(1, self.prefixSum[-1])

        idx = bisect.bisect_left(self.prefixSum, target)
        return idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
