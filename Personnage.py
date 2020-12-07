from Modele import *
from Arme_et_Armure import *

class Hero(Modele_Personnage, Modele_Arme, Modele_Armure):
    #On fait appelle a l'heritage de la classe Modele Personnage/Arme /Armure
    def __init__(self, nom, vie, attaque, defense):
        super().__init__(nom, vie, attaque, defense)
        self.armure = None
        self.arme = None 
        print("Bienvenue,\nNom : ", nom, " / Vie : ", vie, " / Attaque : ", attaque, " / Defense : ", defense, "\n")

    def a_une_arme(self,):
        return self.arme is not None  

    def set_arme(self, arme):
        self.arme = arme

'''    def attack_player(self, cible):
        super().__init__(self, nom, dommage)
        cible.dommage(self.attaque)
        print( cible.get_nom(),"a prit", self.dommage, "de dégats")
        if self.a_une_arme():
            dommage = dommage + self.arme.dommage_enplus()
'''

class MonstresForts(Modele_Personnage):

    def __init__(self, nom, vie, attaque, defense, attaque_speciale):
        super().__init__(nom, vie, attaque, defense)
        self.attaque_speciale = attaque_speciale
        print("Un monstre special apparait!")
        print("Nom :", nom, "/ Vie :", vie, "/ Attaque :", attaque, "/ Defense :", defense, "/ Attaque speciale :",
              attaque_speciale, "\n")

    def attaque_speciale(self):
        return self.attaque_speciale


Hero1 = Hero("Hero", 10, 10, 10,)
Boss = MonstresForts("Super Alien", 10, 19, 10, 10)


