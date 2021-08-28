# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: merge_two_sorted_list.py
# @Date:   9/27/20, Sun
"""
Merge Two Sorted Lists
Easy

4968

630

Add to List

Share
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = temp = ListNode(0)
        while l1 is not None and l2 is not None:  # 1

            if l1.val < l2.val:  # 2
                temp.next = l1  # 3
                l1 = l1.next  # 4
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2  # 5
        return dummy.next  # 6
