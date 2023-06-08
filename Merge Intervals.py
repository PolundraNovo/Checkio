# Task: https://py.checkio.org/en/mission/merge-intervals/

def merge_intervals(intervals):
    """
        Merge overlapped intervals.
    """
    # Your code here
    cur_set, res = [], []
    if len(intervals) == 0:
        return []
    for item in intervals:
        if len(cur_set) == 0:  # 1st item 
            cur_set = list(item)
        else:
            if item[0] <= cur_set[1] + 1:
                if item[1] > cur_set[1]:
                    cur_set[1] = item[1]
            else:                   # new interval
                res.append(tuple(cur_set))
                cur_set = list(item)
    res.append(tuple(cur_set))    
    return res

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]) == [(1, 6), (8, 10), (12, 19)], "First"
    assert merge_intervals([(1, 12), (2, 3), (4, 7)]) == [(1, 12)], "Second"
    assert merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]) == [(1, 15), (17, 20)], "Third"
    print('Done! Go ahead and Check IT')