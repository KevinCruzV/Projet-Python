def direction (a):
    a = input("Où voulez vous aller ? gauche (1) ou droite (2)")
    while a != 1 or a != 2 :
         a = input("Où voulez vous aller ? gauche (1) ou droite (2)")

    if a == 1:
        droite()
    if a == 2:
        gauche()
    

def droite():
    print("Vous avez choisis d'aller à droite")
    Salle()

def gauche(): 
    print("Vous avez choisis d'aller à gauche")
    Salle()



def Salle ():
    #On va mettre dans la liste les salles en var 
    L=[]
    i=0
    SalleOuAller=0

    #on parcour la liste si une salle a deja été utilisé on avance dans la liste sinon on stock la salle dans la var SalleOuAller
    while SalleOuAller == 0 :

        while i<len(L):
            if DejaUtilisé(L[i])  :

                #TO DO une fonction boolean DejaUtilisé() qui renvois true si la salle a deja été utilisé
                i=i+1
            else :
                SalleOuAller=L[i]

    #On regarde L[i] et on declanche la fonction de la salle 
    # ex 1 : Vestiaire
    if L[i] == 1:
        Vestiaire()


    