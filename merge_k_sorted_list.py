
#!/usr/bin/env python
# coding:utf-8
"""
@FileName : merge_k_sorted_list.py
@Author   : Harsh Parikh
@Date     : 7/13/21 3:21 PM
"""

import heapq


# time complexity:O(nlog(k) + k) |  space-> O(n + k)
def mergeSortedArrays(arrays):
    # Write your code here.
    sortedList = []
    elementIdxs = [0 for _ in range(len(arrays))]

    while True:
        heapArray = []
        for index, each_array in enumerate(arrays):
            if elementIdxs[index] == len(each_array):
                continue
            heapArray.append((each_array[elementIdxs[index]], index))
        if len(heapArray) == 0:
            break
        heapq.heapify(heapArray)
        minValue, minIdx = heapq.heappop(heapArray)
        sortedList.append(minValue)
        elementIdxs[minIdx] += 1

    return sortedList


if __name__ == '__main__':
    print(mergeSortedArrays([
        [1, 5, 9, 21],
        [-1, 0],
        [-124, 81, 121],
        [3, 6, 12, 20, 150]
    ]))
