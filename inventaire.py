from Modele import *
from Personnage import *


<<<<<<< HEAD
Inventaire = [["Soins"], ["Armes"], ["Objets Importants"]]

def choix_inventaire(Inventaire):
    choix = int(input("Que voulez vous dans l'inventaire? 1 = Soins | 2 = Armes | 3 = Objets importants | "
                      "4 = Fermer l'inventaire"))
=======

Inventaire = [["Soins"], ["Armes"], ["Objets Importants"]]

def choix_inventaire(Inventaire, Hero):
    choix = int(input("Que voulez vous dans l'inventaire? 1 = Soins | 2 = Armes | 3 = Objets importants | 4 = Fermer l'inventaire"))
>>>>>>> Salle
    if choix == 1:
        print(Inventaire[0])
    elif choix == 2:
        print(Inventaire[1])
        selection = int(input("Que voulez vous selectionner? 1 | 2 :"))
        if selection == 1:
<<<<<<< HEAD
            Kevin.a_une_arme(Inventaire[1][0])
        if selection == 2:
            Kevin.a_une_arme(Inventaire[1][1])
=======
            Hero.a_une_arme(Inventaire[1][0])
        if selection == 2:
            Hero.a_une_arme(Inventaire[1][1])
>>>>>>> Salle
    elif choix == 3:
        print(Inventaire[2])
    elif choix == 4:
        print("TODO retour boucle principale")

'''def ajout_inventaire(Inventaire):'''
<<<<<<< HEAD
=======

def searchInventaire(Inventaire, objet):
    for i in len(Inventaire) :
        for j in len(Inventaire[i]) :
            if Inventaire[i][j] == objet :
                return True
>>>>>>> Salle
