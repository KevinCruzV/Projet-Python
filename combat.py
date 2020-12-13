from Personnage import Hero
from Personnage import MonstresNormaux
from inventaire import inventory
from random import randint


def combat(Monstre = MonstresNormaux("Alien", 15, 7, 10, 1), Hero1 = Hero("Hugo", 100, 5, 10, 0, 0)):

    while Hero1.vie > 0 or Monstre.vie > 0:
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
            Hero1.attack_player(Monstre)
            Monstre.attack_monster(Hero1)
            print(Monstre.nom, "a maintenant", Monstre.vie ,"/ 25 pv")
            print("Vous avez maintenant", Hero1.vie, " /100 pv\n")
        if Monstre.vie <= 0:
            print("Vous avez éliminé:", Monstre.nom)
            break
        if Hero1.vie <= 0:
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


combat()
