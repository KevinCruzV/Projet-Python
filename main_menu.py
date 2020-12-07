from Personnage import *
#importation  de l'os pour lancer le jeu dans la console
import os

#Menu principal qui execute la fonction choisie

#Fonction qui exécute la boucle principale du jeu


def main_loop():
    print("TODO")
    main_menu()
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
                main_menu()
        except ValueError:
            input("Appuyez sur 1 pour retourner au menu:")

#Fonction qui explique commennt jouer au jeu


def HowToPlay():
    print("Pour jouer, vous devez entrer un des chiffres disponible et qui définira ensuite votre action.\n")
    TestUser(TestUserInput=False)


#Fonction à propos du jeu


def About():
    print("Projet en python d'un rpg textuel\n")
    TestUser(TestUserInput=False)

#Fonction du menu principal qui permet de lancer la fonction choisie


def main_menu(TestUserInput=False):
    print("1: Jouer")
    print("2: Comment jouer")
    print("3: A propos du jeu")
    print("4: Exit\n")

    # Boucle pour tester ce qu'entre comme valeur l'utilisateur et qui ensuite déclenche une fonction si la condition est vérifiée

    while TestUserInput == False:
        UserInput = input("Entrez un chiffre entre 1 et 4:")
        try:
            UserInput = int(UserInput)
            if UserInput > 0 and UserInput < 5:
                TestUserInput = True
            if UserInput == 1:
                print("Partie initialisée\n")
                main_loop()
            if UserInput == 2:
                print("Accés confirmé\n")
                HowToPlay()
            if UserInput == 3:
                print("Accés confirmé\n")
                About()
            if UserInput == 4:
                print("Autodestruction du vaisseau, vous avez perdu.")
                os.system("pause")
            elif UserInput < 0:
                 print("Cette valeur est trop petite\n")
            elif UserInput > 4:
                 print("Cette valeur est trop grande\n")
        except ValueError:
                print("Erreur, vous vous êtes trompé\n")


#Activation de la fonction du menu principal

Hero = Hero("kevin",20,30)



