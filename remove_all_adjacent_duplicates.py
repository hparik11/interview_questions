# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: remove_all_adjacent_duplicates.py
# @Date:   9/21/20, Mon
"""
1209. Remove All Adjacent Duplicates in String II
Share
Given a string s, a k duplicate removal consists of choosing k adjacent and
equal letters from s and removing them causing the left and the right side
of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.



Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # if not s:
        #     return ""
        stack = []

        for ch in s:
            # print(ch, stack)
            if len(stack) > 0:
                if stack[-1][0] == ch:
                    if stack[-1][1] + 1 < k:
                        stack.append((ch, stack[-1][1] + 1))
                    else:
                        for _ in range(k - 1):
                            stack.pop()
                else:
                    stack.append((ch, 1))
            else:
                stack.append((ch, 1))

        return "".join([x for x, c in stack])


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates("abcd", 2))
    print(s.removeDuplicates("deeedbbcccbdaa", 3))
    print(s.removeDuplicates("pbbcggttciiippooaais", 2))
