#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_counting_inversions.py
@Author   : Harsh Parikh
@Date     : 9/6/21 11:48 AM

We can determine how "out of order" an array A is by counting the number of inversions it has.
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j.
That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions.
 The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3).
 The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
"""


def mergeSortInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr) // 2]
        b = arr[len(arr) // 2:]

        a, ai = mergeSortInversions(a)
        b, bi = mergeSortInversions(b)

        inversions = ai + bi
        c = []
        i = 0
        j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a) - i)

    c += a[i:]
    c += b[j:]

    return c, inversions


if __name__ == '__main__':
    print(mergeSortInversions([2, 4, 1, 3, 5]))
    print(mergeSortInversions([5, 4, 3, 2, 1]))
