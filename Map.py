def CreatMap() :
    Map = [ [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0] ]
    return Map

#Fonction de la map

def VoirMap(Map):
    for row in Map:
        print(row) 
    print("----------------")


def MapAZero(Map):
    x=0
    y=0 
    Map[y][x] = 0 
    for row in Map:
        print(row) 
    print("----------------")   

def MapDebut(Map):
    x=0
    y=0 
    Map[y][x] = 1 
    for row in Map:
        print(row) 
    print("----------------")

def DeplacementMapXGauche(Map):
    x=0
    y=0
    MapAZero(map)
    x = x + 1
    Map[y][x] = 1
    for row in Map:
        print(row)
    print("----------------")   
    
def DeplacementMapYDroite(Map):
    x=0
    y=0
    MapAZero(map)
    y = y + 1
    Map[y][x] = 1
    for row in Map:
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








