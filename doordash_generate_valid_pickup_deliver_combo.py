#!/usr/bin/env python
# coding:utf-8
"""
@FileName : doordash_generate_valid_pickup_deliver_combo.py
@Author   : Harsh Parikh
@Date     : 9/30/21 11:51 AM

"""


def generateValidPickupDeliveriesCombination(n):
    if n is None or n == 0:
        return []

    if n == 1:
        return ['P1', 'D1']

    res = []
    pickup = set()
    delivery = set()
    dfs(n, [], res, pickup, delivery)

    return res


def dfs(n, curr, res, pickup, delivery):
    if len(curr) == n * 2:
        res.append(curr)
        return

    for i in range(n):
        if i not in pickup:
            pickup.add(i)
            dfs(n, curr + ['P' + str(i + 1)], res, pickup, delivery)
            pickup.remove(i)

    for j in range(n):
        if j in pickup and j not in delivery:
            delivery.add(j)
            dfs(n, curr + ['D' + str(j + 1)], res, pickup, delivery)
            delivery.remove(j)

    return


if __name__ == '__main__':

    all_combo = generateValidPickupDeliveriesCombination(3)

    print(all_combo)
