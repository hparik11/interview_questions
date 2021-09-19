def levenshteinDistance(str1, str2):
    # Write your code here.
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2

    curr = [0] * (len(small) + 1)
    pre = [0] * (len(small) + 1)

    for i in range(len(big) + 1):
        for j in range(len(small) + 1):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                curr[j] = curr[j - 1] + 1
            elif j == 0:
                curr[j] = curr[j] + 1
            elif small[j - 1] == big[i - 1]:
                curr[j] = pre[j - 1]
            else:
                curr[j] = min(pre[j - 1], curr[j], curr[j - 1]) + 1

        # https://stackoverflow.com/questions/4081561/what-is-the-difference-between-list-and-list-in-python
        """
        When reading, list is a reference to the original list, and list[:] shallow-copies the list.

        When assigning, list (re)binds the name and list[:] slice-assigns, replacing what was previously in the list.

        Also, don't use list as a name since it shadows the built-in.
        """
        pre = curr[:]

    return curr[-1]

    # small = str1 if len(str1) < len(str2) else str2
    # big = str1 if len(str1) >= len(str2) else str2
    # evenEdits = [x for x in range(len(small) + 1)]
    # oddEdits = [None for x in range(len(small) + 1)]
    # for i in range(1, len(big) + 1):
    #     if i % 2 == 1:
    #         currentEdits = oddEdits
    #         previousEdits = evenEdits
    #     else:
    #         currentEdits = evenEdits
    #         previousEdits = oddEdits
    #     currentEdits[0] = i
    #     # print(currentEdits, previousEdits)
    #     for j in range(1, len(small) + 1):
    #         if big[i - 1] == small[j - 1]:
    #             currentEdits[j] = previousEdits[j - 1]
    #         else:
    #             currentEdits[j] = 1 + min(previousEdits[j - 1], previousEdits[j], currentEdits[j - 1])

    # return oddEdits[-1] if i %2 == 1 else evenEdits[-1]


if __name__ == "__main__":
    print(levenshteinDistance('abc', 'yabd'))
