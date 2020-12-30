from Personnage import *
from Arme_et_Armure import *



#Inventaire sous forme de dictionnaire avec les valeurs stockées dans des listes'

Inventaire = {
    "Soins": [kit_de_soins, kit_de_soins, kit_de_soins],
    "Armes": [Pistolet_Laser, Epee],
    "Objets rares": [Cle_refectoire],
    "Fermer l'inventaire": True
}

#Fonctions pour ouvrir l'inventaire, se déplacer dedans et utliser les items
#Lorsque qu'un items de soins est utilisé, il est immédiatemment supprimé de la liste

def choix_inventaire(Inventaire, Hero):
    choix = int(input("Que voulez vous dans l'inventaire? 1 = Soins | 2 = Armes | 3 = Objets importants | 4 = Fermer l'inventaire"))

#Fonctions pour ouvrir l'inventaire, se déplacer dedans et utliser les items
#Lorsque qu'un items de soins est utilisé, il est immédiatemment supprimé de la liste

    #Choix des soins

    if choix == 1 and len(Inventaire["Soins"]) > 0:
        for x in Inventaire["Soins"]:
            print(" -", x.nomObjet)
        choix_section = int(input("Que voulez vous selectionner?: ")) - 1
        Hero.vie_addition(Inventaire["Soins"][(choix_section)].vieEnPlus)
        Inventaire["Soins"].pop([0][choix_section - choix_section])
        print("Vous avez maintenant", Hero.get_viePersonnage(), "points de vie\n")
        choix_inventaire(Inventaire, Hero)

    #Choix des armes

    if choix == 2 and len(Inventaire["Armes"]) > 0:
        for x in Inventaire["Armes"]:
            print(" -", x.nomArme)
        choix_section = int(input("Que voulez vous selectionner?: ")) - 1
        Hero.set_arme(Inventaire["Armes"][int(choix_section)])
        Hero.attaque_adition(Inventaire["Armes"][int(choix_section)].get_dommageArme())
        print(Hero.recap())
        choix_inventaire(Inventaire, Hero)

    #Choix des objets

    if choix == 3 and len(Inventaire["Armes"]) > 0:
        print(Inventaire["Objets rares"])

    #Retour à la boucle principale du jeu

    if choix == 4:
        print("TODO")

    if len(Inventaire["Soins"]) or len(Inventaire["Armes"]) or len(Inventaire["Objets rares"]) <= 0:
        print("Cette catégorie est vide")
        choix_inventaire(Inventaire, Hero)


def searchInventaire(Inventaire, objet):
       for i in len(Inventaire["Objets rares"]) :
            if i == objet :
                return True

#choix_inventaire(Inventaire)


#choix_inventaire(Inventaire)
#print(Hero.get_nomArme())


#Code à placer dans les salles pour rajouter des items dans l'inventaire

#print("Vous trouvez par terre un item de soin = ", Objet_de_Quete.get_nomObjet(kit_de_soins))
#ramasser = int(input(("Que voulez vous faire? 1 = Ramasser l'objet | 2 = Laisser l'objet")))
#if ramasser == 1:
#    Inventaire["Soins"].append(kit_de_soins)




#def ajout_inventaire(Inventaire):


