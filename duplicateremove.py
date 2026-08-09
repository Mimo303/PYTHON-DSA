"""Q5. Write a function to remove duplicates from a list while preserving the original order."""

def remove_duplicates_preserve_order(arr):
    seen = set()
    result = []

    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

nums = [4, 5, 2, 5, 4, 3, 1, 2]
print(remove_duplicates_preserve_order(nums))