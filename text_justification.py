#!/usr/bin/env python
# coding:utf-8
"""
@FileName : text_justification.py
@Author   : Harsh Parikh
@Date     : 8/23/21 1:51 PM

68. Text Justification

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify(line, width, maxWidth):
            if len(line) == 1:
                return line[0] + ' ' * (maxWidth - width)
            else:
                spaces = maxWidth - width

                locations = len(line) - 1

                # Number of spaces distributed evenly between each word
                assign = locations * [spaces // locations]

                # Sharing the extra/remaining spaces among left hand side words
                for i in range(spaces % locations):
                    assign[i] += 1

                s = ''

                for i in range(locations):
                    s += line[i] + assign[i] * ' '

                s += line[-1]

                return s

        answer = []
        line, width = [], 0
        for w in words:
            if width + len(w) + len(line) <= maxWidth:
                line.append(w)
                width += len(w)
            else:
                answer.append(justify(line, width, maxWidth))
                line, width = [w], len(w)

        # For last word
        answer.append(' '.join(line) + (maxWidth - width - len(line) + 1) * ' ')

        return answer
