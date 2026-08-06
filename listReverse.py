def reverse_in_place(arr):
    left = 0
    right = len(arr)-1

    #swap elements from outer boundaries moving inward
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -=1

nums = [10, 20, 30, 40, 50]
reverse_in_place(nums)
print(nums)