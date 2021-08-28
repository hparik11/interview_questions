#!/usr/bin/env python
# coding:utf-8
"""
@FileName : maximize_expression.py
@Author   : Harsh Parikh
@Date     : 7/5/21 7:01 PM

Maximum of Value Expression

arr1[a] - arr1[b] + arr1[c] - arr1[c]

where the maximum is taken over all a < b < c < d


Example 1:

Input: arr1 = [3, 6, 1, -3, 2, 7]
Output: 4

Choose a->6, b->-3, c-> 2, d->7
       6 - (-3) + 2 - 7 = 4

"""


def maximizeExpression(array):
    # Write your code here.
    if len(array) < 4:
        return 0

    maxOfA = [array[0]]

    for i in range(1, len(array)):
        currentMax = max(maxOfA[i - 1], array[i])
        maxOfA.append(currentMax)

    maxOfAMinusB = [float('-inf')]

    # Find Max A in first iteration
    for i in range(1, len(array)):
        currentMax = max(maxOfAMinusB[i - 1], maxOfA[i - 1] - array[i])
        maxOfAMinusB.append(currentMax)

    print(maxOfAMinusB)

    maxOfAMinusBPlusC = [float('-inf')] * 2

    for i in range(2, len(array)):
        currentMax = max(maxOfAMinusBPlusC[i - 1], maxOfAMinusB[i - 1] + array[i])
        maxOfAMinusBPlusC.append(currentMax)

    print(maxOfAMinusBPlusC)

    maxOfAMinusBPlusCMinusD = [float('-inf')] * 3

    for i in range(3, len(array)):
        currentMax = max(maxOfAMinusBPlusCMinusD[i - 1], maxOfAMinusBPlusC[i - 1] - array[i])
        maxOfAMinusBPlusCMinusD.append(currentMax)

    print(maxOfAMinusBPlusCMinusD)

    return maxOfAMinusBPlusCMinusD[-1]