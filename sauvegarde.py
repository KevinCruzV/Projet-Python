import pickle
from Arme_et_Armure import * 
from inventaire import Inventaire
from Salle import *
import shutil



def Sauve(Hero, salle, inventaire):
    data = {
        "Héro" : Hero,
        "Inventaire": Inventaire,
        "Salle" : salle,
    }

    Sauve=open("sauve.pickle", "wb") 
    pickle.dump(data, Sauve)
    shutil.copyfile("sauve.pickle", "sauve.pickle.bak")
    Sauve.close()
        

def recupData():
    Load = open("sauve.pickle","rb")
    data = pickle.load(Load)
    return data

def dataRecap(Data):
    print("Chargement de la Partie sauvegardé")
    Data["Héro"].recap()





