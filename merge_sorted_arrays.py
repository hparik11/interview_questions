import heapq
def mergeSortedArrays(arrays):
    # Write your code here.
    sortedList = []
    elementIdxs = [0 for _ in range(len(arrays))]
    
    while True:
        heapArray = []
        for index, each_array in enumerate(arrays):
            if elementIdxs[index] == len(each_array):
                continue
            heapArray.append((each_array[elementIdxs[index]], index))
        if len(heapArray) == 0:
            break
        heapq.heapify(heapArray)
        print(heapArray)
        minValue = heapq.heappop(heapArray)
        sortedList.append(minValue[0])
        elementIdxs[minValue[1]] += 1
    
    return sortedList

if __name__ == "__main__":
    print(mergeSortedArrays([[1, 5, 9, 21], [-1, 0], [-124, 81, 121], [3, 6, 12, 20, 150]]))