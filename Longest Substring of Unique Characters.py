# Task: https://py.checkio.org/en/mission/longest-substring-of-unique-characters/

def longest_substr(s: str) -> int:
    if len(s) < 2:
        return len(s)
    max = s[0]
    cur_max = s[0]
    for i in range(len(s)-1):
        if s[i+1] not in cur_max:  # not same char
            cur_max += s[i+1]
        else:
            x = (cur_max.find(s[i+1]))
            if len(cur_max) > len(max):
                max = cur_max
            cur_max = cur_max[x+1:] + s[i+1]    #  del first (cur_max.find(s[i+1])) symbols
    if len(cur_max) > len(max):
        max =  cur_max
    # your code here
    return len(max)


print("Example:")
print(longest_substr("abcabcbb"))

# These "asserts" are used for self-checking
assert longest_substr("abcabcbb") == 3
assert longest_substr("bbbbb") == 1
assert longest_substr("pwwkew") == 3
assert longest_substr("abcdef") == 6
assert longest_substr("") == 0
assert longest_substr("au") == 2
assert longest_substr("dvdf") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")