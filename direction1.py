from Salle import *


def direction ():
    a = input("Où voulez vous aller ? gauche ou droite (g/d)" )
    while a != 'd' or a != 'g' : 
        a = input("Où voulez vous aller ? gauche ou droite (g/d)" )
        
        if a == 'd':
            droite()
        if a == 'g':
            gauche()



def droite():
    print("Vous avez choisis d'aller à droite")
    #Random_Salle()
    choixSalles()
def gauche(): 
    print("Vous avez choisis d'aller à gauche")
    #Random_Salle()
    choixSalles()


direction()        
    
#def Salle ():
    #On va mettre dans la liste les salles en var 
   # L=[]
#    i=0
#    SalleOuAller=0

    #on parcour la liste si une salle a deja été utilisé on avance dans la liste sinon on stock la salle dans la var SalleOuAller
 #   while SalleOuAller == 0 :

  #      while i<len(L):
   #         if DejaUtilisé(L[i])  :

                #TO DO une fonction boolean DejaUtilisé() qui renvois true si la salle a deja été utilisé
    #            i=i+1
     #       else :
      #          SalleOuAller=L[i]

    #On regarde L[i] et on declanche la fonction de la salle 
    # ex 1 : Vestiaire
    #if L[i] == 1:
   #     Vestiaire()