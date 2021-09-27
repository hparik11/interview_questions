# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: amazon_reorder_data_log_files.py
# @Date:   10/18/20, Sun
"""
937. Reorder Data in Log Files


Share
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.
"""


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sorting_algorithm(log):
            left_side, right_side = log.split(" ", 1)

            if right_side[0].isalpha():
                return 0, right_side, left_side
            else:
                return (1,)

        return sorted(logs, key=sorting_algorithm)

    def reorderLogFiles1(self, logs: List[str]) -> List[str]:

        letter_logs, number_logs = [], []
        for log in logs:
            if log.split()[1].isdigit():
                number_logs.append(log)
            else:
                letter_logs.append(log)

        letter_logs.sort(key=lambda x: x.split()[1:] + [x.split()[0]])
        return letter_logs + number_logs


if __name__ == '__main__':
    s = Solution()
    print(s.reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
