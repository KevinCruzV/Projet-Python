from combat import *
from Modele import Modele_Salle
from random import *
from inventaire import searchInventaire
from inventaire import *
from Arme_et_Armure import *

#####  Fonction pour lancer les salles  #####
Salles = [1,2,3]

def choixSalles(salle):
    nb = randint(1, 3)
    for i in salle:
        if nb == 1:
            Vestiaire()
            SuppSalle(salle, nb)
        if nb == 2:
            Refectoire()
            SuppSalle(salle, nb)
        if nb == 3:
            pass
        i += 1




'''def Random_Salle():
    #salles=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    salles = [1, 2, 3]
    nb = randint(1, 3)
    for i in salles:
        if SearchFor(salles, nb):
            if nb == 1:
                Vestiaire()
                SuppSalle(salles,nb)
            elif nb == 2:
                Refectoire()
                SuppSalle(salles,nb)
            #Il faut continuer a faire les salles

        else :
            nb = randint(1,22)
            i=i+1'''



#Regarde si la salle existe
def SearchFor(L,X):
    for v in L:
        if v == X:
            return True

        return False

#Supprime une salle apres qu'elle soit utilisé une fois

def SuppSalle(Liste,num):
    c = 0
    for v in Liste:
        if v == num:
            c = c + 1

    for i in range(c):
        Liste.remove(num)

    return Liste






#####  Salles #####


def Salle_0():
    pass

def Salle_final():
    pass


def Refectoire():
    inventaire = input("Avez vous la clé du réféctoire ? y/n")
    if inventaire == 'y':
        if searchInventaire(Inventaire, Cle_refectoire) :
            Refectoire = Modele_Salle("Refectoire")
            Q = input("Il y a une faille dans le " + Refectoire.get_nomSalle() + " elle vous fait perdre de l'oxygène. Voulez vous continuer ? o/n")
            if Q == "n":
                print("TO DO : fonction quitter")
            else :
                print("Vous continuez d'avancer dans le refectoire, mais une énorme silouhette dévore un homme. Elle se retourne et vous regarde.")
                print("TO DO : fonction monstre")
                print("TO DO : fonction combat")
                print("TO DO : fonction item --> le personnage récupère de la nourriture dans les placard ")    
        else :
            print("Vous n'avez pas la clé du réfectoire !")
            print("TO DO : return au point ou on est")

    #Elle peut etre la premiere salle

def Vestiaire():
    Vestiaire = Modele_Salle("Vestaire")
    print("Le", Vestiaire.get_nomSalle(),"est sombre... Vous n'y voyez rien. Vous essayez de marché dans le noir lorsque vous butez sur un objet. Mais quel est-il ?\n " )
    print("TO DO : fonction Lampe")
    print("TO DO : fonction Inventaire")
    print("Vous pouvez maintenant voir. Mais... Un horrible spectacle est devant vous, du sang.. Du sang partout et des traces de griffure")
    print("TO DO : fonction event")
    print("TO DO : fonction Monstre")
    print("TO DO : fonction Combat")


def Hangar():
    Hangar = Modele_Salle("Hangar")
    print("Vous entrez dans l'immense", Hangar.get_nomSalle(),". Vide de vaisseaux, vous sentez une odeur de souffre et de sang. Lorsque tout a coup ! Un grognement étrange se fait entendre. PLOUC, PLOUC, vous levez la tête") 
    print("TO DO : Combat avec un Monstre Moyen")

def Armurerie():
    Armurerie = Modele_Salle("Armurerie")
    print("Vous arrivez devant la porte de", Armurerie.get_nomSalle())
    print("Vous trouvez par terre un item de soin = ", Objet_de_Quete.get_nomObjet(kit_de_soins))
    ramasser = int(input(("Que voulez vous faire? 1 = Ramasser l'objet | 2 = Laisser l'objet")))
    if ramasser == 1:
        Inventaire["Soins"].append(kit_de_soins)
        Inventaire["Soins"].append(kit_de_soins)
    print("Vous trouvez également un", Pistolet_Laser.nomArme)
    ramasser = int(input("Que voulez vous faire? 1 = Ramasser l'objet | 2 = Laisser l'objet"))
    if ramasser == 1:
        Inventaire["Armes"].append(Pistolet_Laser)


#Random_Salle()
#choixSalles()