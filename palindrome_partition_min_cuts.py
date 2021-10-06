#!/usr/bin/env python
# coding:utf-8
"""
@FileName : palindrome_partition_min_cuts.py
@Author   : Harsh Parikh
@Date     : 7/25/21 4:29 PM

Given a non-empty string,
write a function that returns the minimum number of cuts
needed to perform on the string such that each remaining substring is a palindrome.
A palindrome is dened as a string that is written the same forward as backward.

Note that single-character strings are palindromes.

Sample input:"noonabbad"

Sample output: 2 ("noon | abba | d")


"""


def palindromePartitioningMinCuts(string):
    # Write your code here.
    """
    "noonabbd" -> noon | abba | d -> 2 cuts

              n o o n a b b a d
              0 1 2 3 4 5 6 7 8
        n   0 T F F T F F F F F
        o   1   T T F F F F F F
        o   2     T F F F F F F
        n   3 		T F F F F F
        a   4 		  T F F T F
        b   5           T F F F
        b   6             T F F
        a   7               T F
        d   8                 T

    """

    palindromes = [[False for _ in range(len(string))] for _ in range(len(string))]

    for i in range(len(string)):
        for j in range(i, len(string)):
            palindromes[i][j] = is_palindrome(string[i: j + 1])

    cuts = [float('inf') for _ in string]

    for j in range(len(string)):
        # print(cuts)
        if palindromes[0][j]:
            cuts[j] = 0
        else:
            cuts[j] = cuts[j - 1] + 1
            for i in range(1, j):
                if palindromes[i][j] and cuts[j] > 1 + cuts[i - 1]:
                    cuts[j] = 1 + cuts[i - 1]

    return cuts[-1]


def is_palindrome(string):
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False

        left += 1
        right -= 1

    return True


if __name__ == '__main__':
    print(palindromePartitioningMinCuts("noonabbad") == 2)
