# Task: https://py.checkio.org/ru/mission/evenly-spaced-trees/

from typing import List
from math import gcd
from functools import reduce

def evenly_spaced_trees(trees: List[int]) -> int:
    if len(trees) < 2:
        return 0
    spaces = []
    for i in range(1, len(trees)):
        spaces.append(trees[i] - trees[i-1])
    nod1 = reduce(gcd, spaces) 
    res = 0
    for item in spaces:
        res = res + item/nod1 -1
    return res


if __name__ == '__main__':
    print("Example:")
    print(evenly_spaced_trees([0, 2, 6]))
    assert evenly_spaced_trees([0, 2, 6]) == 1, 'add 1'
    assert evenly_spaced_trees([1, 3, 6]) == 3, 'add 3'
    assert evenly_spaced_trees([0, 2, 4]) == 0, 'no add'
    print("Coding complete? Click 'Check' to earn cool rewards!")
