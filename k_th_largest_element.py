"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

import heapq
from typing import List


class Solution:
    # O(NLogK)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        # heapq.heapify(heap)

        for i in range(k, len(nums)):
            heapq.heappushpop(heap, nums[i])
        return heap[0]

    # O(nk) time, bubble sort idea, TLE
    def findKthLargest2(self, nums, k):
        for i in range(k):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    # exchange elements, time consuming
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums[len(nums) - k]

    # Avergae - O(N) | worst - O(N^2)
    def findKthLargest3(self, nums: List[int], k: int) -> int:

        def quickSortUtil(nums, startIndex, endIndex):
            pivotIndex = startIndex
            left = startIndex + 1
            right = endIndex

            while left <= right:
                if nums[left] > nums[pivotIndex] and nums[right] < nums[pivotIndex]:
                    nums[left], nums[right] = nums[right], nums[left]

                if nums[left] <= nums[pivotIndex]:
                    left += 1

                if nums[right] >= nums[pivotIndex]:
                    right -= 1

            nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]

            return right

        def select(nums, left, right, k_th_smallest):

            if left == right:
                return nums[left]

            pivot_index = quickSortUtil(nums, left, right)

            if pivot_index == k_th_smallest:
                return nums[pivot_index]
            elif pivot_index < k_th_smallest:
                return select(nums, pivot_index + 1, right, k_th_smallest)
            else:
                return select(nums, left, pivot_index - 1, k_th_smallest)

        return select(nums, 0, len(nums) - 1, len(nums) - k)


if __name__ == "__main__":
    print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 5))
