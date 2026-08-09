"""Q8. Write a function to merge two sorted lists into a single sorted list without using the sort() function."""

def merge_two_sorted_lists(list1, list2):
    i = 0
    j = 0
    merged = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    #Append remaining elements if list1 is not exhausted
    while i < len(list1):
        merged.append(list1[i])
        i += 1

    #Append remaining elements if list2 is not exhausted
    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged

l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8, 10]
print(merge_two_sorted_lists(l1, l2))
