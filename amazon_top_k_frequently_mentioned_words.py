# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: amazon_top_k_frequently_mentioned_words.py
# @Date:   9/25/20, Fri
"""
Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in order of most to least frequently mentioned.

The comparison of strings is case-insensitive.
Multiple occurrences of a keyword in a review should be considred as a single mention.
If keywords are mentioned an equal number of times in reviews, sort alphabetically.

Example 1:

Input:
k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]

Output:
["anacell", "betacellular"]

Explanation:
"anacell" is occuring in 2 different reviews and "betacellular" is only occuring in 1 review.
Example 2:

Input:
k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]

Output:
["betacellular", "anacell"]

Explanation:
"betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" are occuring in 2 reviews, but "anacell" is lexicographically smaller.

"""
import string
from collections import defaultdict


class Solution:
    def topMentioned(self, k, keywords, reviews):
        def preprocess(word1):
            processed_word1 = ''
            for ch in word1:
                if ch not in string.punctuation:
                    processed_word1 += ch.lower()

            return processed_word1

        wordSet = set(keywords)
        counter = defaultdict(int)

        for review in reviews:
            words = review.split()
            seen = set()
            for word in words:
                processed_word = preprocess(word)
                if processed_word in wordSet and processed_word not in seen:
                    counter[processed_word] += 1
                    seen.add(processed_word)

        frequent_words = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
        print(frequent_words)
        return [x[0] for x in frequent_words[:k]]


if __name__ == '__main__':
    s = Solution()
    print(s.topMentioned(2, ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"], [
        "I love anacell Best services; Best services provided by anacell",
        "betacellular has great services",
        "deltacellular provides much better services than betacellular",
        "cetracular is worse than anacell",
        "Betacellular is better than deltacellular.",
    ]))

    print(s.topMentioned(2, ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"], [
        "Anacell provides the best services in the city",
        "betacellular has awesome services",
        "Best services provided by anacell, everyone should use anacell",
    ]))