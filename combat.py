from Personnage import *
from random import randint
from inventaire import *
from time import *
import os
#os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
#import pygame


##PYGAME mis en commentaire pour ne pas crash si la lib n'est pas installée

#from colorama import *

def combat(Monstre, Hero):
    #pygame.init()
    #Alien_Grognement = pygame.mixer.Sound("grognement-2.wav")
    #Alien_Grognement.set_volume(0.1)
    while Hero.viePersonnage > 0 or Monstre.viePersonnage > 0:
        #print(Fore.RED, "\n")
        print(" Appuyez sur 1 pour attaquer")
        print(" Appuyez sur 2 pour ouvrir l'inventaire")
        print(" Appuyez sur 3 pour fuir le combat\n")

        control = (input("Que voulez vous faire ?\n"))
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
                AttaqueSpe = randint(1,5)
                if AttaqueSpe == 4:
                    print("\n")
                    print("Vous attaquez", Monstre.nomPersonnage)
                    sleep(2)
                    Hero.attack_player(Monstre)
                    #Alien_Grognement.play()
                    print(Monstre.nomPersonnage,"utilise", Monstre.Nom_attaque_speciale)
                    sleep(2)
                    Monstre.attackSpe_sur(Hero)
                    sleep(2)
                    print(Monstre.nomPersonnage, "a maintenant", Monstre.viePersonnage ," /", vieMonstre ,"pv")
                    sleep(2)
                    print("Vous avez maintenant", Hero.viePersonnage, " /", vieHero,"pv\n")
                else:
                    print("\n")
                    print("Vous attaquez", Monstre.nomPersonnage)
                    sleep(2)
                    Hero.attack_player(Monstre)
                    sleep(2)
                    #Alien_Grognement.play()
                    print(Monstre.nomPersonnage,"vous attaque")
                    Monstre.attack_monster(Hero)
                    sleep(2)
                    print(Monstre.nomPersonnage, "a maintenant", Monstre.viePersonnage ," /", vieMonstre ,"pv")
                    sleep(2)
                    print("Vous avez maintenant", Hero.viePersonnage, " /", vieHero,"pv\n")
                    sleep(2)
            else:
                print("\n")
                print("Vous attaquez", Monstre.nomPersonnage)
                sleep(2)
                Hero.attack_player(Monstre)
                sleep(2)
                #Alien_Grognement.play()
                print(Monstre.nomPersonnage,"vous attaque")
                Monstre.attack_monster(Hero)
                sleep(2)
                print(Monstre.nomPersonnage, "a maintenant", Monstre.viePersonnage ," /", vieMonstre ,"pv")
                sleep(2)
                print("Vous avez maintenant", Hero.viePersonnage, " /", vieHero,"pv\n")
                sleep(2)

        elif control == 2:
            choix_inventaire(Inventaire, Hero)
            
        elif control == 3:
            fuite = randint(1, 4)
            if fuite == 3:
                print("\n")
                sleep(2)
                print("Vous parvenez à vous échapper!\n")
                break
            else:
                print("\n")
                sleep(2)                
                print("Vous ne parvenez pas a prendre la fuite")
                print("\n")
                Monstre.attack_monster(Hero)
                sleep(2)
                #Alien_Grognement.play()
                print(Monstre.nomPersonnage,"vous attaque")
                sleep(2)
                print(Monstre.nomPersonnage, "a maintenant", Monstre.viePersonnage ," /", vieMonstre ,"pv")
                sleep(2)
                print("Vous avez maintenant", Hero.viePersonnage, " /", vieHero ,"pv\n")
                sleep(2)                

                combat(Monstre,Hero)
                
        if Monstre.viePersonnage <= 0:
            print("Vous avez éliminé:", Monstre.get_nomPersonnage(), "!")
            Hero.barre_Exp(Monstre.get_ExpADonne())
            Hero.Augment_level()
            break
        

        if Hero.viePersonnage <= 0:
            print("Vous êtes mort...\n")
            print("Vous reprendrez au dernier point de passage")
            print("3")
            sleep(2)
            print("2")
            sleep(2)
            print("1")
            sleep(2)
            os.system(exit())
            break

    print("Fin du combat")


#Hero = hero("Kevin", 100, 5, 0, 1, 0, None, None)
#combat(AlienN1, Kevin)

#Hero = hero("Kevin", 100, 5, 0, 1, 0, None, None)
#combat(AlienF3, Kevin)


