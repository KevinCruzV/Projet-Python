map = [ [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0] ]

#Fonction de la map

def VoirMap(Map):
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

def DeplacementMapXGauche(Map):
    x=0
    y=0
    MapAZero(map)
    x = x + 1
    map[y][x] = 1
    for row in map:
        print(row)
    print("----------------")   
    
def DeplacementMapYDroite(Map):
    x=0
    y=0
    MapAZero(map)
    y = y + 1
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


# fonction de liste bidim


def Del1(L):
    c=0
    a=0
    for i in L:
        for j in L[i]:
            if j == 1:
                c = c + 1

    for a in range(c):
        L.remove(1)
        L.pop(0)





MapAZero(map)
MapDebut(map)
DeplacementMapXGauche(map)
DeplacementMapYDroite(map)
VoirMap(map)


