from Personnage import *
from Arme_et_Armure import *
from Modele import *

#Inventaire sous forme de dictionnaire avec les valeurs stockées dans des listes'

Inventaire = {
    "Soins": [kit_de_soins],
    "Armes": [],
    "Objets rares": [],
    "Fermer l'inventaire": True

<<<<<<< HEAD
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
=======
}

#Fonctions pour ouvrir l'inventaire, se déplacer dedans et utliser les items
#Lorsque qu'un items de soins est utilisé, il est immédiatemment supprimé de la liste

def choix_inventaire(Inventaire):
    choix = int(input("Que voulez vous dans l'inventaire? 1 = Soins | 2 = Armes | 3 = Objets rares | "
                      "4 = Fermer l'inventaire\n"))

    #Choix des soins

    if choix == 1 and len(Inventaire["Soins"]) > 0:
        print(Inventaire["Soins"])

        #Choix dans la section soins
        choix_section = int(input("Que voulez vous selectionner?: ")) - 1
        Kevin.vie_addition(Inventaire["Soins"][(choix_section)].vieEnPlus)
        Inventaire["Soins"].pop([0][choix_section])
        print("Vous avez maintenant", Kevin.get_viePersonnage(), "points de vie\n")
        choix_inventaire(Inventaire)

    #Choix des armes

    if choix == 2 and len(Inventaire["Armes"]) > 0:
        print(Inventaire["Armes"])
        choix_section = int(input("Que voulez vous selectionner?: ")) - 1
        Kevin.set_arme(Inventaire["Armes"][int(choix_section)])
        Kevin.attaque_adition(Inventaire["Armes"][int(choix_section)].get_dommageArme())
        print(Kevin.recap())
        choix_inventaire(Inventaire)

    #Choix des objets

    if choix == 3:
>>>>>>> b17bed7b724db4002602a7567b54e8f933bbda3c
        print(Inventaire[2])
        choix_inventaire(Inventaire)

    #Retour à la boucle principale du jeu

    if choix == 4:
        print("TODO")

    if len(Inventaire["Soins"]) or len(Inventaire["Armes"]) or len(Inventaire["Objets rares"]) <= 0:
        print("Cette catégorie est vide")
        choix_inventaire(Inventaire)


choix_inventaire(Inventaire)
print(Kevin.get_nomArme())


#Code à placer dans les salles pour rajouter des items dans l'inventaire

'''print("Vous trouvez par terre un item de soin = ", Objet_de_Quete.get_nomObjet(petit_bandage))
ramasser = int(input(("Que voulez vous faire? 1 = Ramasser l'objet | 2 = Laisser l'objet")))
if ramasser == 1:
    Inventaire["Soins"].append(petit_bandage)'''




<<<<<<< HEAD
'''def ajout_inventaire(Inventaire):'''
<<<<<<< HEAD
=======

def searchInventaire(Inventaire, objet):
    for i in len(Inventaire) :
        for j in len(Inventaire[i]) :
            if Inventaire[i][j] == objet :
                return True
>>>>>>> Salle
=======
>>>>>>> b17bed7b724db4002602a7567b54e8f933bbda3c
