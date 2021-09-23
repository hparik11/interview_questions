#!/usr/bin/env python
# coding:utf-8
"""
@FileName : linkedlist_palindrome.py
@Author   : Harsh Parikh
@Date     : 7/3/21 6:29 PM

Given a singly linked list of integers, determine whether or not it's a palindrome.

Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list

Example

For l = [0, 1, 0], the output should be
isListPalindrome(l) = true;

For l = [1, 2, 2, 3], the output should be
isListPalindrome(l) = false.

Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 5 · 105,
-109 ≤ element value ≤ 109.

[output] boolean

Return true if l is a palindrome, otherwise return false
"""
import math


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome(head):
    # Write your code here.

    slow = fast = head
    # find the mid node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow
    # reverse the second half
    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    # compare the first and second half nodes
    while prev:
        if prev.val != head.val:
            return False
        prev = prev.next
        head = head.next

    return True


if __name__ == '__main__':
    head = LinkedList(0)
    head.next = LinkedList(1)
    head.next.next = LinkedList(2)
    head.next.next.next = LinkedList(2)
    head.next.next.next.next = LinkedList(1)
    head.next.next.next.next.next = LinkedList(0)
    print(linkedListPalindrome(head))
