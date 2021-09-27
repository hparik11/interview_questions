"""
We begin by comparing the first two elements of the list. 
If the first element is larger than the second element, we swap them. 
If they are already in order we leave them as is. We then move to the next pair of elements, compare their values and swap as necessary. 
This process continues to the last pair of items in the list.

Upon reaching the end of the list, it repeats this process for every item. 
Though, this is highly inefficient. What if only a single swap needs to be made in the array? Why would we still iterate though it n^2 times, even though it's already sorted?

Obviously, to optimize the algorithm, we need to stop it when it's finished sorting.

How would we know that we're finished sorting? If the items were in order then we would not have to swap items. So, whenever we swap values we set a flag to True to repeat sorting process. If no swaps occurred, the flag would remain False and the algorithm would stop.

Time Complexity
In the worst case scenario (when the list is in reverse order), this algorithm would have to swap every single item of the array. Our swapped flag would be set to True on every iteration. Therefore, if we have n elements in our list, we would have n iterations per item - thus Bubble Sort's time complexity is O(n^2).

"""


def bubbleSort(array):
    # Write your code here.
    # We set swapped to True so the loop looks runs at least once
    for _ in range(len(array)):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                # Swap the elements
                array[i], array[i + 1] = array[i + 1], array[i]
                # Set the flag to True so we'll loop again

        return array


# Verify it works
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)
