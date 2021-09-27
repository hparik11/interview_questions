"""
211. Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.

#       time: O(N), N: number of letters in the word
#       space: O(N)
        """
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}

            node = node[ch]

        node['$'] = True

    def search(self, word: str) -> bool:
        node = self.root

        return self.dfs(node, word)

    def dfs(self, node, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.

        # time: (26 ^ N), worst case: ".....", this will have to search for all combinations of 26 characters
        # space: O(N), for recursion stack
        """

        for i, ch in enumerate(word):
            if ch not in node:
                # if the current character is '.'
                # check all possible nodes at this level
                if ch == '.':
                    for x in node:
                        if x != '$' and self.dfs(node[x], word[i + 1:]):
                            return True

                # if no nodes lead to answer
                # or the current character != '.'

                return False
            # if the character is found
            # go down to the next level in trie
            else:
                node = node[ch]

        return '$' in node


# class WordDictionary:
#
#     def __init__(self):
#         self.root = {}
#
#     def addWord(self, word: str) -> None:
#         node = self.root
#         for c in word:
#             if c not in node:
#                 node[c] = {}
#             node = node[c]
#         node['*'] = False
#
#     def search(self, w: str) -> bool:
#         def dfs(node, i):
#             if not node:
#                 return False
#
#             if i == L:
#                 return '*' in node
#
#             if w[i] != '.':
#                 if w[i] not in node:
#                     return False
#                 return dfs(node[w[i]], i + 1)
#
#             for j in node.values():
#                 if dfs(j, i + 1):
#                     return True
#
#             return False
#
#         node, L = self.root, len(w)
#         return dfs(node, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
obj = WordDictionary()
obj.addWord('apple')
# obj.addWord('apll')
param_2 = obj.search('appl.')
print(param_2)
