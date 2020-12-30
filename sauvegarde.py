import pickle
from Map import *
from Personnage import *
from Modele import *
from Arme_et_Armure import *
from Salle import *
from inventaire import Inventaire
from combat import *

def Sauve(Hero, inventaire):
    data = {
        "Héro" : Hero,
        "Inventaire": Inventaire,
        "Salle" : Salles,
    }   
    Sauve=open("sauve.pickle", "wb") 
    pickle.dump(data, Sauve)
    Sauve.close()

def recupData():
    Load = open("sauve.pickle","rb")
    data = pickle.load(Load)
    return data

#Hero1 = Hero("Kevin",20,10,20,1,0,None,None)
#Epee = Modele_Arme("Epee", 20)
#Armure = Modele_Armure("combi",30)
#Hero1.a_une_arme(Epee)
#Hero1.a_une_armure(Armure)
#Hero1.barre_Exp(100)
#Hero1.Augment_level()
#Hero1.recap()

