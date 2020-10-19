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


# class TrieNode(object):
#     def __init__(self, val=None):
#         self.val = val
#         self.children = {}


# class WordDictionary:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = TrieNode()
#         self.curr = TrieNode()


#     def addWord(self, word: str) -> None:
#         """
#         Adds a word into the data structure.
#         """
#         node = self.root
#         for ch in word:
#             if ch not in node.children:
#                 node.children[ch] = TrieNode(ch)

#             node = node.children[ch]

#         node.children['/'] = TrieNode('/')

#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
#         """

#         for i in range(len(word)):
#             if word[i] != '.':
#                 if word[i] in root.children:
#                     root = root.children[word[i]]
#                 else:
#                     return False
#             else:
# 				#If the present char is a '.' then I visit all the children nodes in DFS manner to find match
#                 visitAll = root.children
#                 for child in visitAll:
#                     if self.search(root.children[child], word[i+1:]):
#                         return True
#                 return False
#         return (root.isWord == True)

class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['*'] = False

    def search(self, w: str) -> bool:
        def dfs(node, i):
            if not node:
                return False

            if i == L:
                return '*' in node

            if w[i] != '.':
                if w[i] not in node:
                    return False
                return dfs(node[w[i]], i + 1)

            for j in node.values():
                if dfs(j, i + 1):
                    return True

            return False

        node, L = self.root, len(w)
        return dfs(node, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
obj = WordDictionary()
obj.addWord('apple')
# obj.addWord('apll')
param_2 = obj.search('appl.')
print(param_2)
