# Definition for singly-linked list.
"""
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        first = head

        cnt = 1
        while cnt < m - 1:
            first = first.next
            print(first.val)
            cnt += 1

        prev = None
        cur = first.next

        while cnt < n:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
            cnt += 1

        first.next.next = cur
        first.next = prev

        return head
