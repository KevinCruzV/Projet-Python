from Modele_Salle import Modele_Salle

def Refectoire():
    Refectoire = Modele_Salle("Refectoire")
    Q = input("Il y a une faille dans le " + Refectoire.get_nom() + " elle vous fait perdre de l'oxygène. Voulez vous continuer ? o/n")
    if Q == "n":
        print("TO DO : fonction quitter")
    else :
        print("Vous continuez d'avancer dans le refectoire, mais une énorme silouhette dévore un homme. Elle se retourne et vous regarde.")
        print("TO DO : fonction monstre")
        print("TO DO : fonction combat")
        print("TO DO : fonction item --> le personnage récupère de la nourriture dans les placard ")

Refectoire()