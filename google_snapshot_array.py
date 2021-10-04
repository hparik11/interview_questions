#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_snapshot_array.py
@Author   : Harsh Parikh
@Date     : 10/3/21 4:38 PM

1146. Snapshot Array

Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id


Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation:
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
"""

from collections import defaultdict


class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = defaultdict(defaultdict)
        self.snap_cnt = 0

    def set(self, index: int, val: int) -> None:
        self.snaps[self.snap_cnt][index] = val

    def snap(self) -> int:
        self.snap_cnt += 1
        return self.snap_cnt - 1

    def get(self, index: int, snap_id: int) -> int:
        cur = snap_id
        while cur > 0 and index not in self.snaps[cur]:
            cur -= 1
        if index in self.snaps[cur]:
            return self.snaps[cur][index]
        return 0


class SnapshotArray1:

    def __init__(self, length: int):
        self.snapshot = {i: {0: 0} for i in range(length)}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.snapshot[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id not in self.snapshot[index]:
            keys = list(self.snapshot[index].keys())
            idx = bisect.bisect_right(keys, snap_id)
            return self.snapshot[index][keys[idx - 1]]

        return self.snapshot[index][snap_id]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)