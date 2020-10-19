# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: length_of_last_word.py
# @Date:   9/15/20, Tue
"""
 Length of Last Word
Easy

782

2716

Add to List

Share
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5

"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        lastWordCharCount = 0
        count = 0
        i = 0
        while i < len(s):
            ch = s[i]
            if ch == ' ':
                if count != 0:
                    lastWordCharCount = count
                    count = 0
            else:
                count += 1

            i += 1

        return lastWordCharCount if count == 0 else count


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))
    print(s.lengthOfLastWord("  Hello World"))
    print(s.lengthOfLastWord("World"))
    print(s.lengthOfLastWord("  Hello World   "))
    print(s.lengthOfLastWord("  Hello World s"))