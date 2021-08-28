#!/usr/bin/env python
# coding:utf-8
"""
@FileName : sort_stacks.py
@Author   : Harsh Parikh
@Date     : 8/7/21 10:11 PM

Given a stack, sort the elements in the stack using one additional stack.

eg.

sort([1, 3, 2, 4]) = [1, 2, 3, 4]

[1, 3, 5, 4, 2]
[2]

"""


def sort_stack(stack):
    new_stack = [stack.pop()]

    while stack:
        temp = stack.pop()
        while new_stack and temp > new_stack[-1]:
            stack.append(new_stack.pop())

        new_stack.append(temp)

    while new_stack:
        print(new_stack.pop(), end=' ')


if __name__ == '__main__':
    sort_stack([1, 3, 5, 4, 2])
