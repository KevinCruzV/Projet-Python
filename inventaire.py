from Personnage import *
from Arme_et_Armure import *



#Inventaire sous forme de dictionnaire avec les valeurs stockées dans des listes'

<<<<<<< HEAD
inventaire = {
    "Soins": [kit_de_soins],
    "Armes": [],
    "Objets rares": [],
    "Fermer l'inventaire": True


Inventaire=[["Soins"],["Armes"],["Objets Importants"]]

def choix_inventaire(Inventaire, Hero):
    choix = int(input("Que voulez vous dans l'inventaire? 1 = Soins | 2 = Armes | 3 = Objets importants | 4 = Fermer l'inventaire"))
    if choix == 1:
        print(Inventaire[0])
    elif choix == 2:
        print(Inventaire[1])
        selection = int(input("Que voulez vous selectionner? 1 | 2 :"))
        if selection == 1:
            Hero.a_une_arme(Inventaire[1][0])
        if selection == 2:
            Hero.a_une_arme(Inventaire[1][1])
    elif choix == 3:
=======
Inventaire = {
    "Soins": [kit_de_soins, kit_de_soins, kit_de_soins],
    "Armes": [Pistolet_Laser, Epee],
    "Objets rares": [],
    "Fermer l'inventaire": True
>>>>>>> 0f136d389810872c78b65227ce61137745313bed
}

#Fonctions pour ouvrir l'inventaire, se déplacer dedans et utliser les items
#Lorsque qu'un items de soins est utilisé, il est immédiatemment supprimé de la liste

def choix_inventaire(Inventaire):
<<<<<<< HEAD
    choix = int(input("Que voulez vous dans l'inventaire? 1 = Soins | 2 = Armes | 3 = Objets rares | 4 = Fermer l'inventaire\n"))
=======
    choix = int(input("Que voulez vous dans l'inventaire? 1 = Soins | 2 = Armes | 3 = Objets importants |"
                      " 4 = Fermer l'inventaire"))

#Fonctions pour ouvrir l'inventaire, se déplacer dedans et utliser les items
#Lorsque qu'un items de soins est utilisé, il est immédiatemment supprimé de la liste
>>>>>>> 0f136d389810872c78b65227ce61137745313bed

    #Choix des soins

    if choix == 1 and len(Inventaire["Soins"]) > 0:
        for x in Inventaire["Soins"]:
            print(" -", x.nomObjet)
        choix_section = int(input("Que voulez vous selectionner?: ")) - 1
<<<<<<< HEAD
        Hero.vie_addition(Inventaire["Soins"][(choix_section)].vieEnPlus)
        Inventaire["Soins"].pop([0][choix_section])
        print("Vous avez maintenant", Hero.get_viePersonnage(), "points de vie\n")
=======
        Kevin.vie_addition(Inventaire["Soins"][(choix_section)].vieEnPlus)
        Inventaire["Soins"].pop([0][choix_section - choix_section])
        print("Vous avez maintenant", Kevin.get_viePersonnage(), "points de vie\n")
>>>>>>> 0f136d389810872c78b65227ce61137745313bed
        choix_inventaire(Inventaire)

    #Choix des armes

    if choix == 2 and len(Inventaire["Armes"]) > 0:
        for x in Inventaire["Armes"]:
            print(" -", x.nomArme)
        choix_section = int(input("Que voulez vous selectionner?: ")) - 1
        Hero.set_arme(Inventaire["Armes"][int(choix_section)])
        Hero.attaque_adition(Inventaire["Armes"][int(choix_section)].get_dommageArme())
        print(Hero.recap())
        choix_inventaire(Inventaire)

    #Choix des objets

<<<<<<< HEAD
    if choix == 3:
        print(Inventaire[2])
        choix_inventaire(Inventaire)
=======
    if choix == 3 and len(Inventaire["Armes"]) > 0:
        print(Inventaire["Objets rares"])
>>>>>>> 0f136d389810872c78b65227ce61137745313bed

    #Retour à la boucle principale du jeu

    if choix == 4:
        print("TODO")

    if len(Inventaire["Soins"]) or len(Inventaire["Armes"]) or len(Inventaire["Objets rares"]) <= 0:
        print("Cette catégorie est vide")
        choix_inventaire(Inventaire)


choix_inventaire(Inventaire)
<<<<<<< HEAD
print(Hero.get_nomArme())
=======
>>>>>>> 0f136d389810872c78b65227ce61137745313bed


'''choix_inventaire(Inventaire)
print(Kevin.get_nomArme())
'''

#Code à placer dans les salles pour rajouter des items dans l'inventaire

<<<<<<< HEAD
#print("Vous trouvez par terre un item de soin = ", Objet_de_Quete.get_nomObjet(petit_bandage))
#ramasser = int(input(("Que voulez vous faire? 1 = Ramasser l'objet | 2 = Laisser l'objet")))
#if ramasser == 1:
#    Inventaire["Soins"].append(petit_bandage)'''
=======
'''print("Vous trouvez par terre un item de soin = ", Objet_de_Quete.get_nomObjet(kit_de_soins))
ramasser = int(input(("Que voulez vous faire? 1 = Ramasser l'objet | 2 = Laisser l'objet")))
if ramasser == 1:
    Inventaire["Soins"].append(kit_de_soins)'''
>>>>>>> 0f136d389810872c78b65227ce61137745313bed




<<<<<<< HEAD

#'''def ajout_inventaire(Inventaire):'''
=======
'''def ajout_inventaire(Inventaire):'''
>>>>>>> 0f136d389810872c78b65227ce61137745313bed


'''def searchInventaire(Inventaire, objet):
    for i in len(Inventaire) :
        for j in len(Inventaire[i]) :
            if Inventaire[i][j] == objet :
<<<<<<< HEAD
                return True
=======
                return True'''


>>>>>>> 0f136d389810872c78b65227ce61137745313bed

