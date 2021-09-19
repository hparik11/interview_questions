"""
1013. Partition Array Into Three Parts With Equal Sum

Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

 

Example 1:

Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

"""


class Solution:
    #     def canThreePartsEqualSum(self, A: List[int]) -> bool:
    #         leftIndex = 0
    #         rightIndex = len(A) - 1

    #         while True:
    #             if leftIndex >= rightIndex:
    #                 return False
    #             if sum(A[:leftIndex+1]) == sum(A[rightIndex:]):
    #                 break
    #             if sum(A[:leftIndex+1]) > sum(A[rightIndex:]):
    #                 rightIndex -= 1
    #             else:
    #                 leftIndex += 1

    #             # print(leftIndex, rightIndex, A[:leftIndex+1], A[rightIndex:])

    #         if sum(A[leftIndex+1:rightIndex]) == sum(A[:leftIndex+1]):
    #             return True
    #         return False
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        expected, total, count = sum(A) / 3, 0, 0

        for each in A:
            total += each
            if total == expected:
                count += 1
                total = 0

        return count == 3


if __name__ == "__main__":
    print(Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
