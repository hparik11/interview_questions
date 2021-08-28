#!/usr/bin/env python
# coding:utf-8
"""
@FileName : sum_of_linkedlist.py
@Author   : Harsh Parikh
@Date     : 6/23/21 11:38 PM
"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    resultLinkedList = LinkedList(0)
    tempNode = resultLinkedList
    carry = 0

    while linkedListOne is not None and linkedListTwo is not None:
        currSum = carry + linkedListOne.value + linkedListTwo.value

        quotient, remainder = divmod(currSum, 10)

        carry = quotient

        newNode = LinkedList(remainder)

        tempNode.next = newNode
        tempNode = newNode

        linkedListOne = linkedListOne.next
        linkedListTwo = linkedListTwo.next

    while linkedListOne is not None:
        currSum = carry + linkedListOne.value
        quotient, remainder = divmod(currSum, 10)
        carry = quotient

        # tempNode.value = remainder
        newNode = LinkedList(remainder)

        tempNode.next = newNode
        tempNode = newNode
        linkedListOne = linkedListOne.next

    while linkedListTwo is not None:
        currSum = carry + linkedListTwo.value
        quotient, remainder = divmod(currSum, 10)
        carry = quotient

        newNode = LinkedList(remainder)
        tempNode.next = newNode
        tempNode = newNode

        linkedListTwo = linkedListTwo.next

    if carry == 1:
        newNode = LinkedList(carry)
        tempNode.next = newNode
        tempNode = newNode

    return resultLinkedList.next
