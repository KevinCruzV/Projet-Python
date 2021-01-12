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
Pistolet_electrique = ("Pistolet à impulsion électrique", 25)
Fusil_ultraviolet = ("Fusil ultraviolet", 30)
Sabre_laser = ("Sabre laser", 27)
Canon_souffleur =("Canon souffleur", 30)
Fouet_electrique = ("Fouet électrique", 23)
Poignard_solaire = ("Poignard solaire", 25)
Gantelets_electriques = ("Gantelets électriques", 20)
Mitaines_gamma = ("Mitaines gamma", 26)
Gants_combustion = ("Gants de combustion", 24)



#Armure :
Combinaison_Spatial_trouee = Modele_Armure("Combinaison spatiale trouée", 5)
Combinaison_Spatial_en_Carbone = Modele_Armure("Combinaison spatiale en carbone", 15)
Exosquelette = Modele_Armure("Exosquelette", 20)

#Objets de Quetes :
Cle_de_la_Salle_des_Capsules_de_sauvetage = Objet_de_Quete("Clé de la salle des capsule de sauvetage")
Seringue_adrenaline = Objet_de_soin("Seringue d'adrénaline", 10)
Lampe = Objet_de_Quete("lampe de poche")




