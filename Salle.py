from Modele import Modele_Salle

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



    #Elle peut etre la premiere salle

def Vestiaire():
    Vestiaire = Modele_Salle("Vestaire")
    print("Le", Vestiaire.get_nom(),"est sombre, vous n'y voyez rien. Vous essayez de marché dans le noir lorsque vous butez sur objet. Mais quel est-il ?\n " )
    print("TO DO : fonction Lampe")
    print("TO DO : fonction Inventaire")
    print("Vous pouvez maintenant voir. Mais... Un horrible spectacle est devant vous, du sang.. Du sang partout et des traces de griffure")
    print("TO DO : fonction event")
    print("TO DO : fonction Monstre")
    print("TO DO : fonction Combat")


