import math

def jump_search(arr, x):

    # Finding block size to be jumped 
    step = math.sqrt(len(arr))
    n = len(arr)

    # Finding the block where element is 
    # present (if it is present) 
    prev = 0
    while(arr[int(min(step, n))-1] < x):
        prev = step
        if step >= n:
            return -1
        step += math.sqrt(len(arr))
    
    # Doing a linear search for x in  
    # block beginning with prev. 
    while prev < n:
        # If element is found 
        if arr[int(prev)] == x:
            return int(prev)
        prev += 1
    
    return -1
        

if __name__ == "__main__":
    arr = [1, 2, 3, 9, 10, 20]
    element_idx = jump_search(arr, 20)
    print(element_idx)