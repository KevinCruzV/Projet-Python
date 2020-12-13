from Modele import *
from Arme_et_Armure import *
#from Arme_et_Armure import *


class Hero(Modele_Personnage):
    #On fait appelle a l'heritage de la classe Modele Personnage/Arme /Armure
    def __init__(self, nom, vie, attaque, defense, level, exp):
        super().__init__(nom, vie, attaque, defense, level)
        self.armure = None
        self.arme = None 
        self.exp = 0
        print("Statistiques:\nNom : ", nom, " | Vie : ", vie, " | Attaque : ", attaque, " | Defense : ", defense, " | Niveau : ", level, "\n")

    def a_une_arme(self,):
        return self.arme is not None  

    def set_arme(self, arme):
        self.arme = arme

    def get_exp(self):
        return self.exp 

    def barre_Exp(self, exp_en_plus, Hero):
        self.exp += exp_en_plus
        Hero.get_exp()
        

    def Augment_level(self, Hero):
        if Hero.get_exp() == 100 :
            self.level = self.level + 1
            self.vie = self.vie + 20
            self.attaque += 15
            self.defense += 30 
            self.exp = 0
            print("Vous avez augmenté d'un niveau !")
            print("Vous etes maintenant au niveau : ", Hero.get_level())

        else : 
             
            break

'''    def attack_player(self, cible):
        super().__init__(self, nom, dommage)
        cible.dommage(self.attaque)
        print( cible.get_nom(),"a prit", self.dommage, "de dégats")
        if self.a_une_arme():
            dommage = dommage + self.arme.dommage_enplus()
'''


class MonstresForts(Modele_Personnage):

    def __init__(self, nom, vie, attaque, defense, level, attaque_speciale):
        super().__init__(nom, vie, attaque, defense, level)
        self.attaque_speciale = attaque_speciale
        print("/!\ Un monstre spécial apparait /!\ ")
        print("Nom :", nom, "| Vie :", vie, "| Attaque :", attaque, "| Defense :", defense, "| Attaque speciale :",
              attaque_speciale, "\n")

    def attaque_speciale(self):
        return self.attaque_speciale


class MonstresNormaux(Modele_Personnage):

    def __init__(self, nom, vie, attaque, defense, level):
        super().__init__(nom, vie, attaque, defense, level)
        print("Un monstre apparait !")
        print("Nom :", nom, "| Vie :", vie, "| Attaque :", attaque, "| Defense :", defense, "\n")

    def damage(self, attaque):
        self.vie -= attaque
        print("Le monstre à subit", attaque, "dégats")

    def dommage(self, dommage):
        self.vie = self.vie - dommage

    def attack_monster(self, cible):
        cible.dommage(self.attaque)
        print(cible.get_nom(), "a prit", self.attaque, "de dégats.")




