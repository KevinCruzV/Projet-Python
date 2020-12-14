from Personnage import *
from Personnage import *
from inventaire import inventory
from random import randint


def combat(Monstre, Hero):

    while Hero.vie > 0 or Monstre.vie > 0:
        print("Appuyez sur 1 pour attaquer")
        print("Appuyez sur 2 pour utiliser un objet")
        print("Appuyez sur 3 pour fuir le combat\n")

        control = (input("Que voulez vous faire?\n"))
        #test de l'input "control"
        try:
            control = int(control)
        except ValueError:
            print("Impossible")
            continue
        if control < 0:
            print("Impossible")
        if control > 4:
            print("Impossible")

        if control == 1:
            Hero.attack_player(Monstre)
            Monstre.attack_monster(Hero)
            print(Monstre.nom, "a maintenant", Monstre.vie ,"/ 25 pv")
            print("Vous avez maintenant", Hero.vie, " /100 pv\n")
        if Monstre.vie <= 0:
            print("Vous avez éliminé:", Monstre.nom)
            break
        if Hero.vie <= 0:
            print("Vous êtes mort...")
            break
        elif control == 2:
            inventory()
        elif control == 3:
            fuite = randint(1, 5)
            print(fuite)
            if fuite == 3:
                print("Vous parvenez à vous échapper!")
                break


Hugo = Hero("Kevin",100,50,20,1,0,None,None)
Alien = MonstresNormaux("Alien", 25, 10, 5, 1)
#PB a regler : faire que l'on peut reinitialiser les arme + ajout pts d'attaque quand arme et def + pb avec programme de hugo
combat(Alien, Hugo)
