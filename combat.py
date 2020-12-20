from Personnage import *
from inventaire import inventory
from random import randint


def combat(Monstre, Hero):

    while Hero.viePersonnage > 0 or Monstre.viePersonnage > 0:
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
            print(Monstre.nomPersonnage, "a maintenant", Monstre.viePersonnage ,"/ 25 pv")
            print("Vous avez maintenant", Hero.viePersonnage, " /100 pv\n")
        if Monstre.viePersonnage <= 0:
            print("Vous avez éliminé:", Monstre.nomPersonnage)
            break
        if Hero.viePersonnage <= 0:
            print("Vous êtes mort...\n")
            break
        elif control == 2:
            inventory()
        elif control == 3:
            fuite = randint(1, 5)
            if fuite == 3:
                print("Vous parvenez à vous échapper!\n")
                break


Hugo = Hero("Kevin",100,10,2,1,0,None,None)
Alien = MonstresNormaux("Alien", 25, 10, 5, 1)
combat(Alien, Hugo)

