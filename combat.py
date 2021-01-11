from Personnage import *
from random import randint
from inventaire import *


def combat(Monstre, Hero):

    while Hero.viePersonnage > 0 or Monstre.viePersonnage > 0:
        print("Appuyez sur 1 pour attaquer")
        print("Appuyez sur 2 pour ouvrir l'inventaire")
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
        elif control == 2:
            choix_inventaire(Inventaire, Hero)
        elif control == 3:
            fuite = randint(1, 5)
            if fuite == 3:
                print("Vous parvenez à vous échapper!\n")
                break
            else:
                print("Vous ne parvenez pas a prendre la fuite")
                combat(Monstre,Hero)
                
    if Monstre.viePersonnage <= 0:
        print("Vous avez éliminé:", Monstre.get_nomPersonnage())
        Hero.barre_Exp(Monstre.get_ExpADonne())
        Hero.Augment_level()
        
    if Hero.viePersonnage <= 0:
        print("Vous êtes mort...\n")
