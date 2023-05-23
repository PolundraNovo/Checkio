# Humpty Dumpty Form
# Task: https://py.checkio.org/en/mission/humpty-dumpty/

import math

def checkio(height, width):
    pi = 3.141592653589793238462643383279
    w1 = width / 2
    h1 = height / 2
    v = round(4/3 *  pi * w1 * w1 * h1, 2)
    if w1 > h1: # Oblate spheroid
        x = math.log(((w1*w1 - h1*h1) ** 0.5 + w1)  / h1)
        s = round(((x * h1*h1/(w1*w1-h1*h1)**0.5 + w1) * 2 * pi * w1), 2)
    elif w1 < h1:   #  Prolate spheroid    
        x = math.asin(((h1*h1-w1*w1) ** 0.5) / h1)
        s = round((x * h1*h1 / ((h1*h1-w1*w1) ** 0.5) + w1) * 2*pi*w1, 2)
    else: #shere
        s = round(4 * pi * w1 * w1, 2)
#    print([v, s]) 
    return [v, s]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    