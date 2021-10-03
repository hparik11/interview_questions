#!/usr/bin/env python
# coding:utf-8
"""
@FileName : find_all_prime_numbers_before_n.py
@Author   : Harsh Parikh
@Date     : 10/2/21 6:13 PM


"""
import math


def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True

    idx = 2
    while idx <= math.sqrt(number):
        if number % idx == 0:
            return False

        idx += 1

    return True


# O(N * sqrt(N))
def find_all_primes(n):
    all_primes = []
    for i in range(n + 1):
        if is_prime(i):
            all_primes.append(i)

    return all_primes


"""
Time: N * Log(LogN)
    
    for every curr:  
        find multiples if prime ->  N/2 + N/3 + N/5 + N/7 + N/11 ..... = Log(LogN) -> harmonic series for prime
        
"""


def find_all_primes1(n):
    # initialize all values true
    primes = [True] * (n + 1)
    # start from 2 and iterate until sqrt(n)
    for curr in range(2, int(math.sqrt(n)) + 1):
        # if true the find all values multiple of current value
        # and mark them as prime=false so we won't iterate them
        if primes[curr]:
            # start from double of current value and
            # increment would be same as current value
            for j in range(curr * 2, n + 1, curr):
                primes[j] = False

    all_primes = []

    for val in range(2, n + 1):
        if primes[val]:
            all_primes.append(val)

    return all_primes


if __name__ == '__main__':
    # print(find_all_primes(37))
    print(find_all_primes1(37))
