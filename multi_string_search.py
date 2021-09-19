# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: multi_string_search.py
# @Date:   9/5/20, Sat
class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = '*'

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]

        node[self.endSymbol] = word


def search(bigString, startIndex, trie, results):
    node = trie.root
    for i in range(startIndex, len(bigString)):
        ch = bigString[i]
        if ch not in node:
            break

        node = node[ch]

        if trie.endSymbol in node:
            results[node[trie.endSymbol]] = True


def multiStringSearch(bigString, smallStrings):
    # Write your code here.

    trie = Trie()
    for word in smallStrings:
        trie.insert(word)

    results = {}
    for i in range(len(bigString)):
        search(bigString, i, trie, results)

    final_results = [False for _ in range(len(smallStrings))]
    for i, word in enumerate(smallStrings):
        if word in results:
            final_results[i] = results[word]

    return final_results


if __name__ == '__main__':
    print(multiStringSearch("this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]))
