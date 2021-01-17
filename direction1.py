#from Salle import *
#from Salle import Salles



def direction ():
    #while (pour limiter le depacement de la map par rapport a gauche / d1roite)
    print("\n")
    a = input("Où voulez vous aller ? gauche ou droite (g/d) : ") 
    if a == 'd':
        return True

    elif a == 'g':
        return False
            


