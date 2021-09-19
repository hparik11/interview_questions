"""
208. Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""


class TrieNode(object):
    def __init__(self, val=None):
        self.val = val
        self.children = {}


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode(ch)

            node = node.children[ch]

        node.children['/'] = TrieNode('/')

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root

        for ch in word + '/':
            if ch in node.children:
                node = node.children[ch]
                continue
            else:
                return False

        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root

        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
                continue
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
obj.insert('apll')
param_2 = obj.search('apll')
print(param_2)
param_3 = obj.startsWith('ape')
print(param_3)
