# Task: https://py.checkio.org/en/mission/knapsack-problem-2/

def knapsack02(w, p, k, weight, n):    
    a = [[0 for i in range(weight+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(0, weight + 1):
            for cnt in range(min(k[i-1], weight // w[i-1]) + 1):
                if w[i-1] * cnt <= j:
                    a[i][j] = max(a[i][j], a[i - 1][j - w[i-1] * cnt] + p[i-1] * cnt)
    return a[-1][-1]

def knapsack(weight: int, items: list[tuple[int, int] | tuple[int, int, int]]) -> int:
    res = 0
    cur_items =  [list(x) for x in items if x[1] <= weight]
    # check too large items
    print(f'{cur_items=}')
    if len(cur_items) == 0:
        return 0
    for item in cur_items:
        if len(item) == 2:
            item.append(999)
    counts = [999] * len(cur_items)
    counts = [x[2] for x in cur_items if len(x) == 3]   # count of each item
    w = [x[1] for x in cur_items]
    p = [x[0] for x in cur_items]
    res = knapsack02(w,p, counts, weight, len(cur_items))    
    # your code here
    return res


print("Example:")
print(knapsack(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]))

# These "asserts" are used for self-checking
assert knapsack(8, [(10, 10, 3)]) == 0
assert knapsack(9, [(2, 1, 2), (3, 1), (5, 2)]) == 27
assert knapsack(5, [(4, 2, 1), (6, 6, 2), (5, 2, 1), (2, 1, 1), (8, 3, 1)]) == 13
assert knapsack(5, [(4, 2, 1), (5, 2, 1), (2, 1, 1), (8, 3, 1)]) == 13
assert knapsack(8, [(4, 2), (5, 2), (2, 1), (8, 3)]) == 21
assert knapsack(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]) == 12


print("The mission is done! Click 'Check Solution' to earn rewards!")