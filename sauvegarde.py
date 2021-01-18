import pickle
from Arme_et_Armure import * 
from inventaire import Inventaire
from Salle import *




def Sauve(Hero, salle, inventaire):
    data = {
        "Héro" : Hero,
        "Inventaire": Inventaire,
        "Salle" : salle,
    }

    Sauve=open(os.path.join("sauve.pickle"), "wb") 
    pickle.dump(data, Sauve)
    Sauve.close()
        

def recupData():
    Load = open(os.path.join("sauve.pickle"),"rb")
    data = pickle.load(Load)
    return data

def dataRecap(Data):
    print("Chargement de la Partie sauvegardé")
    Data["Héro"].recap()





