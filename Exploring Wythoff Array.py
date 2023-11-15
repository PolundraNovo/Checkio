# Task: https://py.checkio.org/en/mission/exploring-wythoff-array/

def wythoff_array(n: int) -> tuple[int, int]:
    string_num = 0 # number of string in array
    fi = 1.61803398875  # need many digits
    w_array = [0] * 100000
    while True:  # while all numbers don't processed
        # full 1st string
        if string_num == 0:  # for 1st string
            w_array[0] = 1
            w_array[1] = 2
        else:
            x = string_num + int((string_num + 1) * fi)
            w_array[0] = x
            w_array[1] = w_array[0] + int((string_num + 1) * fi)
        i = 2
        if w_array[0] == n:
            return (string_num, 0)
        if w_array[1] == n:
            return (string_num, 1)
        while w_array[i-1] + w_array[i-2] <= n:
            if w_array[i-1] + w_array[i-2] == n:
                return (string_num, i)
            w_array[i]  = w_array[i-1] + w_array[i-2]  # full i-th string
            i+=1
        string_num +=1    
    # your code here

print("Example:")
print(wythoff_array(3))

# These "asserts" are used for self-checking
assert wythoff_array(21) == (0, 6)
assert wythoff_array(9) == (3, 0)
assert wythoff_array(47) == (1, 5)
assert wythoff_array(1042) == (8, 8)
assert wythoff_array(39088170) == (14930352, 0)  # extra 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
