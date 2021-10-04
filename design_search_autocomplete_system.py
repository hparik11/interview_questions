#!/usr/bin/env python
# coding:utf-8
"""
@FileName : design_search_autocomplete_system.py
@Author   : Harsh Parikh
@Date     : 7/8/21 12:48 AM

642. Design Search Autocomplete System

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a
special character '#').

You are given a string array sentences and an integer array times both of length n where sentences[i] is a previously typed sentence and times[i] is the corresponding number of times the sentence was typed. For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Implement the AutocompleteSystem class:

AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.
List<String> input(char c) This indicates that the user typed the character c.
Returns an empty array [] if c == '#' and stores the inputted sentence in the system.
Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed. If there are fewer than 3 matches, return them all.


Example 1:

Input
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
Output
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]

Explanation
AutocompleteSystem obj = new AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]);
obj.input("i"); // return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
obj.input(" "); // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
obj.input("a"); // return []. There are no sentences that have prefix "i a".
obj.input("#"); // return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.
"""

from collections import defaultdict


class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        self.partial = []  # previously seen chars of current sentence
        self.matches = []  # matching sentences in decreasing frequency order

        self.counts = defaultdict(int)  # map from sentence to its frequency
        for sentence, count in zip(sentences, times):
            self.counts[sentence] = count

    def input(self, c):
        if c == "#":
            sentence = "".join(self.partial)
            self.counts[sentence] += 1
            self.partial = []  # reset partial and matches
            self.matches = []
            return []

        if not self.partial:  # first char of sentence
            self.matches = [(-count, sentence) for sentence, count in self.counts.items() if sentence[0] == c]
            self.matches.sort()
            self.matches = [sentence for _, sentence in self.matches]  # drop the counts
        else:
            i = len(self.partial)  # filter matches for c
            self.matches = [sentence for sentence in self.matches if len(sentence) > i and sentence[i] == c]

        self.partial.append(c)
        return self.matches[:3]


if __name__ == '__main__':
    # Your AutocompleteSystem object will be instantiated and called as such:
    obj = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
    param_1 = obj.input("i")
    param_2 = obj.input(" ")
    param_3 = obj.input("a")
    param_4 = obj.input("#")

    print(param_1, param_2, param_3, param_4)
