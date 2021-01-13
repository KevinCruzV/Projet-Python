from Modele import *
from Arme_et_Armure import *




def VarHero(hero):
    return hero

class hero(Modele_Personnage, Modele_Arme, Modele_Armure):
    #On fait appelle a l'heritage de la classe Modele Personnage/Arme /Armure
    def __init__(self, nomPersonnage, viePersonnage, attaquePersonnage, defensePersonnage, levelPersonnage, exp, arme, armure):
        super().__init__(nomPersonnage, viePersonnage, attaquePersonnage, defensePersonnage, levelPersonnage)
        self.armure = None
        self.arme = None 
        self.exp = 0
       



    def recap(self):
        if self.arme == None and self.armure == None :
            print("\n")
            print("Badge Spatial:\nNom : ", self.get_nomPersonnage(), " | Vie : ", self.get_viePersonnage(), " | Attaque : ", self.get_attaquePersonnage(), " | Defense : ", self.get_defensePersonnage(), " | Niveau : ", self.get_levelPersonnage(), " | Arme : Rien ", "| Armure : Rien " "\n")

        if self.arme == None and self.armure is not None :
            print("\n")
            print("Badge Spatial:\nNom : ", self.get_nomPersonnage(), " | Vie : ", self.get_viePersonnage(), " | Attaque : ", self.get_attaquePersonnage(), " | Defense : ", self.get_defensePersonnage(), " | Niveau : ", self.get_levelPersonnage(), " | Arme : Rien ", "| Armure : ", self.armure.get_nomArmure(), "\n") 

        if self.arme is not None and self.armure == None :
            print("\n")
            print("Badge Spatial:\nNom : ", self.get_nomPersonnage(), " | Vie : ", self.get_viePersonnage(), " | Attaque : ", self.get_attaquePersonnage(), " | Defense : ", self.get_defensePersonnage(), " | Niveau : ", self.get_levelPersonnage(), " | Arme : ", self.arme.nomArme, "| Armure : Rien", "\n")

        if self.arme is not None and self.armure is not None :
            print("\n")
            print("Badge Spatial:\nNom : ", self.get_nomPersonnage(), " | Vie : ", self.get_viePersonnage(), " | Attaque : ", self.get_attaquePersonnage(), " | Defense : ", self.get_defensePersonnage(), " | Niveau : ", self.get_levelPersonnage(), " | Arme : ", self.arme.nomArme, "| Armure : ", self.armure.get_nomArmure(), "\n")






    def a_une_arme(self, arme):
        print("Vous êtes equipé de l'arme", arme.nomArme, "!")
        print("Vous rajoutez +",arme.get_dommageArme(),"a votre attaque")
        if self.arme is not None :
            self.attaquePersonnage -= self.arme.get_dommageArme()
        self.attaque_adition(arme.get_dommageArme())
        self.set_arme(arme)
        return self.arme is not None

    def set_arme(self, arme):
        self.arme = arme

    def attaque_adition(self, attqArme):
        self.attaquePersonnage += attqArme

    def vie_addition(self, VieAddition):
        self.viePersonnage += VieAddition


        # Fonction Armure #

    def a_une_armure(self, armure):
        print("Vous etes equipé d'une", armure.get_nomArmure()) 
        print("Vous rajoutez +",armure.get_defenseArmure(),"a votre defense")      
        if self.armure is not None :
            self.defensePersonnage -= self.armure.get_defenseArmure()
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
            self.viePersonnage += 10
            self.attaquePersonnage += 8
            self.defensePersonnage += 7 
            self.exp = 0
            print("Vous avez augmenté d'un niveau !")
            print("Vous etes maintenant au niveau : ", self.get_levelPersonnage())

        else :    
            pass




class PNG(Modele_Personnage):     
   def __init__(self, nomPersonnage, viePersonnage, attaquePersonnage, defensePersonnage, levelPersonnage, attaque_speciale):
        super().__init__(nomPersonnage, viePersonnage, attaquePersonnage, defensePersonnage, levelPersonnage)
         







class BOSS(Modele_Personnage):
 def __init__(self, nomPersonnage, viePersonnage, attaquePersonnage, defensePersonnage, levelPersonnage, attaque_speciale, PointAttackSpe): 
    super().__init__(nomPersonnage, viePersonnage, attaquePersonnage, defensePersonnage, levelPersonnage)    
    self.attaque_speciale = attaque_speciale
    self.PointAttackSpe = 50



class MonstresForts(Modele_Personnage):

    def __init__(self, nomPersonnage, viePersonnage, attaquePersonnage, defensePersonnage, levelPersonnage, attaque_speciale, PointAttackSpe):
        super().__init__(nomPersonnage, viePersonnage, attaquePersonnage, defensePersonnage, levelPersonnage)
        self.ExpADonner = 100
        self.attaque_speciale = attaque_speciale
        self.PointAttackSpe = 25
        #print(" /! Un monstre spécial apparait !\ ")
        #print("Nom :", nomPersonnage, "| Vie :", viePersonnage, "| Attaque :", attaquePersonnage, "| Defense :", defensePersonnage, "| Attaque speciale :", attaque_speciale, " | Niveau : ", levelPersonnage, "\n")

    def get_attaque_speciale(self):
        return self.attaque_speciale


class MonstresNormaux(Modele_Personnage):

    def __init__(self, nomPersonnage, viePersonnage, attaquePersonnage, defensePersonnage, levelPersonnage):
        super().__init__(nomPersonnage, viePersonnage, attaquePersonnage, defensePersonnage, levelPersonnage)
        self.ExpADonner = 50
        #print("Un", nomPersonnage ,"apparait !")
        #print("Nom :", nomPersonnage, "| Vie :", viePersonnage, "| Attaque :", attaquePersonnage, "| Defense :", defensePersonnage, " | Niveau : ", levelPersonnage, "\n")

    def damage(self, attaque):
        self.viePersonnage -= attaque
        print("Le monstre à subit", attaque, "dégats")   

    def get_ExpADonne(self):
        return self.ExpADonner

    def attack_monster(self, cible):
        cible.dommage(self.attaquePersonnage)
        print(cible.get_nomPersonnage(), "a prit", self.attaquePersonnage, "de dégats.\n")



###############################      Personnage du Jeux      ######################################



Robot = MonstresForts("Jarvis", 70, 50, 20, 100, 0)
Soldat = MonstresForts('Oleg', 20, 2, 0, 5, 1)
Alien = MonstresNormaux('Alien',20,2,0,5)
#Robot = MonstresNormaux('ROBOT',100,5,0,1,)


Soldat = PNG('Oleg', 20, 2, 0, 5, 1)
ViceCapitaine = PNG("Alexei", 0,0,0,0,0)

####################################################################################################  
#Epee = Modele_Arme("Epée", 20)
#Pistolet_Laser = Modele_Arme("Pistolet Laser", 35)
#rmure = Modele_Armure("combi",30)
'''Kevin.a_une_arme(Epee)
Kevin.a_une_armure(Armure)
Kevin.barre_Exp(100)
Kevin.Augment_level()
Kevin.recap()
'''

#Epee = Modele_Arme("Epee", 20)
#Kevin = hero("Kevin",20,10,20,1,0,None,None)
#Epee = Modele_Arme("Epee", 20)
#Armure = Modele_Armure("combi",30)
#Kevin.a_une_arme(Epee)
#Kevin.a_une_armure(Armure)
#Kevin.barre_Exp(100)
#Kevin.Augment_level()
#Kevin.recap()
#Couteau = Modele_Arme("couteau",25)
#Kevin.a_une_arme(Couteau)
#Kevin.recap()

