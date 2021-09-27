#!/usr/bin/env python
# coding:utf-8
"""
@FileName : count_subset_min_max_less_than_k.py
@Author   : Harsh Parikh
@Date     : 7/10/21 12:49 AM

Count of subsets having sum of min and max element less than K
Difficulty Level : Medium

Given an integer array arr[] and an integer K, the task is to find the number of non-empty subsets S such that min(S) + max(S) < K.
Examples:


Input: arr[] = {2, 4, 5, 7} K = 8
Output: 4
Explanation:
The possible subsets are {2}, {2, 4}, {2, 4, 5} and {2, 5}
Input:: arr[] = {2, 4, 2, 5, 7} K = 10
Output: 26


Approach


Sort the input array first.
Now use Two Pointer Technique to count the number of subsets.
Let take two pointers left and right and set left = 0 and right = N-1.

if (arr[left] + arr[right] < K )
Increment the left pointer by 1 and add 2 j – i into answer, because the left and right values make up a potential end values of a subset. All the values from [i, j – 1] also make up end of subsets which will have the sum < K. So, we need to calculate all the possible subsets for left = i and right ∊ [i, j]. So, after suming up values 2 j – i + 1 + 2 j – i – 2 + … + 2 0 of the GP, we get 2 j – i .
if( arr[left] + arr[right] >= K )
Decrement the right pointer by 1.

"""


def get_subset_count(arr, K, N):
    # Sorting the array
    arr.sort()

    left = 0;
    right = N - 1;

    # ans stores total number of subsets
    ans = 0;

    while left <= right:
        if arr[left] + arr[right] < K:

            # Add all possible subsets
            # between i and j
            ans += 1 << (right - left);
            left += 1;
        else:

            # Decrease the sum
            right -= 1;

    return ans;


# Driver code
arr = [2, 4, 5, 7];
K = 8;

print(get_subset_count(arr, K, 4))
