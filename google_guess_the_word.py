#!/usr/bin/env python
# coding:utf-8
"""
@FileName : google_guess_the_word.py
@Author   : Harsh Parikh
@Date     : 8/24/21 11:14 PM

843. Guess the Word

This is an interactive problem.

You are given an array of unique strings wordlist where wordlist[i] is 6 letters long, and one word in this list is chosen as secret.

You may call Master.guess(word) to guess a word. The guessed word should have type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word. Also, if your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have exactly 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or fewer calls to Master.guess and at least one of these guesses was secret, then you pass the test case.



Example 1:

Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"], numguesses = 10
Output: You guessed the secret word correctly.
Explanation:
master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
Example 2:

Input: secret = "hamada", wordlist = ["hamada","khaled"], numguesses = 10
Output: You guessed the secret word correctly.
"""


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: [str], master: 'Master') -> None:
        wordlist = list(set(wordlist))
        for _ in range(10):
            # Either take any random index word or first word in list
            guess_word = wordlist[0]
            matches = master.guess(guess_word)

            if matches == -1:
                continue

            candidates = []
            for word in wordlist:
                if matches == self._get_matches_between(guess_word, word):
                    candidates.append(word)

            wordlist = candidates

    def _get_matches_between(self, word1, word2):
        matches = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                matches += 1
        return matches
