class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)
        print(self.root)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        for i, ch in enumerate(string):
            self.createTrie(i, string)

    def createTrie(self, index, string):
        trie = self.root
        for j in range(index, len(string)):
            print(string[j])
            if string[j] in trie:
                trie = trie[string[j]]
            else:
                trie[string[j]] = {}
                trie = trie[string[j]]

        trie[self.endSymbol] = True

    def contains(self, string):
        # Write your code here.
        trie = self.root
        for ch in string:
            if ch not in trie:
                return False
            else:
                trie = trie[ch]

        return '*' in trie


if __name__ == '__main__':
    s = SuffixTrie("babc")
    print(s.contains('c'))
