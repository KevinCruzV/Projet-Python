from Salle import *
def droite():
    print("Vous avez choisis d'aller à droite")
    Vestiaire()

def gauche(): 
    print("Vous avez choisis d'aller à gauche")
    Vestiaire()

def direction ():
    a = int(input("Où voulez vous aller ? gauche ou droite (1/2)" ))
    while a != 1 or a != 2 
         a = int(input("Où voulez vous aller ? gauche ou droite (1/2)" ))

    if a == 1:
        droite()
    if a == 2:
        gauche()
    