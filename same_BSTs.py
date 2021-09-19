# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: same_BSTs.py
# @Date:   8/18/20, Tue


def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    if len(arrayOne) != len(arrayTwo):
        return False

    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    if arrayOne[0] != arrayTwo[0]:
        return False

    print(arrayOne, arrayTwo)
    leftSide1 = leftSideTreeElements(array=arrayOne, rootElement=arrayOne[0])
    leftSide2 = leftSideTreeElements(array=arrayTwo, rootElement=arrayTwo[0])

    rightSide1 = rightSideTreeElements(array=arrayOne, rootElement=arrayOne[0])
    rightSide2 = rightSideTreeElements(array=arrayTwo, rootElement=arrayTwo[0])

    return sameBsts(leftSide1, leftSide2) and sameBsts(rightSide1, rightSide2)


def leftSideTreeElements(array, rootElement):
    leftArray = []
    for i in range(1, len(array)):
        if array[i] < rootElement:
            leftArray.append(array[i])

    return leftArray


def rightSideTreeElements(array, rootElement):
    rightArray = []
    for i in range(1, len(array)):
        if array[i] >= rootElement:
            rightArray.append(array[i])

    return rightArray


if __name__ == '__main__':
    print(sameBsts([10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 81]))
