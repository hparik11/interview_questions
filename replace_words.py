"""
648. Replace Words

In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
"""

from typing import List


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = '*'

    def add(self, word):
        current = self.root

        for ch in word:
            if ch not in current:
                current[ch] = {}
            current = current[ch]

        current[self.endSymbol] = word

    def search(self, word):
        node = self.root
        for ch in word:
            if self.endSymbol in node:
                return node[self.endSymbol]
            elif ch not in node:
                return word
            else:
                node = node[ch]

        return word


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = Trie()

        for each in dict:
            trie.add(each)
        output = []
        sentence_split = sentence.split()

        for word in sentence_split:
            # print(trie.search(word))
            output.append(trie.search(word))

        print(output)
        return ' '.join(output)


if __name__ == "__main__":
    s = Solution()
    print(s.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery"))
