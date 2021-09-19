"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

from typing import List

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         countDictn = {}
#         for num in nums:
#             if num in countDictn:
#                 countDictn[num] += 1
#             else:
#                 countDictn[num] = 1
#         return sorted(countDictn, key=countDictn.get, reverse=True)[:k]

import collections
import heapq


class Solution:

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        countDictn = {}
        for num in nums:
            if num in countDictn:
                countDictn[num] += 1
            else:
                countDictn[num] = 1
        return sorted(countDictn, key=countDictn.get, reverse=True)[:k]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []
        myDict = collections.Counter(nums)
        for key in myDict:
            temp = (myDict[key], key)
            if len(heap) >= k:
                heapq.heappushpop(heap, temp)
            else:
                heapq.heappush(heap, temp)
        for i in range(len(heap)):
            result.append(heapq.heappop(heap)[1])
        return result[::-1]


if __name__ == '__main__':
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3, 3, 3], 2))
