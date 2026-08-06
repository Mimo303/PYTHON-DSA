"""Q3. Write a function to check if a list is sorted in ascending order."""

def is_sorted_ascending(arr):
    # an empty or single-element array is always sorted
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

print(is_sorted_ascending([1, 2, 3, 4, 5]))
print(is_sorted_ascending([1, 3, 2, 4, 5]))
print(is_sorted_ascending([2, 2, 2, 3, 3]))