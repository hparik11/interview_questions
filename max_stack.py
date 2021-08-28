#!/usr/bin/env python
# coding:utf-8
"""
@FileName : max_stack.py
@Author   : Harsh Parikh
@Date     : 8/7/21 10:59 PM

Implement a LIFO stack that has a push(), pop(), and max() function, where max() returns the maximum value in the stack. All of these functions should run in O(1) time.

eg.

push(1)
max() = 1
push(2)
max() = 2
push(1)
max() = 2
pop() = 1
max() = 2
pop() = 2
max() = 1

"""

import unittest


class Node:
    def __init__(self, value, nxt=None, old_max=None):
        self.value = value
        self.nxt = nxt
        self.old_max = old_max


class MaxStack:
    def __init__(self):
        self.stack = []
        self.max = None

    def push(self, x: int):
        n = Node(x)

        if self.max is None or n.value > self.max.value:
            n.oldMax = self.max
            self.max = n

    def pop(self):
        try:
            if self.stack:
                n = self.stack
                self.stack = n.nxt
                self.max = n.old_max
                return n.value
        except ValueError:
            print("Stack is None")

    def max_val(self):
        try:
            if self.max:
                return self.max.value
        except ValueError:
            print("Max is None")


class TestMaxStack(unittest.TestCase):
    def test_1(self):
        ms = MaxStack()
        ms.push(1)
        ms.push(100)
        ms.push(5)
        self.assertEqual(ms.max_val(), 100)

    def test_2(self):
        ms = MaxStack()
        ms.push(1)
        ms.push(2)
        ms.push(3)
        self.assertEqual(ms.max_val(), 3)

    def test_3(self):
        ms = MaxStack()
        ms.push(-1)
        ms.push(2)
        ms.push(-3)
        self.assertEqual(ms.max_val(), 2)


if __name__ == '__main__':
    unittest.main()
