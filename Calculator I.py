# Calculator I
# Task: https://py.checkio.org/en/mission/calculator-i/

import re
from collections import namedtuple

def get_number(str1:str, pos:int):
    print('get_number works')
    return 0

def calculator(log: str) -> str:
    MATH_SYMBOLS = '+-='
    # your code here
    Token = namedtuple('Token', ['type', 'value'])
 
# ќпредел€ем шаблоны
# NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)' # шаблон дл€ выражений типа 'foo = 1 + 1'
    EQ = r'(?P<EQ>=)'
    NUM = r'(?P<NUM>\d+)'
    PLUS = r'(?P<PLUS>\+)'
    MINUS = r'(?P<MINUS>\-)'
    MULTIPLY = r'(?P<MULTIPLY>\*)'
    DEVIDE = r'(?P<DEVIDE>\/)'
    WS = r'(?P<WS>\s+)'
 
 
    def generate_tokens(pat, text):
        scanner = pat.scanner(text)
        for m in iter(scanner.match, None):
            yield Token(m.lastgroup, m.group())
 
    master_pat = re.compile('|'.join([NUM, PLUS, MINUS, MULTIPLY, DEVIDE, WS, EQ]))
    actions = ['PLUS', 'MINUS', 'MULTIPLY', 'DEVIDE']
    MATH_SYMBOLS = '+-=*/'

    if log == '':  # check empty
        return '0'
    x = 0
    pos = 0
    action = 'PLUS'
    my_log = log
    print(f'{my_log=}')
    if my_log.find('=') >-1:  # check some '='
        if my_log[-1] == '=':   # '=' is last symbol
            my_log = str(my_log[my_log[:-1].rfind('=')+1:])
        else:    
            my_log = str(my_log[my_log.rfind('=')+1:])
    if my_log[-1] not in MATH_SYMBOLS:  # check MATH_SYMBOLS
        pos = max(my_log[:-1].rfind('-'), my_log[:-1].rfind('+'), my_log[:-1].rfind('/'), my_log[:-1].rfind('*'))
        if pos > -1:
            my_log = str(my_log[pos:])
    else:
        my_log = str(my_log[:-1])

    print(f'{my_log=}, {pos=}')
    
    for tok in generate_tokens(master_pat, my_log):
        print(tok, tok[1])
        if tok[0] in actions:
            action = tok[0]
        else:
            print(action)
            if action == 'PLUS':
                x += int(tok[1])
            elif action == 'MINUS':    
                x -= int(tok[1])
            elif action == 'DEVIDE':    
                x /= int(tok[1])
            elif action == 'MULTIPLY':    
                x *= int(tok[1])
    print(f'{x=}')
    return str(x)


print("Example:")
print(calculator("1+2"))

# These "asserts" are used for self-checking
assert calculator("000000") == "0"
assert calculator("0000123") == "123"
assert calculator("12") == "12"
assert calculator('000005+003') == '3'
assert calculator("=5=10=15") == "15"
assert calculator("12=") == "12"
assert calculator("+12") == "12"
assert calculator("-12") == "-12"
assert calculator("") == "0"
assert calculator("1+2=2") == "2"
assert calculator("1+2=") == "3"
assert calculator("1+2-") == "3"
assert calculator("1+2") == "2"
assert calculator("2+") == "2"

print("The mission is done! Click 'Check Solution' to earn rewards!")