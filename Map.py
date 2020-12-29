map = [ [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0] ]

def MapDiretion(Direction, Map):
    x=0
    y=0
    if Direction :
        map[y][x] = 0
        x = x + 1
        map[y][x] = 1
        for row in map:
            print(row)
        print("----------------")   
    else :
        map[y][x] = 0
        y = y + 1
        map[y][x] = 1
        for row in map:
            print(row)    
        print("----------------")   

def MapAZero(Map):
    x=0
    y=0 
    map[y][x] = 0 
    for row in map:
        print(row) 
    print("----------------")   

def MapDebut(Map):
    x=0
    y=0 
    map[y][x] = 1 
    for row in map:
        print(row) 
    print("----------------")  

def CoordonneX(Map):
    i=0
    while i < len(Map) :
        j=0
        while j < len(Map[i]):
            x = Map[i][j]
            print(x)
            return x    

def CoordonneY(Map):
    for y in Map[y] :
        return Map[y]    

#a = True
#b = False
#MapAZero(map)
#MapDebut(map)
#MapDiretion(a, map)
#CoordonneX(map)
#MapDiretion(b, map)
#CoordonneX(map)

