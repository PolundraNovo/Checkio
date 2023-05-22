# Three Points Circle
# Task: https://py.checkio.org/ru/mission/three-points-circle/

def convert(str1):
    res1 = str1
    if str1[-2:] == '.0':
        res1 = str(str1[:-2])
    if res1[0] == '-':
        res1 = '+' + res1[1:]
    else:    
        res1 = "-" + res1
    return res1    
    

def checkio(data):
    str1 = data.replace('(','')
    str1 = str(str1.replace(')',''))
    my_tuple = tuple(str1.split(sep=','))
    x1, y1, x2, y2, x3, y3 = map(int, my_tuple)
    
    a = x2 - x1;
    b = y2 - y1;
    c = x3 - x1;
    d = y3 - y1;
    e = a * (x1 + x2) + b * (y1 + y2);
    f = c * (x1 + x3) + d * (y1 + y3);
    g = 2 * (a * (y3 - y2) - b * (x3 - x2));
    cx = (d * e - b * f) / g
    cy = (a * f - c * e) / g 
    r = ((x1 - cx) ** 2 + (y1 - cy) ** 2) ** 0.5
    r = round(((x1 - cx) ** 2 + (y1 - cy) ** 2) ** 0.5, 2)
    cx, cy = round(cx, 2), round(cy, 2)
    str_cx, str_cy, str_r = str(cx), str(cy), str(r)
    if str_r[-2:] == '.0':
        str_r = str(str_r[:-2])
    str_cx = convert(str_cx)
    str_cy = convert(str_cy)
    if cx != 0:
        res = '(x' + str_cx + ')^2+(y'
    else:
        res = '(x^2+(y'
    if cy != 0:
        res = res + str_cy
    res = res + ')^2=' + str_r + '^2'
    print(res)
    #replace this for solution
    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
    assert checkio("(6,6),(2,9),(1,6)") == "(x-3.5)^2+(y-6.83)^2=2.64^2"
