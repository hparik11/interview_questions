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
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = []

        # for num in nums:
        #     heapq.heappush(heap, num)
        
        # heapq._heapify_max(heap)
        # # print(heapq.nlargest(5, heap))
        # while k > 0:
        #     val = heapq._heappop_max(heap)
        #     k-=1
        
        # return val
        # heapq.heapify(nums)
        # klargest = heapq.nlargest(k, nums)
        # return klargest.pop()

        heap = nums[:k]
        heapq.heapify(heap)

        for i in range(k,len(nums)):
            heapq.heappushpop(heap, nums[i])
        return heap[0]

if __name__ == "__main__":
    print(Solution().findKthLargest([3,2,1,5,6,4], 2))