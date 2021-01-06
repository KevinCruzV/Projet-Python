from combat import *
from Modele import Modele_Salle
from random import *
from inventaire import searchInventaire
from inventaire import Inventaire
from Arme_et_Armure import *
from time import *

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
            Hangar()
            SuppSalle(salle, nb)
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
    Salle_0 = Modele_Salle("Salle 0")
    print("\n")
    print("? : Hey ! HEY ! REVEILLE TOI ! \n")
    sleep(3)
    print("Vous vous réveillez dans une salle blanche... Autour de vous, il y du matériel informatique et une table d'opération avec dessus des instruments chirurgicaux... \n")
    sleep(4)
    print("? : C'est pas trop tôt, j'ai cru que tu te réveillerais jamais ! Moi c'est", Robot.nomPersonnage, ".\n")
    sleep(4)
    print(Robot.nomPersonnage,": Nous sommes dans la", Salle_0.get_nomSalle() ,"tu arrive a te souvenir de quelque chose ? \n")
    sleep(4)
    print("? : Où suis-je ? Que se passe t-il ? \n")
    sleep(3)
    print(Robot.nomPersonnage, " :... dans la", Salle_0.get_nomSalle() ,"! T'as rien écouté ou quoi ?! La mission a rencontré un petit imprévu, j'ai entendu une explosion alors je suis venu ici et j'ai du te sortir de ta capsule plus tôt que prévu... \n")
    sleep(6)
    Hero=hero(str(input("*Nom robot* : Ah et j'oubliais, quel est ton prénom ? \n")),10,5,0,1,0,None,None)
    sleep(3)
    print(Robot.nomPersonnage, ": Très bien ", Hero.get_nomPersonnage()," viens avec moi, allons voir ce qui s'est passé au plus vite. Oh et tu ferais mieux de prendre de quoi te défendre, on sait jamais ce qui nous attends là-bas. \n")
    sleep(6)
    print("Il y a un", Scalpel.get_nomArme() ,"sur une table d'opération... \n")
    sleep(5)
    prendre = int(input(("Que voulez vous faire ? 1 = Prendre l'objet | 2 = Laisser l'objet \n")))
    sleep(2)
    if prendre == 1:
        Inventaire["Armes"].append(Scalpel)
        print(Robot.nomPersonnage, ": Okay, je pense que ça fera l'affaire. \n")
        sleep(3)
        ouvrir = int(input("Voulez vous ouvrir l'inventaire pour l'équiper ? 1 = oui | 2 = non \n"))
        sleep(1)
        if ouvrir == 1:
            choix_inventaire(Inventaire, Hero)
            Hero.recap()
        else :
            print("*Vous rangez l'arme dans l'inventaire*\n")    
    if prendre == 2:
        sleep(2)
        print(Robot.nomPersonnage, ":... pas de", Scalpel.get_nomArme() ,"alors ? Comme tu voudras mais ne viens pas te plaindre. \n")
    print("Vous avancez et vous trouvez une porte avec un digicode")
    sleep(3)
    print(Robot.nomPersonnage, ": Si on veut sortir de la, il va nous falloir le code... \n")
    sleep(3)
    print("On peut voir une suite de chiffres griffonnée à coté de la porte :'90234' \n")
    sleep(4)
    print("Vous essayez d'ouvrir la porte en tapant sur le clavier du digicode \n")
    sleep(4)

    Code = int(input("Entrer un nombre :\n"))
    while Code != 90234 :
        sleep(2)
        print("*Warning Mauvais Code*\n")
        sleep(2)
        print(Robot.nomPersonnage, ": sans le bon code, on s'en ira jamais d'ici...\n")
        sleep(2)
        Code = int(input("Entrer un nombre :\n"))
    sleep(2)
    print("*Code Bon*")
    sleep(2)
    print("*Ouverture de la porte en cours*\n")
    sleep(3)
    print(Robot.nomPersonnage,": Non mais... qui est l'idiot qui a écrit le code ici ? Autant laisser la porte grande ouverte.\n")
    sleep(4)
    print("La porte s'ouvre, vous êtes éblouit par la lumière du couloir.\n")
    sleep(3)
    print("*tap* *tap* *tap*, des bruits de pas s'éloignent vers la gauche...\n")

    



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
    Vestiaire = Modele_Salle("Vestiaire")
    print("Le", Vestiaire.get_nomSalle(),"est sombre... Vous n'y voyez rien. Vous marchez à tâtons dans le noir lorsque vous butez sur un objet...\n " )
    sleep(3)
    print(Robot.nomPersonnage, ": C'est une",Lampe.get_nomObjet(),"! Avec ça on y verra plus clair ! \n")
    sleep(2)
    print("Vous ramassez la lampe et l'ajoutez à votre inventaire. \n")
    sleep(3)
    Inventaire["Objets rares"].append(Lampe)
    print("La",Lampe.get_nomObjet(),"éclaire le", Vestiaire.get_nomSalle() ,"... Mais plus vous y voyez clair, plus vous êtes effrayé. Du sang, des traces de griffes, tout est en désordre ! \n")
    sleep(5)
    print(Robot.nomPersonnage, ": Qu'est-ce qu'il s'est passé ici...", Hero.get_nomPersonnage(),", je ne sais pas quelle créature à bien pu faire ça, mais une chose est sûre, si elle nous trouve on est fichus ! Ne trainons pas là ! \n")
    sleep(6)
    print("Vous vous dirigez vers la sortie mais vous entendez une voix... \n")
    sleep(3)
    question1 = input("C'est un membre du vaisseau, il est à terre et appelle a l'aide. Allez vous l'aider ? y/n \n")
    if question1 == "n":
        sleep(3)
        print("Vous ne l'aidez pas et vous dirigez vers la sortie. \n")
        sleep(3)
        print(Robot.nomPersonnage, ": Je suis d'accord on ferais mieux d'y aller, et puis avec un peu de chance il s'en sortira... Qu'est-ce que ... Attention !! \n")
        sleep(5)
        print("Une ombre se dirige vers vous, vous l'éclairez avec la",Lampe.get_nomObjet(),". C'est un",Alien.get_nomPersonnage(),", il est couvert de sang... mais est-ce le sien ? \n")
        sleep(5)
        combat(Alien,Hero)
        if Hero.get_viePersonnage() <= 0:
            return 0
        else:
            print("On l'a échappé belle pour cette fois. Qu'est-ce qui a bien pu se passer pour que de tels monstres s'introduisent dans le vaisseau. \n")
            sleep(4)
            print("Vous quittez le",Vestiaire.get_nomSalle(),". \n")
            

    else :
        sleep(3)
        print(Robot.nomPersonnage,": Euh... tu es sur qu'on devrait l'aider, si la chose nous retrouve on va y passer. \n")
        sleep(4)
        print("Vous avancez vers lui mais... Il n'a plus de jambes, il a rampé jusqu'ici à la force de ses bras. Il est trop tard pour le secourir... \n")
        sleep(5)
        print(Robot.nomPersonnage,": J'en étais sûr, on aurait jamais du s'aventurer ici, et maintenant on va finir comme lui ! \n")
        sleep(5)
        print("Un grognement venant du fond du",Vestiaire.get_nomSalle(),"retentit, et ensuite des bruits de pas... les pas se rapprochent, ils seront bientôt tout près... \n")
        sleep(5)
        combat(Alien,Hero)
        if Hero.get_viePersonnage() <= 0:
            return 0
        else:
            sleep(3)
            print(Robot.nomPersonnage,": Bien joué", Hero.get_nomPersonnage(),"je ne pensais pas que tu allais t'en sortir, on a eu chaud. \n")
            sleep(4)
            question2 = input("En passant devant le corps du membre du vaisseau, vous découvrez une arme attachée à sa ceinture. Voulez-vous la ramasser ? y/n \n")
            if question2 == "n":
                sleep(2)
                print("Vous n'avez pas ramasser l'arme. \n")
                sleep(2)
                print(Robot.nomPersonnage,": Je pense que tu as raison, on devrait le laissez tranquille. \n")
            else:
                sleep(2)
                print("Vous avez trouvez un", Blaster_rouille.nomArme,". Vous l'ajoutez à votre inventaire. \n")
                Inventaire["Armes"].append(Blaster_rouille)
                sleep(3)
                question3 = input("Voulez vous ouvrir l'inventaire pour l'équiper ? y/n \n")
                if question3 == "y":
                    sleep(2)
                    choix_inventaire(Inventaire, Hero)
                    Hero.recap()
                else:
                    sleep(2)
                    print("*Vous rangez l'arme dans l'inventaire*")
                sleep(3)
                print(Robot.nomPersonnage,": Bonne initiative, avec ça le prochain monstre qui viendra nous attaquer a du soucis à se faire ! \n")
    


def Hangar():
    Hangar = Modele_Salle("Hangar")
    print("Vous entrez dans le", Hangar.get_nomSalle(), ". Vous sentez une odeur de souffre et de sang. \n")
    sleep(3)
    print(Robot.nomPersonnage,": Waouh c'est immense ici !. Tiens bizarre... il n'y a aucun vaisseaux et puis c'est quoi cette odeur. J'aime pas trop cet endroit... \n")
    sleep(6)
    print("Vous continuez d'avancer dans le", Hangar.get_nomSalle(), ". \nIl y a un vaisseau au loin. \n")
    sleep(3)
    print(Robot.nomPersonnage,": Regarde là-bas ! Il reste un vaisseau.", Hero.get_nomPersonnage() ,"on y va ? \n")
    sleep(3)
    question1 = input("Voulez-vous y aller ? y/n \n")
    if question1 == "y":
        sleep(2)
        print("Vous vous dirigez vers le vaisseau. \n")
        sleep(2)
        print(Robot.nomPersonnage,": Allons à l'intérieur ! \n")
        sleep(2)
        print("Les lumières sont allumées et le système de réchauffement aussi. \n")
        print(Robot.nomPersonnage,": Il est encore allumé. Qui aurait laisser un vaisseau allumé sans s'en servir ? \n")
        sleep(4)
        print(Robot.nomPersonnage,": Le pilote ! il est encore là ..... Il ne respire plus... on dirait qu'il cherchait à s'enfuir, mais de quoi ? On ferait bien de filer au plus vite, non ? \n")
        sleep(6)
        question2= int(input("Que voulez vous faire ?  1 = Fouillez dans les baggages | 2 = Filer d'ici \n"))
        sleep(2)
        if question2 == 1:
            print("Vous regardez dans les baggages. \n")
            sleep(2)
            print("Vous avez trouvé un exosquelette. Vous l'ajoutez à l'inventaire. \n")
            sleep(3)
            print(Robot.nomPersonnage, ": Ça alors, un exosquelette ! On pouvait pas trouver mieux ! \n")
            sleep(2)
            Inventaire["Armures"].append(Exosquelette)
            question3 = input("Voulez vous ouvrir l'inventaire pour l'équiper ? y/n \n")
            if question3 == "y":
                sleep(2)
                choix_inventaire(Inventaire, Hero)
                Hero.recap()
            else:
                sleep(2)
                print("*Vous rangez l'arme dans l'inventaire* \n")
        else:
            print(Robot.nomPersonnage, ": Suis moi, on s'en va d'ici ! \n")
            sleep(2)
            print("Vous sortez du vaisseau puis vous dirigez vers la sortie. \n")
            sleep(2)
            print("Vous quittez le", Hangar.get_nomSalle,". \n")
            
    else:
        sleep(2)
        (Robot.get_nomPersonnage,": Continuons par ici alors. \n")
        sleep(2)
        ("L'odeur de souffre s'intensifie et soudain, la lumière clignote. \n")
        sleep(3)
        (Robot.get_nomPersonnage,": Euh", Hero.get_nomPersonnage,"tu devrais regarder par ici... \n")
        sleep(3)
        ("Vous apercevez une silhouette au plafond. C'est un alien, il dort suspendu a la lampe. \n")
        sleep(4)
        (Robot.get_nomPersonnage,": C'est sûrement lui qui a tué celui dans le vaisseau... \n")
        sleep(3)
        question4 = int(input("Que voulez vous faire ?  1 = Venger votre coéquipier | 2 = S'en aller \n"))
        if question4 == 1:
            sleep(2)
            print(Robot.get_nomPersonnage,": C'est une blague hein ? Me dis pas que tu veux vraiment attaquer cette chose ! \n")
            sleep(3)
            print("Vous saisissez un morceau de métal au sol et le lancez sur l'alien \n")
            sleep(2)
            print("La lampe se brise, plongeant la salle dans l'obscurité et l'alien tombe au sol \n")
            sleep(4)
            question5 = int(input("Voulez vous utiliser a lampe de poche ? y/n \n"))
            if question5 == "y":
                sleep(2)
                print("Vous allumez votre lampe de poche \n")
                sleep(2)
                print("Le monstre est juste devant vous, il vous fixe avec de grands yeux noirs. \n")
                sleep(3)
                combat(Alien,Hero)
            else:
                print("Vous n'allumez votre lampe de poche \n")
                sleep(2)
                print("Des bruits de pas viennent dans votre direction... quelque chose est en train de courir vers vous. \n ")
                sleep(3)
                combat(Alien,Hero)
            if Hero.get_viePersonnage() <= 0:
                return 0
            else:
                sleep(2)
                print(Robot.get_nomPersonnage,": Tu devrais vraiment revoir ta façon de réfléchir, foncer dans la gueule du loup comme ça c'était pas une bonne idée ! \n")
                sleep(5)
                print("Vous quittez le", Hangar.get_nomSalle(),". \n")




        
    

def Armurerie():
    Armurerie = Modele_Salle("Armurerie")
    print("Vous arrivez devant la porte de", Armurerie.get_nomSalle())
    print("Vous trouvez par terre un item de soin = ", Objet_de_Quete.get_nomObjet(kit_de_soins))
    ramasser = int(input(("Que voulez vous faire? 1 = Ramasser l'objet | 2 = Laisser l'objet")))
    if ramasser == 1:
        Inventaire["Soins"].append(kit_de_soins)
        Inventaire["Soins"].append(kit_de_soins)
    print("Vous trouvez également un", Pistolet_Laser.nomArme)
    ramasser = int(input("Que voulez vous faire ? 1 = Ramasser l'objet | 2 = Laisser l'objet"))
    if ramasser == 1:
        Inventaire["Armes"].append(Pistolet_Laser)


#Random_Salle()
#choixSalles()
Alien = MonstresNormaux('Alien',20,2,0,5)
Robot = MonstresNormaux('ROBOT',100,5,0,1,)
Hero = hero('Kevin',10,10,10,10,0,0,0)
choix_inventaire(Inventaire, Hero)