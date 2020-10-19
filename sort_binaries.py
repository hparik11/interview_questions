# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: sort_binaries.py
# @Date:   9/29/20, Tue

# Please enter your solution below
def sort_binaries(arr):
    # TODO: Implementation here
    if len(arr) < 2:
        return arr

    i = 0
    j = len(arr) - 1

    while i < len(arr) and j > 0:
        while arr[i] != 1:
            i += 1
        while arr[j] != 0:
            j -= 1

        print(i, j)
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]

    return arr


if __name__ == '__main__':
    print(sort_binaries([1, 0, 1, 0, 1, 1, 0]))
    print(sort_binaries([0, 0, 1, 1, 0, 1, 0]))
    print(sort_binaries([1, 1, 1, 0, 0, 0, 1]))
