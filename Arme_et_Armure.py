from Modele import Modele_Arme
from Modele import Modele_Armure
from Modele import Objet_de_Quete



class Objet_de_soin(Objet_de_Quete):

    def __init__(self, nomObjet, vieEnPlus):
        super().__init__(nomObjet)
        self.vieEnPlus = vieEnPlus
        

    def get_VieEnPlus(self):
        return self.vieEnPlus

    

class Objet_de_defense(Objet_de_Quete):
    
    def __init__(self, nomObjet, defenseEnPlus):
        super().__init__(nomObjet)
        self.defenseEnPlus = defenseEnPlus


        
#Objets de soins :

kit_de_soins = Objet_de_soin("Kit de soins", 40)
champignons_blancs = Objet_de_soin("Champignons blancs", 70)
fleurs_oranges = Objet_de_soin("Fleurs oranges", 70)
plantes_bleues = Objet_de_soin("Plantes bleues", 70)

#Armes :
Scalpel = Modele_Arme("Scalpel",5)
Blaster_rouille = Modele_Arme("Blaster Rouillé", 8)
Fouet_laser = Modele_Arme("Fouet Laser", 15)
Epee = Modele_Arme("Epee", 20)
Pistolet_Laser = Modele_Arme("Pistolet Laser", 35)

#Armure :
Combinaison_Spatial_trouee = Modele_Armure("Combinaison spatial trouée", 5)
Combinaison_Spatial_en_Carbone = Modele_Armure("Combinaison Spatial en Carbone", 15)
Exosquelette = Modele_Armure("Exosquelette", 20)

#Objets de Quetes :
Cle_de_la_Salle_des_Capsules_de_sauvetage = Objet_de_Quete("Clé de la salle des capsule de sauvetage")
Seringue_adrenaline = Objet_de_soin("Seringue d'adrénaline", 10)
Lampe = Objet_de_Quete("lampe de poche")




