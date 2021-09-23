# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: amazon_merge_k_sorted_lists.py
# @Date:   10/18/20, Sun
"""
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""

from typing import List


class Solution(object):
    """
    Heap

    Complexity Analysis

        Time complexity : O(Nlog k)

        The comparison cost will be reduced to O(\log k)O(logk) for every pop and insertion to priority queue. But finding the node with the smallest value just costs O(1)O(1) time.
        There are NN nodes in the final linked list.
        Space complexity :

        O(n) Creating a new linked list costs O(n) space.
        O(k) The code above present applies in-place method which cost O(1)O(1) space. And the priority queue (often implemented with heaps) costs O(k)O(k) space (it's far less than NN in most situations).
    """

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        minHeap, index_node_map = [], {}

        for index, node in enumerate(lists):
            if node:
                index_node_map[index] = node
                heapq.heappush(minHeap, [node.val, index])

        head = prevNode = None

        while minHeap:
            currVal, currIndex = heapq.heappop(minHeap)
            tmpNode = ListNode(currVal)

            if not head:
                head = tmpNode
            else:
                prevNode.next = tmpNode

            prevNode = tmpNode

            if index_node_map[currIndex].next:
                index_node_map[currIndex] = index_node_map[currIndex].next
                heapq.heappush(minHeap, [index_node_map[currIndex].val, currIndex])

        return head

    """
    With mergesort
    
    Complexity Analysis

        Time complexity : O(N\log k) where \text{k}k is the number of linked lists.
        
        We can merge two sorted linked list in O(n) time where N is the total number of nodes in two lists.
        O(Nlogk)
        Space complexity : O(1)
        
        We can merge two sorted linked lists in O(1) space.
    """

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next
