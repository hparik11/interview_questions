#!/usr/bin/env python
# coding:utf-8
"""
@FileName : remove_duplicates_from_linkedlist.py
@Author   : Harsh Parikh
@Date     : 6/28/21 9:23 PM

"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    current = linkedList

    while current is not None:
        nextNode = current.next

        while nextNode is not None and nextNode.value == current.value:
            nextNode = nextNode.next

        current.next = nextNode
        current = nextNode

    return linkedList

