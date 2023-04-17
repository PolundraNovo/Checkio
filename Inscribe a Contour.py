# https://py.checkio.org/ru/mission/inscribe-a-contour/
# Task: https://py.checkio.org/ru/mission/inscribe-a-contour/

from math import sqrt

def rotate(A,B,C):
    return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])

def grahamscan(A):  # Graham scan
# https://habr.com/ru/articles/144921/
    n = len(A) # points number
    P = list(range(n)) # list of points numbers
    for i in range(1,n):
        if A[P[i]][0]<A[P[0]][0]: # if point P[i] "more left" than point P[0]
            P[i], P[0] = P[0], P[i] # change them numbers
    for i in range(2,n): # sorting
        j = i
        while j>1 and (rotate(A[P[0]],A[P[j-1]],A[P[j]])<0): 
            P[j], P[j-1] = P[j-1], P[j]
            j -= 1
    S = [P[0],P[1]] # make a stack
    for i in range(2,n):
        while rotate(A[S[-2]],A[S[-1]],A[P[i]])<0:
            del S[-1] # pop(S)
        S.append(P[i]) # push(S,P[i])
    return S

def Rect_sq(a, b, c):
# a, b - base points, c - check point    
    print('---- Points ',a, b,  c,' ----')
    XY = [0, 0]
    if a[1] == b[1]:
        XY = [c[0], a[1]]
    elif a[0] == b[0]:   
        XY = [a[0], c[1]]
    else:    
        k0 = (b[1]- a[1]) / (b[0]- a[0])
        b0 = (a[1] * (a[0] + b[0]) - a[0] * (b[1] + a[1])) / (b[0] - a[0])
        k1 = - 1 / k0
        b1 = c[1] - k1 * c[0]  # perpendicular
#        print(' k0=',k0,'  b0=',b0)
#        print(' k1=',k1,'  b1=',b1)
        XY[0] = (b1-b0) / (k0-k1)
        XY[1] = XY[0] * k0 + b0
#    print('point 1: ',XY)
    if (XY[0] - a[0]) * (XY[0] - b[0]) > 0:  # need move
#        print('Need move')
        if (a[0] - b[0]) * (a[0] - XY[0]) > 0:  # move 2nd base point
            b = XY
        else:   # move 1st point
            a = XY
#    print('point 1a:', (a[0] - XY[0]) * (b[0] - XY[0]), (a[1] - XY[1]) * (b[1] - XY[1]))
    if (a[0] - XY[0]) * (b[0] - XY[0]) >0 and  (a[1] - XY[1]) * (b[1] - XY[1]) > 0:
   # length of 1st rectangle side         
        len1 = max(sqrt((a[0] - XY[0]) ** 2 + (a[1] - XY[1]) ** 2), sqrt((b[0] - XY[0]) ** 2 + (b[1] - XY[1]) ** 2))
    else:
    # perpendicular point is between base points    
#        print('point 1b')
        len1 = sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
 # length of 2nd rectangle side         
    len2 = sqrt((c[0] - XY[0]) ** 2 + (c[1] - XY[1]) ** 2)
#    print('len1 = ',len1,' len2=',len2,' s=',round(len1 * len2, 5))
    return len1, len2, XY

def inscribe(contour):
    # your code here
    print('='*50)
    s = grahamscan(contour)
    print(s)
    l1 = []
    len1, len2 = 0,0
    max1, max2 = 0,0
    ss = 1000
    for item in s:
        l1.append(contour[item])
    l1.append(l1[0])   # add 0th point twice
 #   print(l1)  #convex hull  
    # y = kb + b
    min_s = 500000000
    for i in range(1, len(l1)):
 #       print('')
#        print(f'**** Base points:{i-1} {i}   {l1[i-1]}   {l1[i]} ')
        max1, max2 = 0,0
        if len(l1) == 4:
            if i == 3:
                len1, len2, XY = Rect_sq(l1[2], l1[3], l1[1]) 
            else:                
                len1, len2, XY = Rect_sq(l1[i-1], l1[i], l1[i+1]) 
#            print('point 2 ', len1, len2, max1, max2, i)
            ss = len1 * len2
        else:    
            point1 = [l1[i-1][0], l1[i-1][1]]
            point2 = [l1[i][0], l1[i][1]]
            max1, max2 = 0,0
            for j in range(1, len(l1)):
# check mext points for max rectangle's square for THIS base points
#                print('square computing')
                if point1 != list(l1[j]) and point2 != list(l1[j]):
#                    print('*** 1 ***', point1, point2, list(l1[j]))
                    len1, len2, XY = Rect_sq(point1, point2, l1[j]) 
#                    print('*** 2 ***', point1, point2, XY)
                    if (XY[0] - point1[0]) * (XY[0] - point2[0]) > 0:  # need move
                        if (point1[0] - point2[0]) * (point1[0] - XY[0]) > 0:  # move 2nd base point
                            point2 = XY
                        else:   # move 1st point
                            point1 = XY
                    else: # need chech moving by Y only
                        if (XY[1] - point1[1]) * (XY[1] - point2[1]) > 0:  # need move
                            if (point1[1] - point2[1]) * (point1[1] - XY[1]) > 0:  # move 2nd base point
                                point2 = XY
                            else:     # move 1st point
                                point1 = XY
#                    print('*** 3 ***', point1, point2, XY)
#                    print('len1=',len1,' len2=',len2)
                    max1 = len1 if len1 > max1 else max1 
                    max2 = len2 if len2 > max2 else max2
                    print('max1=',max1,' max2=',max2)
            ss = max1 * max2
        print('current S=',round(ss,3))
        if ss >0 and ss< min_s:
            min_s = ss
    print('Res=',min_s)            
    return min_s


if __name__ == '__main__':
    print("Example:")
    print(inscribe([(1, 1), (1, 2), (0, 2), (3, 5), (3, 4), (4, 4)]))

    def close_enough(contour, answer):
        result = inscribe(contour)
        assert abs(result - answer) <= 1e-3, \
            f'inscribe({contour}) == {answer}, and not {result}'

    # These "asserts" are used for self-checking and not for an auto-testing
    close_enough([(6, 5), (10, 7), (2, 8)], 20.0)
    close_enough([(10, 250), (60, 300), (300, 60), (250, 10)], 24000.0)
    close_enough([[96,131],[213,146],[257,59],[55,282]], 26183.727749654856)
#    close_enough([[282,212],[160,290],[90,276],[288,140],[89,23],[46,252],[141,3],[183,284],[291,186],[7,171],[263,240],[191,21],[214,30],[17,208],[52,41],[32,223],[251,249],[24,88],[30,62],[107,20],[0,146],[107,284],[129,279],[16,115],[253,43],[289,128],[280,88],[272,60],[216,275],[162,9]],79849.548)
    close_enough([(0, 0), (0, 10), (0, 20), (100, 20), (100, 30), (120, 30), (120, 20), (120, 10), (20, 10), (20, 0)], 2679.208)
    close_enough([(2, 3), (3, 8), (8, 7), (9, 2), (3, 2), (4, 4), (6, 6), (7, 3), (5, 3)], 41.538)
    close_enough([(1, 1), (1, 2), (0, 2), (3, 5), (3, 4), (4, 4)], 6.0)
    close_enough([(10, 250), (60, 300), (110, 250), (160, 300), (210, 250), (160, 200), (300, 60), (250, 10)], 48000.0)
    print("Coding complete? Click 'Check' to earn cool rewards!")

