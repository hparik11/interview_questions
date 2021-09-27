#!/usr/bin/env python
# coding:utf-8
"""
@FileName : snap_phone_screen_regex_match.py
@Author   : Harsh Parikh
@Date     : 7/6/21 11:56 PM

Given a list of strings and a regex like string return all strings that match

Example:
['world', 'word', 'would', 'wont', 'which', 'hello']
'w3*d'

Would return 'world' and 'would' since there are 3 wildcards between w and d

'w2*d' would return 'word' since there are 2 wildcards between w and d


"""

import collections


class Trie:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['*'] = False

    def process(self, node, abbr, string, num):
        if not abbr and num == 0:
            if '*' in node:
                print(string)
            return

        if num != 0:
            for char, n in node.items():
                self.process(n, abbr, string + char, num - 1)

        elif abbr[0].isdigit():
            count = 0
            while abbr[0].isdigit():
                count = count * 10 + int(abbr[0])
                abbr = abbr[1:]

            self.process(node, abbr[1:], string, count)

        else:
            if node.get(abbr[0]):
                self.process(node[abbr[0]], abbr[1:], string + abbr[0], 0)


def helper(w, rex):
    stack = []
    num = 0
    carry = 0
    start = 0
    for i in range(len(rex)):
        if rex[i].isalpha():
            stack.append(rex[i])
            start += 1
        elif rex[i].isdigit():
            carry += 1
            num = num * 10 + int(rex[i])
        elif rex[i] == "*":
            try:
                stack.append(w[start:start + num])
                start = start + num
                num = 0
                carry = 0
            except:
                return False

    return True if "".join(stack) == w else False


def findmatch(words, rex):
    res = []
    for wd in words:
        if helper(wd, rex):
            res.append(wd)
    return res


if __name__ == '__main__':

    trie = Trie()

    wordList = ["world", "word", "would", "wont", "which", "hello", "baaaaaaaaaab"]
    abbrList = ['w3*d', "3*d", "4*", "5*", "b10*b", "b5*a4*b"]
    # Insert word into Trie
    for word in wordList:
        trie.addWord(word)

    print(trie.root)
    # # Check if abbr exist
    for abbr in abbrList:
        print(abbr)
        trie.process(trie.root, abbr, '', 0)
        print('--')
