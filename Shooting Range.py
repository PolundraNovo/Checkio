# Task: https://py.checkio.org/ru/mission/shoot-range/

import math

def shot(wall1, wall2, shot_point, later_point):
    wall_lenght = math.sqrt((wall1[0] - wall2[0]) ** 2 + (wall1[1] - wall2[1]) **2) /2
    center = [(wall1[0] + wall2[0]) / 2, (wall1[1] + wall2[1]) / 2]
    if wall2[1] != wall1[1]:
        q = (wall2[0] - wall1[0]) / (wall1[1] - wall2[1])
        sn = (shot_point[0] - later_point[0]) + (shot_point[1] - later_point[1]) * q
        fn = (shot_point[0] - wall1[0]) + (shot_point[1] - wall1[1]) * q
        if sn == 0:
            return -1
        n = fn / sn
    else:
        n = (shot_point[1] - wall1[1]) / (shot_point[1] - later_point[1])
    dot = [shot_point[0] + (later_point[0] - shot_point[0]) * n,
    shot_point[1] + (later_point[1] - shot_point[1]) * n]
    offset = math.sqrt((dot[0] - center[0]) ** 2 + (dot[1] - center[1]) ** 2)
    if (shot_point[0] - later_point[0]) * (shot_point[0] - dot[0]) < 0:
        return -1
    res = round((wall_lenght - offset) / wall_lenght * 100)
    if res < 0:
        res = -1
    #replace this for solution
    return res

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert shot((2, 2), (5, 7), (11, 2), (8, 3)) == 100, "1st case"
    assert shot((2, 2), (5, 7), (11, 2), (7, 2)) == 0, "2nd case"
    assert shot((2, 2), (5, 7), (11, 2), (8, 4)) == 29, "3th case"
    assert shot((2, 2), (5, 7), (11, 2), (9, 5)) == -1, "4th case"
    assert shot((2, 2), (5, 7), (11, 2), (10.5, 3)) == -1, "4th case again"
    assert shot((2,2),(5,7),(8,3),(11,2)) == -1 # extra 0