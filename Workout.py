# Workout
# Task: https://py.checkio.org/en/mission/workout/

from typing import List
from math import ceil

def check_interval(l1: list, len1: int, points: int): # can list be divided into parts, max lemgth <= len1 
    #  points - points number
    remain = points # remained points
    for i in range(1, len(l1)):
        if l1[i] - l1[i-1] > len1: # too big interval, have to split
            remain = remain - ceil((l1[i] - l1[i-1]) / len1 ) + 1
#    print('Remained points:' , remain)
    if remain >= 0: # can be divided
        return True
    else: # not enougth points
        return False

def workout(sessions: List[int], additional: int) -> int:
    # your code here
    l2 = list(sessions)  
#    print(l2, additional)
    delta = 1
    ok = check_interval(l2, delta, additional) 
    while not ok:
        delta+=1
        ok = check_interval(l2, delta, additional) 
        print(f'{delta=}') 
    return delta