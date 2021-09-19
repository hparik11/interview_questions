# import math

# def findDistance(points1, points2):
#     return math.sqrt((points1[0] - points2[0]) ** 2 + (points1[1] - points2[1]) ** 2)

# def findAvergae(points1, points2, points3):
#     return sum(findDistance(points1, points2), findDistance(points2, points3), findDistance(points1, points3)) / 3

# def isAlmostPalindrom(input_str):
#     allowOneCharacter = False
#     isPalindrome = False
#     for index in range(len(input_str) // 2):
#         if input_str[index] == input_str[len(input_str) - index - 1]:
#             continue
#         else:
#             if allowOneCharacter:
#                 return False
#             else:
#                 allowOneCharacter = True

#     return True

# def mostPopularNumber(input_array, lenth):
#     if len(input_array) == 0:
#         return None

#     freqDictn = {}

#     for elem in input_array:
#         if elem in freqDictn:
#             freqDictn[elem] += 1
#         else:
#             freqDictn[elem] = 1

#     sortedFreqTuples = sorted(freqDictn.items(), key=lambda x: x[1], reverse=True)

#     if len(sortedFreqTuples) == 1:
#         return sortedFreqTuples[0][0]
#     else:
#         firstElement = sortedFreqTuples[0][0] 
#         secondElement = sortedFreqTuples[1][0]
#         firstElementFrequency = sortedFreqTuples[0][1]
#         secondElementFrequency = sortedFreqTuples[1][1]

#         if firstElementFrequency == secondElementFrequency:
#             return firstElement if firstElement < secondElement else secondElement
#         else:
#             return firstElement


# def findOccurance(arr, int):
#     count = 0
#     for elem in arr:
#         if elem == int:
#             count += 1
#     return count

# def do_hoping(arr=list(range(0, 20))):
#     a = 19
#     for start_index in range(0, a, 5):
#         end_index = min(start_index + 5, a)
#         print(start_index, end_index, end_index - start_index)
#         print(arr[start_index: end_index])


# def flatten(self, root: TreeNode) -> None:
#     """
#     Do not return anything, modify root in-place instead.
#     """
#     if root is not None:
#         stack = [root]
#         prev = None
#         while len(stack) != 0:
#             cur = stack.pop()
#             # Handle non-root here
#             if prev != None:
#                 prev.left = None
#                 prev.right = cur
#             prev = cur
#             if cur.right != None:
#                 stack.append(cur.right)
#             if cur.left != None:
#                 stack.append(cur.left)


def foo(n):
    def multiplier(x):
        return x * n

    return multiplier


a = foo(5)
b = foo(5)

# print(a(b(2)))
print(a)

# if __name__ == '__main__':
#     # print(isAlmostPalindrom('abccfg'))
#     # print(mostPopularNumber([66], 1))
#     # print(findOccurance([2, 3, 4, 3, 2, 1], 1))
#     print(do_hoping())
