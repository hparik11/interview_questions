# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: lru_cache.py
# @Date:   9/23/20, Wed

"""
146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        val = self.dict.pop(key)  # Remove it first before inserting it at the end again
        self.dict[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
        else:
            if len(self.dict) == self.capacity:
                del self.dict[next(iter(self.dict))]

        self.dict[key] = value


class Node:
    def __init__(self, key=-1, val=-1):
        self.key, self.val = key, val
        self.prev = self.next = None


class DoubleLinkedList(object):
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        if not node or node == self.tail:
            return
        node.prev.next = node.next
        node.next.prev = node.prev


class LRUCache(object):
    def __init__(self, capacity):
        self.dic, self.cap = {}, capacity
        self.ddl = DoubleLinkedList()

    def get(self, key):
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.ddl.remove(node)
        self.ddl.insert(node)
        return node.val

    def put(self, key, value):
        if key in self.dic:
            self.ddl.remove(self.dic[key])
        elif len(self.dic) >= self.cap:
            self.dic.pop(self.ddl.head.next.key, None)
            self.ddl.remove(self.ddl.head.next)

        self.dic[key] = Node(key, value)
        self.ddl.insert(self.dic[key])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
