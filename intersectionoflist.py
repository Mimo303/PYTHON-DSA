"""Q11. Write a function to find the intersection of two lists (common elements) without duplicates."""

def find_intersection(list1, list2):
    set1 = set(list1)
    intersection = []
    seen = set()

    for item in list2:
        if item in set1 and item not in seen:
            intersection.append(item)
            seen.add(item)

    return intersection

l1 = [1, 2, 2, 1, 4, 5]
l2 = [2, 2, 3, 4]
print(find_intersection(l1, l2))