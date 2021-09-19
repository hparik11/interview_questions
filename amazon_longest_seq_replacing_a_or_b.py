#!/usr/bin/env python
# coding:utf-8
"""
@FileName : amazon_longest_seq_replacing_a_or_b.py
@Author   : Harsh Parikh
@Date     : 8/4/21 4:51 PM
"""

"""
You are given with a string of 'a' and 'b' only in it. 
You can replace either 'a' to 'b' or vise-versa, as long as they are consecutive. 
Return [start and end index] from that string which you will replace in such a way 
that will give you longest seq either with 'a'(s) / 'b'(s) in the original string. 

*** You cannot modify the original string itself.

example:

i/p: "aaaaabbbaaaabbbbbbbbbbaaaaaaa"
expected out: [12,22] ## if we replace second pattern, then it will give longest seq of 'a' i.e 'aaaaaaaaaaaaaaaaaaaaa', 
Note: end index is not inclusive.
"""


def find_longest_seq_after_replacing_a_or_b(input_string):
    """

    can be solved with sliding window technique. It's easier to see when you preprocess the letters
    into a list of integers where each integer is the length of each subsequence of consecutive
    a's or b's. "aaaaabbbaaaabbbbbbbbbbaaaaaaa" => [5, 3, 4, 10, 7] (5 a's, 3 b's, 4 a's, 10 b's, 7 a's).
    You then find the window of size k = 3 which has the largest sum.* Here, it's [4, 10, 7], which corresponds to the subsequence "aaaabbbbbbbbbbaaaaaaa".
    The middle number is the subsequence that gets flipped ("bbbbbbbbbb", from idx 12 to 22), so that's your answer (you can preprocess this part when you're building up the numbers list).

    (Why k = 3? Because of the way we processed the counts, k = 3 will mean we are checking subsequences of [a, b, a] and switching the b's to a's, or checking [b, a, b] and switching the a's to b's).
    """
    startIdx = 0
    sequence_indexes = []
    input_string_length = len(input_string)

    for idx in range(1, input_string_length):
        if input_string[idx] != input_string[idx - 1]:
            sequence_indexes.append((idx - startIdx, startIdx, idx))
            startIdx = idx

    if input_string_length - startIdx > 0:
        sequence_indexes.append((input_string_length - startIdx, startIdx, input_string_length))

    print(sequence_indexes)
    print(find_longest_sequence_with_largest_sum(sequence_indexes))


def find_longest_sequence_with_largest_sum(sequences):
    if len(sequences) == 1:
        return sequences[0][1], sequences[0][2]

    longest_sequence_sum = 0
    sequence = None
    idx = 1

    while idx < len(sequences) - 1:
        prevSeq = sequences[idx - 1][0]
        currSeq = sequences[idx][0]
        nextSeq = sequences[idx + 1][0]

        currentSum = prevSeq + currSeq + nextSeq
        if currentSum > longest_sequence_sum:
            longest_sequence_sum = currentSum
            sequence = (sequences[idx][1], sequences[idx][2])

        idx += 1

    return sequence


if __name__ == '__main__':
    find_longest_seq_after_replacing_a_or_b("aaaaabbbaaaabbbbbbbbbbaaaaaaa")
    find_longest_seq_after_replacing_a_or_b("aaaaabbbbbbbbbbbbbaaaabbbbbbbbbbbbbbbbbbbaaaaaaaa")
