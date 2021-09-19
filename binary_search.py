def binary_search(arr, l, r, x):
    if l > r:
        return -1
    else:
        mid = (l + r) // 2
        
        if arr[mid] < x:
            return binary_search(arr, mid+1, r, x)
        elif arr[mid] > x:
            return binary_search(arr, l, mid-1, x)
        elif arr[mid] == x:
            return mid
        else:
            return -1
            

if __name__ == "__main__":
    arr = [1, 2, 3, 9, 10, 20]
    element_idx = binary_search(arr, 0, len(arr) - 1, 1)
    print(element_idx)