"""Q1. Write a function to find the maximum and minimum element in a list without using built-in
max()/min()"""

def find_max_min(numbers):
    if not numbers:
        return None,None

    max_val = numbers[0]
    min_val = numbers[0]

    for num in numbers[1:]:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val

nums = [23, 5, 89, 12, 1, 45]
max_num, min_num = find_max_min(nums)

print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")