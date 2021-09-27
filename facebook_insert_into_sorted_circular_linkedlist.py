#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_insert_into_sorted_circular_linkedlist.py
@Author   : Harsh Parikh
@Date     : 9/17/21 1:20 AM
"""


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':

        if not head:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode

        prev, curr = head, head.next
        toInsert = False

        while True:

            if prev.val <= insertVal <= curr.val:
                # Case #1.
                toInsert = True
            elif prev.val > curr.val:
                # Case #2. where we locate the tail element
                # 'prev' points to the tail, i.e. the largest element!
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True

            if toInsert:
                prev.next = Node(insertVal, curr)
                # mission accomplished
                return head

            prev, curr = curr, curr.next
            # loop condition
            if prev == head:
                break

        # Case #3. all values in LL are same then insert into prev.next
        # did not insert the node in the loop
        prev.next = Node(insertVal, curr)
        return head
