def spiralTraverse(array):
    # Write your code here.
    if not array:
        return array
    if len(array) == 1:
        return array[0]
    firstRow = 0
    lastRow = len(array) - 1
    firstCol = 0
    lastCol = len(array[0]) - 1

    print(firstCol, lastCol, firstRow, lastRow)
    result = []
    while firstCol <= lastCol and firstRow <= lastRow:
        print(firstCol, lastCol, firstRow, lastRow)
        if firstCol < lastCol:
            for i in range(firstCol, lastCol + 1):
                result.append(array[firstRow][i])
            firstRow += 1

        if firstRow < lastRow:
            for i in range(firstRow, lastRow + 1):
                result.append(array[i][lastCol])
            lastCol -= 1

        if firstCol < lastCol and firstRow <= lastRow:
            for i in range(lastCol, firstCol - 1, -1):
                result.append(array[lastRow][i])
            lastRow -= 1

        if firstRow < lastRow and firstCol <= lastCol:
            for i in range(lastRow, firstRow - 1, -1):
                result.append(array[i][firstCol])
            firstCol += 1

        print(result)

    return result


if __name__ == '__main__':
    print(spiralTraverse([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]))
    print(spiralTraverse([[1]]))
    print(spiralTraverse([[1, 2, 3], [8, 9, 4], [7, 6, 5]]))
