#!/usr/bin/env python
# coding:utf-8
"""
@FileName : apartment_hunting.py
@Author   : Harsh Parikh
@Date     : 8/4/21 3:55 PM

You’re looking to move into a new apartment, and you’re given a list of blocks where each block contains some services that it offers. In order to pick your apartment, you want to optimize its location in such a way that the maximum distance to any services that you care for is minimized.
Example —
blocks = [
{[
  {
    "gym": false,
    "school": true,
    "store": false
  },
  {
    "gym": true,
    "school": false,
    "store": false
  },
  {
    "gym": true,
    "school": true,
    "store": false
  },
  {
    "gym": false,
    "school": true,
    "store": false
  },
  {
    "gym": false,
    "school": true,
    "store": true
  }
]
requirements = [ “gym”, “school”, “store” ]

Output = 3
"""


def apartmentHunting(blocks, reqs):
    # Write your code here.

    maxFarthestDistance = [float('-inf') for _ in blocks]

    for i, block in enumerate(blocks):
        for req in reqs:
            closestDistance = float('inf')
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closestDistance = min(closestDistance, abs(j - i))

            maxFarthestDistance[i] = max(maxFarthestDistance[i], closestDistance)

    return maxFarthestDistance.index(min(maxFarthestDistance))


# O(br) time | O(br) space - where b is the number of blocks and r is the number of requirements

def apartmentHunting1(blocks, reqs):
    minDistancesFromBlocks = list(map(lambda req: getMinDistances(blocks, req), reqs))
    maxDistancesAtBlocks = getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks)

    return getIdxAtMinValue(maxDistancesAtBlocks)


def getMinDistances(blocks, req):
    minDistances = [0 for _ in blocks]
    closestReqIdx = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = distanceBetween(i, closestReqIdx)

    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = min(minDistances[i], distanceBetween(i, closestReqIdx))

    return minDistances


def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
    maxDistancesAtBlocks = [0 for block in blocks]
    for i in range(len(blocks)):
        minDistancesAtBlock = list(map(lambda distances: distances[i], minDistancesFromBlocks))
        maxDistancesAtBlocks[i] = max(minDistancesAtBlock)

    return maxDistancesAtBlocks


def getIdxAtMinValue(array):
    idxAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idxAtMinValue = i

    return idxAtMinValue


def distanceBetween(a, b):
    return abs(a - b)
