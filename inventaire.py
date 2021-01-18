from Personnage import *
from Arme_et_Armure import *
#from colorama import *

#Inventaire sous forme de dictionnaire avec les valeurs stockées dans des listes'

Inventaire = {
    "Soins": [],
    "Armes": [Sabre_laser],
    "Armures": [],
    "Objets rares": [],
    #"Fermer l'inventaire": True
}

#Fonctions pour ouvrir l'inventaire, se déplacer dedans et utliser les items
#Lorsque qu'un items de soins est utilisé, il est immédiatemment supprimé de la liste

def choix_inventaire(inventaire, hero):
    #print(Fore.YELLOW, "\n")
    choix = int(input("Que voulez vous dans l'inventaire ?\n 1 = Soins |\n 2 = Armes |\n 3 = Armures |"
                      "\n 4 = Objets importants |"
                      "\n 5 = Fermer l'inventaire |\n"))

#Fonctions pour ouvrir l'inventaire, se déplacer dedans et utliser les items
#Lorsque qu'un items de soins est utilisé, il est immédiatemment supprimé de la liste

    #Choix des soins

    if choix == 1 and len(inventaire["Soins"]) > 0:
        for x in inventaire["Soins"]:
            print(" -", x.nomObjet)
        choix_section = int(input("Que voulez vous selectionner ? (1,2...): \n")) - 1
        hero.vie_addition(inventaire["Soins"][(choix_section)].vieEnPlus)
        inventaire["Soins"].pop([0][choix_section - choix_section])
        print("Vous avez maintenant", hero.get_viePersonnage(), "points de vie\n")
        choix_inventaire(inventaire, hero)

    elif choix == 1 and len(inventaire["Soins"])<= 0:
         print("Cette catégorie est vide\n")
         choix_inventaire(Inventaire, hero)

    #Choix des armes

    if choix == 2 and len(inventaire["Armes"]) > 0:
        for x in inventaire["Armes"]:
            print(" -",  x.nomArme)
        choix_section = int(input("Que voulez vous selectionner ? (1,2...) :\n")) - 1
        hero.a_une_arme(inventaire["Armes"][int(choix_section)])
        print("\n")
        print(hero.recap())
        choix_inventaire(inventaire, hero)

    elif choix == 2 and len(inventaire["Armes"])<= 0:
         print("Cette catégorie est vide\n")
         choix_inventaire(Inventaire, hero)
       
    #Choix des armures

    if choix == 3 and len(inventaire["Armures"]) > 0:
        for x in inventaire["Armures"]:
            print(" -", x.nomArmure)
        choix_section = int(input("Que voulez vous selectionner ? (1,2...) :\n")) - 1
        hero.a_une_armure(inventaire["Armures"][int(choix_section)])
        print("\n")
        print(hero.recap())
        choix_inventaire(inventaire, hero)

    elif choix == 3 and len(inventaire["Armures"])<= 0:
         print("Cette catégorie est vide\n")
         choix_inventaire(Inventaire, hero)

    #Choix des objets

    if choix == 4 and len(inventaire["Objets rares"]) > 0:
        print(inventaire["Objets rares"])

    elif choix == 4 and len(inventaire["Objets rares"])<= 0:
         print("Cette catégorie est vide\n")
         choix_inventaire(Inventaire, hero)

    #Retour à la boucle principale du jeu

    if choix == 5:
        return print("Vous fermez l'inventaire\n")
        

#Code à placer dans les salles pour rajouter des items dans l'inventaire

def searchInventaire(Inventaire, objet):
    for i in len(Inventaire) :
        for j in len(Inventaire[i]) :
            if Inventaire[i][j] == objet :
                return True

#def ajout_inventaire(Inventaire):

#choix_inventaire(Inventaire, Kevin)
    for j in len(Inventaire["Objets Rare"]) :
            if j == objet :
                return True


#choix_inventaire(Inventaire, Kevin)

def ouvir_inventaire():
    open = input(("Voulez vous ouvrir l'inventaire pour effectuer des changements? (y/n)?"))
    if open == str("y"):
        choix_inventaire(Inventaire, hero)
    else:
        print("Vous continuez votre aventure")


Hero = hero("Kevin", 100, 5, 0, 1, 0, None, None)
choix_inventaire(Inventaire, Hero)