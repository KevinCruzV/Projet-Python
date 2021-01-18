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
champignons_blancs = Objet_de_soin("Champignons blancs", 15)
fleurs_oranges = Objet_de_soin("Fleurs oranges", 20)
plantes_bleues = Objet_de_soin("Plantes bleues", 30)
Seringue_adrenaline = Objet_de_soin("Seringue d'adrénaline", 10)

#Armes :
Epee = Modele_Arme("Epee", 20)
Gant = Modele_Arme("Super Gant", 10)
Sabre_Laser = Modele_Arme("Sabre Laser", 15)
Scalpel = Modele_Arme("Scalpel", 5)
Blaster_Rouille = Modele_Arme("Blaster rouillé", 8)
Fouet_Laser = Modele_Arme("Fouet Laser", 15)
Pistolet_Laser = Modele_Arme("Pistolet Laser", 35)
Pistolet_Electrique = Modele_Arme("Pistolet à impulsion élecrtrique", 25)
Fusil_Ultraviolet = Modele_Arme("Fusil Ultraviolet", 30)
Canon_Souffleur = Modele_Arme("Canon Souffleur", 30)
Fouet_Electrique = Modele_Arme("Fouet Electrique", 23)
Poignard_Solaire = Modele_Arme("Poignard Solaire", 25)
Gantelets_Electriques = Modele_Arme("Gantelets Electriques", 20)
Mitaines_Gamma = Modele_Arme("Mitaines Gamma", 26)
Gants_Combutsion = Modele_Arme("Gants de combustion", 24)

#Armures :
Combinaison_Spatial_trouee = Modele_Armure("Combinaison spatial trouée", 5)
Combinaison_Spatial_en_Carbone = Modele_Armure("Combinaison Spatial en Carbone", 12)
Pyjama = Modele_Armure("Pyjama", 0)
Buste_Polyethane = Modele_Armure("Buste en Polyethane",16) 
Exosquelette = Modele_Armure("Exosquelette", 22)
Combinaison_medical = Modele_Armure("Combinaison médical",4)

#Objets de Quetes :
Cle_de_la_Salle_des_Capsules_de_sauvetage = Objet_de_Quete("Clé de la salle des capsules de sauvetage")
Lampe = Objet_de_Quete("lampe de poche")
Talkie_Walkie = Objet_de_Quete("talkie walkie")
Cle_Demarage_Vaisseau = Objet_de_Quete("clé de démarage du vaisseau")
MicroPuce = Objet_de_Quete("micro-puce")




