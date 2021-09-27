"""
239. Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""

from typing import List


class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     result = []

    #     if not nums:
    #         return result

    #     for i in range(0, len(nums)-k+1):
    #         result.append(max(nums[i: i+k]))

    #     return result

    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     if not nums:
    #         return []

    #     result = [max(nums[:k])]
    #     maxLastIndex = nums.index(result[0])

    #     for i in range(k, len(nums)):
    #         if i-k < maxLastIndex <= i:
    #             if nums[i] > result[-1]:
    #                 result.append(nums[i])
    #                 maxLastIndex = i
    #             else:
    #                 result.append(result[-1])
    #         else:
    #             result.append(max(nums[i-k+1:i+1]))
    #             maxLastIndex = nums.index(result[-1])   

    #     return result

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []

        # O(nk) in the worst case of sorted descending array
        # O(n) in the best case of sorted ascending array
        output = []
        max_idx = -1
        for i in range(n - k + 1):
            # max_idx is out of sliding window
            if max_idx < i:
                max_idx = i
                for j in range(i, i + k):
                    if nums[j] > nums[max_idx]:
                        max_idx = j
            # max element is smaller than the last 
            # element in the window
            elif nums[max_idx] < nums[i + k - 1]:
                max_idx = i + k - 1
            output.append(nums[max_idx])
        return output

    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:

        from collections import deque
        q = deque()  # stores *indices*
        res = []

        for i, cur in enumerate(nums):

            while q and nums[q[-1]] <= cur:
                q.pop()

            q.append(i)

            # remove first element if it's outside the window
            if q[0] == i - k:
                q.popleft()

            # if window has k elements add to results (first k-1 windows have <k elements because we start from empty window and add 1 element each iteration)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res


if __name__ == "__main__":
    # print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    # print(Solution().maxSlidingWindow([], 0))
    # print(Solution().maxSlidingWindow([1,-1], 1))
    # print(Solution().maxSlidingWindow([1,3,1,2,0,5], 3))
    print(Solution().maxSlidingWindow([9, 10, 9, -7, -4, -8, 2, -6], 5))
