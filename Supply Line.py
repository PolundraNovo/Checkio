# Task: https://py.checkio.org/en/mission/supply-line/
# Wave alghorith

def Form_Enemy_Set(enemies, All_Points):
    Upper = 'ACEGIK'
    for point in enemies:
        a , b = ord(point[0]), ord(point[1])
        All_Points[a - 65][b - 49] = -1  # unaccessible point     
        if point[1] > '1': # add points in same line
            All_Points[a - 65][b - 49 - 1] = -1  # unaccessible point        
        if point[1] < '9':  # add points in same line
            All_Points[a - 65][b - 49 + 1] = -1  # unaccessible point        
        if point[0] > 'A':
            All_Points[a - 65 - 1][b - 49] = -1  # unaccessible point        
            if point[0] in Upper:
                if point[1] > '1':
                    All_Points[a - 65 - 1][b - 49 - 1] = -1  # unaccessible point        
            elif point[1] < '9':   
                All_Points[a - 65 - 1][b - 49 + 1] = -1  # unaccessible point        
        if point[0] < 'L':
            All_Points[a - 65 + 1][b - 49] = -1  # unaccessible point        
            if point[0] in Upper:
                if point[1] > '1':
                    All_Points[a - 65 + 1][b - 49 - 1] = -1  # unaccessible point        
            elif point[1] < '9':   
                All_Points[a - 65 + 1][b - 49 +1] = -1  # unaccessible point        
    return

def Comp_Way(point, cur, All_Points):
    Upper = 'ACEGIK'
    x , y = ord(point[0])-65, ord(point[1])-49
    lim = 33
    All_Points[x][y] = cur
    
    if (point[1] > '1'): # add points in same line
        if cur < lim and (All_Points[x][y-1] == 0 or (All_Points[x][y-1] != -1 and All_Points[x][y-1] > cur+1)):
            Comp_Way(chr(x+65)+chr(y+49-1), cur+1, All_Points) 

    if point[1] < '9':  # add points in same line
        if (cur < lim) and (All_Points[x][y+1] == 0 or (All_Points[x][y+1] != -1 and All_Points[x][y+1] > cur+1)):
            Comp_Way(chr(x+65)+chr(y+49+1), cur+1, All_Points) 

    if point[0] > 'A' and (cur < lim):
        if (All_Points[x-1][y] == 0 or (All_Points[x-1][y] != -1 and All_Points[x-1][y] > cur+1)):
            Comp_Way(chr(x+65-1)+chr(y+49), cur+1, All_Points) 

        if point[0] in Upper:
            if point[1] > '1'  and  (All_Points[x-1][y-1] == 0 or (All_Points[x-1][y-1] != -1 and All_Points[x-1][y-1] > cur+1)):
                Comp_Way(chr(x+65-1)+chr(y+49-1), cur+1, All_Points) 
        elif point[1] < '9':      
            if (All_Points[x-1][y+1] == 0 or (All_Points[x-1][y+1] != -1 and All_Points[x-1][y+1] > cur+1)):
                Comp_Way(chr(x+65-1)+chr(y+49+1), cur+1, All_Points) 
    
    if point[0] < 'L'  and (cur < lim):
        if (All_Points[x+1][y] == 0 or (All_Points[x+1][y] != -1 and All_Points[x+1][y] > cur+1)):
            Comp_Way(chr(x+65+1)+chr(y+49), cur+1, All_Points) 
        if point[0] in Upper:
            if point[1] > '1' and (All_Points[x+1][y-1] == 0 or (All_Points[x+1][y-1] != -1 and All_Points[x+1][y-1] > cur+1)):
                Comp_Way(chr(x+65+1)+chr(y+49-1), cur+1, All_Points) 
        elif point[1] < '9':    
            if All_Points[x+1][y+1] == 0 or (All_Points[x+1][y+1] != -1 and All_Points[x+1][y+1] > cur+1):
                Comp_Way(chr(x+65+1)+chr(y+49+1), cur+1, All_Points) 
                    
    return All_Points

def supply_line(you, depots, enemies):
    Upper = 'ACEGIK'
    All_Points = [0] * 12
    for i in range(12):
        All_Points[i] = [0] * 9
    Form_Enemy_Set(enemies, All_Points)        
#    print(All_Points)
    
    All_Points = Comp_Way(you, 1, All_Points)
    # replace this for solution
    res = 0
    for point in depots:
        x , y = ord(point[0])-65, ord(point[1])-49        
        if All_Points[x][y] > 0:           
            if res == 0 or (res > All_Points[x][y]  and All_Points[x][y] > 0):
                  res = All_Points[x][y]
    if res == 0 or res == None:
        return None
    return res - 1


if __name__ == '__main__':
    assert supply_line("B4", {"F4"}, {"D4"}) == 6, 'simple'
    assert supply_line("G4",["I5","H7"],["D9","H6","J2","C9","L5","F1"]) == 2, 'Random 2'
    assert supply_line("I4",["L3","B5"],["G5","D7","F5","C8","A9","F2","C7"]) == 3, 'Random 1' 
#    assert supply_line("K4",["C6"],["I5","B5","E1","I3","C9"])
    assert supply_line("A3", {"A9", "F5", "G8"}, {"B3", "G6"}) == 11, 'multiple'
    assert supply_line("C2", {"B9", "F6"}, {"B7", "E8", "E5", "H6"}) is None, 'None'
    assert supply_line("E5", {"C2", "B7", "F8"}, set()) == 4, 'no enemies'
    assert supply_line("A5", {"A2", "B9"}, {"B3", "B7", "E3", "E7"}) == 13, '2 depots'
    print('"Run" is good. How is "Check"?')
