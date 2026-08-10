"""Q12. Write a function to calculate the running sum (prefix sum) of a list"""

def running_sum(nums):
    prefix_sum = []
    current_sum = 0

    for num in nums:
        current_sum += num
        prefix_sum.append(current_sum)

    return prefix_sum

arr = [1, 2, 3, 4]
print(running_sum(arr))