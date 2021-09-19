#!/usr/bin/env python
# coding:utf-8
"""
@FileName : remove_k_from_linked_list.py
@Author   : Harsh Parikh
@Date     : 6/28/21 8:52 PM


Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

Example

For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
removeKFromList(l, k) = [1, 2, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7].
Input/Output

[time limit] 4000ms (py3)
[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 10^5,
-1000 ≤ element value ≤ 1000.

[input] integer k

An integer.

Guaranteed constraints:
-1000 ≤ k ≤ 1000.

[output] linkedlist.integer

Return l with all the values equal to k removed.
"""


def removeKFromList(l, k):
    fakeHead = ListNode(None)
    fakeHead.next = l
    current = fakeHead

    while current:
        while current.next and current.next.value == k:
            current.next = current.next.next
        current = current.next

    return fakeHead.next
