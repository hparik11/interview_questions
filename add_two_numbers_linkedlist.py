#!/usr/bin/env python
# coding:utf-8
"""
@FileName : add_two_numbers_linkedlist.py
@Author   : Harsh Parikh
@Date     : 8/10/21 7:25 PM

445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        number1 = 0
        number2 = 0

        while l1:
            number1 = number1 * 10 + l1.val
            l1 = l1.next

        while l2:
            number2 = number2 * 10 + l2.val
            l2 = l2.next

        lsum = number1 + number2

        head = ListNode(None)
        cur = head

        for istr in str(lsum):
            cur.next = ListNode(int(istr))
            cur = cur.next

        return head.next


class Solution1:

    def reverse_linked_list(self, head):

        prev = None
        curr = head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1 = self.reverse_linked_list(l1)
        l2 = self.reverse_linked_list(l2)

        head = None
        carry = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            carry, val = divmod(carry + val1 + val2, 10)

            node = ListNode(val)
            node.next = head
            head = node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            node = ListNode(carry)
            node.next = head
            head = node

        return head



