#import de l'os pour lancer le jeu dans la console
import os

#Menu principal qui execute la fonction choisie
#Fonction principale du jeu
def main_loop():
    print("TODO")

#Fonction qui explique commennt jouer au jeu
def HowToPlay():
    print("Pour jouer, vous devez entrer un des chiffres entre 1 et 4 qui définira votre action.")
    print("Si vous avez besoin d'aide pendant le jeu, écrivez 'help' ")
    print("Pour retourner au menu, appuyez sur 1")
    UserInput = int(input())
    if UserInput == 1:
        main_menu()
    else:
        print("Action invalide, appuyez sur 1 pour revenir au menu")

#Fonction à propos du jeu
def About():
    print("Projet en python d'un rpg textuel")
    print("Pour retourner au menu appuyez sur 1")
    UserInput = int(input())
    if UserInput == 1:
        main_menu()

#Fonction du menu principal qui permet de lancer la fonction choisie

def main_menu():
    print("1: Jouer")
    print("2: Comment jouer")
    print("3: A propos du jeu")
    print("4: Exit")

    UserInput = int(input("Entrez un chiffre entre 1 et 4:"))

    if UserInput == 1:
        main_loop()
    if UserInput == 2:
        HowToPlay()
    if UserInput == 3:
        About()
    if UserInput == 4:
        os.system("pause")

main_menu()