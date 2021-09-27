#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_min_operations.py
@Author   : Harsh Parikh
@Date     : 7/21/21 2:13 PM

Facebook | Minimizing Permutations


Here's a graph question on the Facebook recruiting portal:

Minimizing Permutations

In this problem, you are given an integer N, and a permutation, P of the integers from 1 to N, denoted as (a_1, a_2, ..., a_N). You want to rearrange the elements of the permutation into increasing order, repeatedly making the following operation:
Select a sub-portion of the permutation, (a_i, ..., a_j), and reverse its order.
Your goal is to compute the minimum number of such operations required to return the permutation to increasing order.

Signature

int minOperations(int[] arr)
Input
Array arr is a permutation of all integers from 1 to N, N is between 1 and 8

Output
An integer denoting the minimum number of operations required to arrange the permutation in increasing order
Example
If N = 3, and P = (3, 1, 2), we can do the following operations:
Select (1, 2) and reverse it: P = (3, 2, 1).
Select (3, 2, 1) and reverse it: P = (1, 2, 3).
output = 2


"""

from collections import defaultdict, deque


def minOperations(arr):
    # goal = ''.join(str(c) for c in sorted(arr))
    # start = ''.join(str(c) for c in arr)
    goal = sorted(arr)

    q = deque([arr])
    visited = set()
    visited.add(tuple(arr))
    levels = 0

    while q:
        for _ in range(len(q)):
            currWord = q.popleft()
            if currWord == goal:
                return levels  # currWord is sorted, return how many levels deep in the BFS.

            for i in range(len(currWord)-1):
                for j in range(i + 1, len(currWord)):
                    reverseList(currWord, i, j)
                    if tuple(currWord) not in visited:
                        visited.add(tuple(currWord))
                        q.append(currWord[:])

                    reverseList(currWord, i, j)  # revert the sublist back to original node state

        levels += 1

    return -1


def reverseList(characters, startIndex, endIndex):
    while startIndex < endIndex:
        characters[startIndex], characters[endIndex] = characters[endIndex], characters[startIndex]
        startIndex += 1
        endIndex -= 1


if __name__ == '__main__':
    print(minOperations([2, 3, 1]))
