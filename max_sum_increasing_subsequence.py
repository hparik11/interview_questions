def maxSumIncreasingSubsequence(array):
    # Write your code here.
    sumArray = array[:]
    maxSum = float('-inf')
    maxSumIndex = 0
    sequences = [None] * len(array)

    for i in range(len(array)):
        currNum = array[i]
        for j in range(i):
            otherNum = array[j]
            if otherNum < currNum and sumArray[j] + currNum > sumArray[i]:
                sumArray[i] = sumArray[j] + currNum
                sequences[i] = j

        if maxSum < sumArray[i]:
            maxSum = sumArray[i]
            maxSumIndex = i

    print(maxSum, maxSumIndex)
    print(sumArray)
    print(sequences)

    sequence = sequences[maxSumIndex]
    final_ans = [array[maxSumIndex]]
    while sequence is not None:
        final_ans.append(array[sequence])
        sequence = sequences[sequence]

    print(list(reversed(final_ans)))
    return list(reversed(final_ans))


if __name__ == "__main__":
    maxSumIncreasingSubsequence([8, 12, 2, 3, 15, 5, 7])
