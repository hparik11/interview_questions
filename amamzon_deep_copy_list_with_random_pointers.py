# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: amamzon_deep_copy_list_with_random_pointers.py
# @Date:   10/19/20, Mon
"""
138. Copy List with Random Pointer
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.


Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return head

        p1 = head
        dic = {}
        while p1 is not None:
            newNode = Node(p1.val, None, None)
            dic[p1] = newNode
            p1 = p1.next

        p2 = head
        while p2 is not None:
            new_p2 = dic[p2]
            if p2.next is not None:
                new_p2.next = dic[p2.next]
            if p2.random is not None:
                new_p2.random = dic[p2.random]
            p2 = p2.next

        return dic[head]

#         mem = {}
#         def deepcopy(node):
#             if not node:
#                 return node

#             if node in mem:
#                 return mem[node]

#             new_node = mem[node] = Node(node.val)

#             new_node.next = deepcopy(node.next)
#             new_node.random = deepcopy(node.random)

#             return new_node

#         return deepcopy(head)
