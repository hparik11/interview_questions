#!/usr/bin/env python
# coding:utf-8
"""
@FileName : facebook_count_valid_pickup_delivery_options.py
@Author   : Harsh Parikh
@Date     : 9/13/21 2:14 PM

1359. Count All Valid Pickup and Delivery Options
Hard

391

52

Add to List

Share
Given n orders, each order consist in pickup and delivery services.

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i).

Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
Example 2:

Input: n = 2
Output: 6
Explanation: All possible orders:
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
Example 3:

Input: n = 3
Output: 90
"""

"""
Consider n = 3 orders.

Now consider one particular sequence; S = [(P1, D1), (P2, D2), (P3, D3)]
Now let us consider an arrangement like this, where P1 comes before P2 and P2 comes before P3, i.e., P1 ... P2 ... P3 ...
Now we observe that -

D3 can only be placed in one position (1 ways), i.e., at the last after P3. So, the sequence becomes - P1 ... P2 ... P3 ... D3 ...
D2 can be placed at any one of three positions (3 ways), i.e., between P2 and P3, or between P3 and D3, or after D3. So, one of the sequence becomes - P1 ... P2 ... P3 ... D2 ... D3 ...
D1 can be placed at any one of the above five positions (5 ways).
So, for the above particular sequence S we have - 1 * 3 * 5 = 15 ways.
But the sequence can be arranged in 3! ways. So, the ans is 3! * (1 * 3 * 5).

In general, the ans is - n! * (1 * 3 * 5 * ... * (2*n-1)).

Time Complexity - O(n)
Space Complexity - O(1)
"""


class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        p = 1000_000_007
        for i in range(1, n + 1):
            res *= i * (2 * i - 1)
            res = res % p
        return res
