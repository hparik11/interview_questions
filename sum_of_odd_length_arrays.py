"""
1588. Sum of All Odd Length Subarrays
Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.

Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
Example 3:

Input: arr = [10,11,12]
Output: 66
 

"""

import unittest
from typing import List
 

class Solution:
    @classmethod
    def sumOddLengthSubarrays_O_N3(self, arr: List[int]) -> int:
        
        totalSum = 0
        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                totalSum += sum(arr[i: j+1])
        
        return totalSum
    
    @classmethod
    def sumOddLengthSubarrays_O_N2(self, arr: List[int]) -> int:
        
        totalSum = 0

        for i in range(len(arr)):
            currSum = 0
            for j in range(i, len(arr), 2):
                if j != i:
                    currSum += arr[j] + arr[j-1]
                else:
                    currSum += arr[j]
                
                totalSum += currSum

        return totalSum

class Test(unittest.TestCase):
    test1 = [1,4,2,5,3]
    expected = 58

    def test_sum(self):
        actual = Solution.sumOddLengthSubarrays_O_N3(self.test1)
        self.assertEqual(actual, self.expected)

        actual = Solution.sumOddLengthSubarrays_O_N2(self.test1)
        self.assertEqual(actual, self.expected)

if __name__ == '__main__':
    unittest.main()