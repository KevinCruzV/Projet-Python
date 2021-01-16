from Personnage import *
from Modele import *
from Salle import *
from sauvegarde import *
from direction1 import direction
import os
#importation  de l'os pour lancer le jeu dans la console


#Menu principal qui execute la fonction choisie

#Fonction qui exécute la boucle principale du jeu 

def main():
    Hero=hero(str(input("quel est ton prénom ? \n")),10,5,0,1,0,None,None)
    Salle_0(Hero)
    for i in Salles:
        if i == len(Salles):
            #Tu entre dans la salle final
            Salle_final(Hero)
            Credit()
            os.system(exit())
        else :
            if direction() :
                choixSalles(Salles, Hero)
            else :
                choixSalles(Salles, Hero)   
            






#Fonction qui charge la partie
def Load():
    Data = recupData()
    if Data != None:
        print("Accés confirmé\nVous revenez au vaisseau\n")
        dataRecap(Data)
        Hero = Data["Héro"]
        for i in Data["Salle"]:
            if i == len(Data["Salle"]):
                Salle_final(Hero)
                Credit()
                os.system(exit())
            else : 
                if direction():   
                    choixSalles(Data["Salle"], Hero)
                else :
                    choixSalles(Data["Salle"], Hero)
    else:
        print("Vous ne pouvez pas revenir au vaisseau (Pas de sauveagarde)\n ")
        menu()    
   


# Credit
def Credit():
    print("Ce jeu a ete devellopé blablabla")


#Fonction qui explique commennt jouer au jeu
def HowToPlay():
    print("Pour jouer, vous devez entrer un des chiffres disponible et qui définira ensuite votre action.\n")
    print("Projet en python d'un rpg textuel\n")
    TestUser(TestUserInput=False)

#Fonction pour tester ce qu'entre comme valeur l'utilisateur et qui ramène au menu si la condition est vérifiée
def TestUser(TestUserInput=False):
    
    while TestUserInput == False:
        UserInput = input("Appuyez sur 1 pour retourner au menu:")
        try:
            UserInput = int(UserInput)
            if UserInput != 1:
                TestUserInput = False
            else:
                TestUserInput = True
                menu()
        except ValueError:
            input("Appuyez sur 1 pour retourner au menu:")


#Fonction du menu principal qui permet de lancer la fonction choisie
def menu(TestUserInput=False):
    print("1: Nouvelle partie :")
    print("2: load Partie :")
    print("3: A propos du jeu")
    print("4: Exit\n")

    # Boucle pour tester ce qu'entre comme valeur l'utilisateur et qui ensuite déclenche une fonction si la condition est vérifiée

    while TestUserInput == False:
        UserInput = input("Entrez un chiffre entre 1 et 4:")
        try:
            UserInput = int(UserInput)
            if UserInput > 0 and UserInput < 5:
                TestUserInput = True

            #Jouer au jeu

            if UserInput == 1:
                print("Partie initialisée\n Bon courage ^^\n")
                main()

            #Sauvegarde

            if UserInput == 2:
                    print("Accés confirmé\nVous revenez au vaisseau\n")
                    Load()

            #Le How To Play

            if UserInput == 3:
                print("Accés confirmé\n Plan d'evacuation\n")
                HowToPlay()

            #Sortir du jeu

            if UserInput == 4:
                print("Autodestruction du vaisseau, vous avez perdu.")
                os.system(exit())

            #Erreurs 

            elif UserInput < 0:
                print("Impossible\n")
            elif UserInput > 4:
                print("Impossible\n")
        except ValueError:
                print("Impossible\n")

                

def choixSalles(salle, hero):
    nb = randint(1, 19)
    P = VarHero(hero)
    for i in salle:
        if nb == 1 or nb == 11 or nb == 12:
            Vestiaire(P)
            SuppSalle(salle, 1)
            SuppSalle(salle, 2)
            SuppSalle(salle, 3)
            print(P)
            P = VarHero(hero)
            Sauve(P,Salles,Inventaire)

        if nb == 2 or nb == 13 or nb == 14:
            Infirmerie(P)
            SuppSalle(salle, 2)
            SuppSalle(salle, 13)
            SuppSalle(salle, 14)
            print(P)
            P = VarHero(hero)
            Sauve(P,Salles,Inventaire)

        if nb == 3 or nb == 15:
            Hangar(P)
            SuppSalle(salle, 3)
            SuppSalle(salle, 15)
            print(P)
            P = VarHero(hero)
            Sauve(P,Salles,Inventaire)

        if nb == 4:
            Armurerie(P)
            SuppSalle(salle, nb)
            print(P)
            P = VarHero(hero)
            Sauve(P,Salles,Inventaire)

        if nb == 5 or nb == 16:
            Laboratoire(P)
            SuppSalle(salle, 5)
            SuppSalle(salle, 16)
            print(P)
            P = VarHero(hero)
            Sauve(P,Salles,Inventaire)

        if nb == 6 or nb == 17:
            ChambreFroide(P)
            SuppSalle(salle, 6)
            SuppSalle(salle, 17)
            print(P)
            P = VarHero(hero)
            Sauve(P,Salles,Inventaire)

        if nb == 7 or nb == 18 or nb == 19:
            Salle_des_Communications(P)
            SuppSalle(salle, 7)
            SuppSalle(salle, 18)
            SuppSalle(salle, 19)
            print(P)
            P = VarHero(hero)
            Sauve(P,Salles,Inventaire)

        if nb == 8:
            ChambreEquipage(P)
            SuppSalle(salle, nb)
            print(P)
            P = VarHero(hero)
            Sauve(P,Salles,Inventaire)

        if nb == 9:
            Bibliotheque(P)
            SuppSalle(salle, nb)
            print(P)
            P = VarHero(hero)
            Sauve(P,Salles,Inventaire)

        if nb == 10:
            CapsuleDeSauvetage(P)
            SuppSalle(salle, nb)
            print(P)
            P = VarHero(hero)
            Sauve(P,Salles,Inventaire)                                       

        i += 1


def GameOver():
    print("\n")
    sleep(2)
    print("GAME OVER ! vous n'avez pas reussi a quitter le vaiseau.")

    







