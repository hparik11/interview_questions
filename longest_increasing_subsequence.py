"""
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""

from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    """

    Complexity Analysis

    Given N as the length of nums,

    Time complexity: O(N^2)

    Space complexity: O(N)

    The only extra space we use relative to input size is the dp array, which is the same length as nums.

    """
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def lengthOfLIS1(self, nums: List[int]) -> int:
    """
    Intuition

    In the previous approach, when we have an element num that is not greater than all the elements in sub, we perform a linear scan to find the first element in sub that is greater than or equal to num. Since sub is in sorted order, we can use binary search instead to greatly improve the efficiency of our algorithm.

    Algorithm

    Initialize an array sub which contains the first element of nums.

    Iterate through the input, starting from the second element. For each element num:

    If num is greater than any element in sub, then add num to sub.
    Otherwise, perform a binary search in sub to find the smallest element that is greater than or equal to num. Replace that element with num.
    Return the length of sub


    Complexity Analysis

    Given N as the length of nums,

    Time complexity: O(N⋅log(N))

    Space complexity: O(N)

    When the input is strictly increasing, the sub array will be the same size as the input.
    """
    sub = []
    for num in nums:
        i = bisect_left(sub, num)
        print(i)

        # If num is greater than any element in sub
        if i == len(sub):
            sub.append(num)

        # Otherwise, replace the first element in sub greater than or equal to num
        else:
            sub[i] = num

    return len(sub)


if __name__ == "__main__":
    # print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    # print(lengthOfLIS([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]))
    print(lengthOfLIS([10, 22, 9, 33, 21, 61, 41, 60, 80]))
    print(lengthOfLIS([1, 5, -1, 10]))
