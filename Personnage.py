from Modele import *
from Arme_et_Armure import *
#from Arme_et_Armure import *


class Hero(Modele_Personnage, Modele_Arme, Modele_Armure):
    #On fait appelle a l'heritage de la classe Modele Personnage/Arme /Armure
    def __init__(self, nomPersonnage, viePersonnage, attaquePersonnage, defensePersonnage, levelPersonnage, exp, arme, armure):
        super().__init__(nomPersonnage, viePersonnage, attaquePersonnage, defensePersonnage, levelPersonnage)
        self.armure = None
        self.arme = None 
        self.exp = 0

        print("Statistiques:\nNom : ", nomPersonnage, " | Vie : ", viePersonnage, " | Attaque : ", attaquePersonnage, " | Defense : ", defensePersonnage, " | Niveau : ", levelPersonnage, " | Arme : Nul ", "| Armure : Nul", "\n")

    

    def recap(self):
    #Pb d'heredité
       print("Statistiques:\nNom : ", self.get_nomPersonnage(), " | Vie : ", self.get_viePersonnage(), " | Attaque : ", self.get_attaquePersonnage(), " | Defense : ", self.get_defensePersonnage(), " | Niveau : ", self.get_levelPersonnage(), " | Arme : ", self.arme.get_nomArme(), "| Armure : ", self.armure.get_nomArmure(), "\n")   




    # Fonction Arme #

    def a_une_arme(self, arme):
        print("Arme equipée:", arme.get_nomArme())
        self.attaque_adition(arme.get_dommageArme())
        self.set_arme(arme)
        return self.arme is not None

    def set_arme(self, arme):
        self.arme = arme

    def attaque_adition(self, attqArme):
        self.attaquePersonnage += attqArme 



        # Fonction Armure #

    def a_une_armure(self, armure):
        print("Vous etes equipé d'une", armure.get_nomArmure())
        self.defense_adition(armure.get_defenseArmure())
        self.set_armure(armure)
        return self.arme is not None  

    def set_armure(self, armure):
        self.armure = armure  
   
    def defense_adition(self, defarmure):
        self.defensePersonnage += defarmure              

 

        # Fonction EXP #

    def get_exp(self):
        return self.exp 

    def barre_Exp(self, exp_en_plus):
        self.exp += exp_en_plus
        self.get_exp()
        

    def Augment_level(self):
        if self.get_exp() == 100 :
            self.levelPersonnage += 1
            self.viePersonnage += 20
            self.attaquePersonnage += 15
            self.defensePersonnage += 30 
            self.exp = 0
            print("Vous avez augmenté d'un niveau !")
            print("Vous etes maintenant au niveau : ", self.get_levelPersonnage())

        else :    
            pass




class MonstresForts(Modele_Personnage):

    def __init__(self, nomPersonnage, viePersonnage, attaquePersonnage, defensePersonnage, levelPersonnage, attaque_speciale):
        super().__init__(nomPersonnage, viePersonnage, attaquePersonnage, defensePersonnage, levelPersonnage)
        self.attaque_speciale = attaque_speciale
        print(" /!\ Un monstre spécial apparait /!\ ")
        print("Nom :", nomPersonnage, "| Vie :", viePersonnage, "| Attaque :", attaquePersonnage, "| Defense :", defensePersonnage, "| Attaque speciale :", attaque_speciale, " | Niveau : ", levelPersonnage, "\n")

    def get_attaque_speciale(self):
        return self.attaque_speciale


class MonstresNormaux(Modele_Personnage):

    def __init__(self, nomPersonnage, viePersonnage, attaquePersonnage, defensePersonnage, levelPersonnage):
        super().__init__(nomPersonnage, viePersonnage, attaquePersonnage, defensePersonnage, levelPersonnage)
        print("Un monstre apparait !")
        print("Nom :", nomPersonnage, "| Vie :", viePersonnage, "| Attaque :", attaquePersonnage, "| Defense :", defensePersonnage, " | Niveau : ", levelPersonnage, "\n")

    def damage(self, attaque):
        self.viePersonnage -= attaque
        print("Le monstre à subit", attaque, "dégats")


    def attack_monster(self, cible):
        cible.dommage(self.attaquePersonnage)
        print(cible.get_nomPersonnage(), "a prit", self.attaquePersonnage, "de dégats.")




Kevin = Hero("Kevin",20,10,20,1,0,None,None)
Epee = Modele_Arme("Epée", 20)
Pistolet_Laser = Modele_Arme("Pistolet Laser", 35)
Armure = Modele_Armure("combi",30)
'''Kevin.a_une_arme(Epee)
Kevin.a_une_armure(Armure)
Kevin.barre_Exp(100)
Kevin.Augment_level()
Kevin.recap()
'''