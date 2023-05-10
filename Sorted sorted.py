# Sort Sorted Groups
# Task: https://py.checkio.org/en/mission/sort-sorted-groups/

def sorted_groups(items: list[int]) -> list[int]:
    # your code here
    if len(items) < 3:
        return(items)
    ascend = True if items[1] > items[0] else False   # ascend sort
    res = []
    part = [items[0]]
    for i in range(1, len(items)):
        if (len(part) == 1) and (i < len(items)-1):
            part.append(items[i])
        else:    
            if ascend:
                if items[i] >= items[i-1]:
                    part.append(items[i])
                else:
                    res.append(part)  # add part to res
                    part = [items[i]]
            else: # descend sort
                if items[i] <= items[i-1]:
                    part.append(items[i])
                else:
                    res.append(part)  # add part to res
                    part = [items[i]]
        if items[i] != items[i-1]:
            ascend = True if items[i] > items[i-1] else False   # ascend sort
    res.append(part)    
    res.sort()
    res2 = [item for member in res for item in member]
    return res2


print("Example:")
print(sorted_groups([5, 1, 5, 0, 5]))

# These "asserts" are used for self-checking
assert sorted_groups([]) == []
assert sorted_groups([5]) == [5]
assert sorted_groups([1, 0, 1, 3, 1, 2, 2, 1]) == [1, 1, 0, 1, 2, 2, 1, 3]  # extra 3
assert sorted_groups([5, 1, 5, 0, 5]) == [5, 5, 0, 5, 1]
assert sorted_groups([5, 5, 1]) == [5, 5, 1]