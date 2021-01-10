import pickle
from Arme_et_Armure import * 
from inventaire import Inventaire
from Salle import *



def Sauve(Hero, salle, inventaire):
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

def dataRecap(Data):
    Data["Héro"].recap()
    print("Inventaire =",Data["Inventaire"])



#Hero = hero("Kevin",20,10,20,1,0,None,None)
#Epee = Modele_Arme("Epee", 20)
#Armure = Modele_Armure("combi",30)
#Hero.a_une_arme(Epee)
#Hero.a_une_armure(Armure)
#Hero.barre_Exp(100)
#Hero.Augment_level()
#Hero.recap()
#Sauve()

