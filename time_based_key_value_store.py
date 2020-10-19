# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: time_based_key_value_store.py
# @Date:   9/20/20, Sun
"""
981. Time Based Key-Value Store
Medium

853

108

Add to List

Share
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").


Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:
TimeMap kv;
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1
kv.get("foo", 1);  // output "bar"
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
kv.set("foo", "bar2", 4);
kv.get("foo", 4); // output "bar2"
kv.get("foo", 5); //output "bar2"

Example 2:

Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]
"""
from collections import defaultdict


class TimeMap(object):

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key, value, timestamp):
        self.map[key].append((timestamp, value))

    def get(self, key, timestamp):

        if key not in self.map:
            return ''
        values = self.map[key]

        left, right = 0, len(values) - 1

        while left < right:
            mid = (left + right + 1) / 2
            pre_time, value = values[mid]
            if pre_time > timestamp:
                right = mid - 1
            else:
                left = mid

        return values[left][1] if values[left][0] <= timestamp else ''
