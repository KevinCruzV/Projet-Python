from Modele import Modele_Arme
from Modele import Modele_Armure
from Modele import Objet_de_Quete


class Objet_de_soin(Objet_de_Quete):
    
    def __init__(self, nomObjet, vieEnPlus):
        super().__init__(nomObjet)
        self.vieEnPlus = vieEnPlus
        


class Objet_de_defense(Objet_de_Quete):
    
    def __init__(self, nomObjet, defenseEnPlus):
        super().__init__(nomObjet)
        self.defenseEnPlus = defenseEnPlus


        
#Armes :

Blaster_rouille = Modele_Arme("Blaster Rouillé", 5)
fouet_laser = Modele_Arme("Fouet Laser", 15)


#Armure :
Combinaison_Spatial_trouée = Modele_Armure("Combinaison spatial trouée", 5)
Combinaison_Spatial_en_Carbone = Modele_Armure("Combinaison Spatial en Carbone", 15)

#Objets de Quetes :
Cle_refectoire = Objet_de_Quete("Clé du réfectoire")
Seringue_adrenaline = Objet_de_soin("Seringue d'adrénaline", 10)




