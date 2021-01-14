from Personnage import *
from random import randint
from inventaire import *
from time import *


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

        vieHero = Hero.viePersonnage
        vieMonstre = Monstre.viePersonnage

        if control == 1:
            if Monstre.a_une_attaque_spe(Monstre.get_a_une_attack_spe()):
                AttaqueSpé = randint(1,5)
                if AttaqueSpé == 4:
                    print("\n")
                    Hero.attack_player(Monstre)
                    Monstre.attackSpe_sur(Hero)
                    sleep(1)
                    print(Monstre.nomPersonnage, "a maintenant", Monstre.viePersonnage ," /", vieMonstre ,"pv")
                    sleep(1)
                    print("Vous avez maintenant", Hero.viePersonnage, " /", vieHero ,"pv\n")
                else :
                    print("\n")
                    Hero.attack_player(Monstre)
                    Monstre.attack_monster(Hero)
                    sleep(1)
                    print(Monstre.nomPersonnage, "a maintenant", Monstre.viePersonnage ," /", vieMonstre ,"pv")
                    sleep(1)
                    print("Vous avez maintenant", Hero.viePersonnage, " /", vieHero ,"pv\n")                        
            else:
                print("\n")
                Hero.attack_player(Monstre)
                Monstre.attack_monster(Hero)
                sleep(1)
                print(Monstre.nomPersonnage, "a maintenant", Monstre.viePersonnage ," /", vieMonstre ,"pv")
                sleep(1)
                print("Vous avez maintenant", Hero.viePersonnage, " /", vieHero ,"pv\n")

        elif control == 2:
            choix_inventaire(Inventaire, Hero)
            
        elif control == 3:
            fuite = randint(1, 5)
            if fuite == 3:
                print("\n")
                sleep(1)
                print("Vous parvenez à vous échapper!\n")
                break
            else:
                print("\n")
                sleep(1)                
                print("Vous ne parvenez pas a prendre la fuite")
                print("\n")
                combat(Monstre,Hero)
                
    if Monstre.viePersonnage <= 0:
        print("Vous avez éliminé:", Monstre.get_nomPersonnage())
        Hero.barre_Exp(Monstre.get_ExpADonne())
        Hero.Augment_level()
        
    if Hero.viePersonnage <= 0:
        print("Vous êtes mort...\n")


Hero=hero("Kevin",10,5,0,1,0,None,None)
combat(AlienF1, Hero)