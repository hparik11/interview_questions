"""
1268. Search Suggestions System

Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.node = {}
        self.suggestions = set()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, product):
        trie = self.root
        for ch in product:
            if ch in trie.node:
                trie = trie.node[ch]
            else:
                trie.node[ch] = TrieNode()
                trie = trie.node[ch]

            trie.suggestions.add(product)

    def search(self, keyword):
        result_suggestions = []
        trie = self.root
        found = False
        for ch in keyword:
            if ch not in trie.node or found:
                result_suggestions.append([])
                found = True
            else:
                trie = trie.node[ch]
                result_suggestions.append(sorted(trie.suggestions)[:3])

        return result_suggestions


class Solution:

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        productTrie = Trie()
        for product in products:
            productTrie.insert(product)

        return productTrie.search(searchWord)


if __name__ == "__main__":
    s = Solution()
    print(s.suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))
