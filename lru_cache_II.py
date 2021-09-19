#!/usr/bin/env python
# coding:utf-8
"""
@FileName : lru_cache_II.py
@Author   : Harsh Parikh
@Date     : 7/3/21 4:36 PM
"""


# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.cache = {}
        self.ddl = DoubleLinkedList()

    def insertKeyValuePair(self, key, value):
        # Write your code here.
        if key in self.cache:
            self.ddl.remove(self.cache[key])

        node = Node(key, value)
        self.ddl.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.maxSize:
            node = self.ddl.head.next
            print(node.key)
            self.ddl.remove(node)
            del self.cache[node.key]

        print(self.cache)

    def getValueFromKey(self, key):
        # Write your code here.
        if key not in self.cache:
            return None

        node = self.cache[key]
        self.ddl.remove(self.cache[key])
        self.ddl.insert(node)

        return node.val

    def getMostRecentKey(self):
        # Write your code here.
        node = self.ddl.tail.prev
        return node.key


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):

        prevNode = self.tail.prev

        prevNode.next = node
        self.tail.prev = node

        node.prev = prevNode
        node.next = self.tail

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = node.next
        nextNode.prev = node.prev
