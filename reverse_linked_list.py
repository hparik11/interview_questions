#!/usr/bin/env python
# coding:utf-8
"""
@FileName : reverse_linked_list.py
@Author   : Harsh Parikh
@Date     : 6/28/21 9:04 PM
"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
    current = head

    previous = None

    while current is not None:
        nextNode = current.next
        current.next = previous
        previous = current
        current = nextNode

    return previous
