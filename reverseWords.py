class Solution(object):
    def reverseWordsInString(self, string: str):
        # Write your code here.

        characters = list(string)

        # initially reverse characters for all string.
        self.reverseList(characters, 0, len(string) - 1)

        startOfWord = 0

        while startOfWord < len(string):
            endOfWord = startOfWord

            # Iterate through end of character for that word
            while endOfWord < len(string) and characters[endOfWord] != ' ':
                endOfWord += 1

            # reverse the characters from startword to endword
            self.reverseList(characters, startOfWord, endOfWord - 1)

            # Skip the spaces
            while endOfWord < len(string) and characters[endOfWord] == " ":
                endOfWord += 1
            startOfWord = endOfWord

        return "".join(characters)

    def reverseList(self, characters, startIndex, endIndex):
        while startIndex < endIndex:
            characters[startIndex], characters[endIndex] = characters[endIndex], characters[startIndex]
            startIndex += 1
            endIndex -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWordsInString("Let's take LeetCode contest"))
