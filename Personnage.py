from Modele import Model_Personnage
from Modele import Modele_Armure
from Modele import Modele_Arme
from Arme_et_Armure import *

class Hero(Modele_Personnage, Modele_Arme, Modele_Armure):
    #On fait appelle a l'heritage de la classe Modele Personnage/Arme /Armure
    def __init__(self, nom, vie, attaque, defense):
        super().__init__(nom, vie, attaque, defense)
        self.armure = None
        self.arme = None 
        print("Bienvenue,\n"  "Nom = ", nom, " / Vie = ", vie, " / Attaque = ",attaque," / Defense = ",defense)

    def a_une_arme(self,):
        return self.arme is not None  

    def set_arme(self, arme):
        self.arme = arme

    def attack_player(self, cible):
        super().__init__(self, nom, dommage)
        cible.dommage(self.attaque)
        print( cible.get_nom(),"a prit", self.dommage, "de dégats")
        if self.a_une_arme():
            dommage = dommage + self.arme.dommage_enplus()


