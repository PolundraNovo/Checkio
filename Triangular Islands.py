#Task:
#https://py.checkio.org/en/mission/triangular-islands/

from typing import Set, Iterable
from math import sqrt, ceil

def sosed(x, max): # срусл neighbours
    print('-----------------', x, max)
    if x == 1:
        return [3]
    else:
        res = []
        k = ceil(sqrt(x)) # power 2 of current row
        print('point s1 ', x, (k-1) **2 + 1, (k **2) )
        if x > (k-1) **2 + 1: #check left neighbour
            res.append(x-1)
        if x < (k **2) : #check right neighbour
            res.append(x+1)
        if (k %2 == 0 and x%2 == 0) or (k %2 != 0 and x%2 != 0): #chech down neighbour
            if k ** 2 < max:
                res.append(x+2*k)            
        else: # check up neighbour
            res.append(x- (k-1)*2)
    return res

def deep1(item, tri, max, mas = None): 
    if not mas:
        mas = []
    l1 = sosed(item, max)
    if item not in mas: # if item not in result array
        mas.append(item)  # add item to array
    for it1 in l1:
        if (it1 not in mas) and (it1 in tri): # call recursion
            deep1(it1, tri, max, mas)
    return mas

def triangular_islands(triangles: Set[int]) -> Iterable[int]:
    
    tri = list(triangles)
    tri.sort()
    if (len(tri) == 1):
        return [1]
    res, res1 = [], []
    max_item = ceil(sqrt(tri[-1])) ** 2
    print(tri, max_item)

    for item in tri:
        if item !=0:
            res1 = deep1(item, tri, max_item, res1)
            res.append(list(res1))
            for i in range(len(tri)):
                if tri[i] in res1:  # if found new items
                    tri[i] = 0 # replace them by 0
            res1.clear()
            if tri.count(0) == len(tri): # if only zeros
                break  # exit from loop
    res1.clear()
    for item in res:
        res1.append(len(item))
    return res1

if __name__ == '__main__':
    print("Example:")
    print(sorted(triangular_islands({1})))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sorted(triangular_islands({1})) == [1]
    assert sorted(triangular_islands({4, 3})) == [2]
    assert sorted(triangular_islands([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,20,21,22,25,26,29,30,31,34,35,36,37,38,39,42,45,46,47,48,50,51,52,53,54,61,64,65,66,67,68,69,70,71,72,73,74,75,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,99,100])) ==   [8,9,24,33] 
    assert sorted(triangular_islands({4, 5, 6, 8})) == [2, 2]
    assert sorted(triangular_islands({1, 2, 6, 7, 8})) == [1, 4]
    assert sorted(triangular_islands({1, 4, 7, 8})) == [1, 3]
    assert sorted(triangular_islands({2, 3, 6})) == [3]
    assert sorted(triangular_islands({1, 2, 3, 4, 5, 6, 7, 8, 9})) == [9]
    assert sorted(triangular_islands({1, 2, 4, 5, 7, 9})) == [1, 1, 1, 1, 1, 1]
    assert sorted(triangular_islands([2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,24,25])) == [18]    
    print("Coding complete? Click 'Check' to earn cool rewards!")