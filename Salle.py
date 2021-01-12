from combat import *
from Modele import Modele_Salle
from random import *
from Personnage import *
from inventaire import searchInventaire
from inventaire import Inventaire
from Arme_et_Armure import *
from time import *



#####  Fonction pour lancer les salles  #####
Salles = [1,2,3]

# def choixSalles(salle):
#     nb = randint(1, 3)
#     P = VarHero(Hero)
#     for i in salle:
#         if nb == 1:
#             Vestiaire(P)
#             SuppSalle(salle, nb)
#         if nb == 2:
#             Refectoire(P)
#             SuppSalle(salle, nb)
#         if nb == 3:
#             Hangar(P)
#             SuppSalle(salle, nb)
#         i += 1




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


def Salle_0(Hero):
    Salle_0 = Modele_Salle("salle des capsules")
    print("\n")
    print("Voix : Hey ! HEY ! REVEILLE TOI ! \n")
    sleep(3)
    print("Vous vous réveillez dans une salle blanche... Autour de vous, il y du matériel informatique et une table d'opération avec dessus des instruments chirurgicaux... \n")
    sleep(5)
    print("Voix : C'est pas trop tôt, j'ai cru que tu te réveillerais jamais ! Moi c'est", Robot.nomPersonnage, ". Je te parle a travers les hauts parleurs du vaisseau !\n")
    sleep(4)
    print(Robot.nomPersonnage,": Nous sommes dans la", Salle_0.get_nomSalle() ,"tu arrive a te souvenir de quelque chose ? \n")
    sleep(4)
    print("? : Où suis-je ? Que se passe t-il ? \n")
    sleep(3)
    print(Robot.nomPersonnage, " :... dans la", Salle_0.get_nomSalle() ,"! T'as rien écouté ou quoi ?! La mission a rencontré un petit imprévu, j'ai entendu une explosion alors je suis venu ici et j'ai du te sortir de ta capsule plus tôt que prévu... \n")
    sleep(6)

    print(Robot.nomPersonnage, ": Très bien ", Hero.get_nomPersonnage()," c'est ça ? Viens avec moi, allons voir ce qui s'est passé au plus vite. Oh et tu ferais mieux de prendre de quoi te défendre, on sait jamais ce qui nous attends là-bas. \n")
    sleep(6)
    print("Il y a un", Scalpel.nomArme ,"sur une table d'opération... \n")
    sleep(5)
    prendre = int(input(("Que voulez vous faire ? 1 = Prendre l'objet | 2 = Laisser l'objet \n")))
    sleep(2)
    print("\n")
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
            print("Vous rangez l'arme dans l'inventaire \n")    
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
    VarHero(Hero)
    Sauve(Hero, Laboratoire, Inventaire)
    


def Salle_final(hero):
    print("\n")
    print(hero.get_nomPersonnage(),": Jarvis ? Jarvis ? Mais pourquoi il ne me repond plus ?")
    sleep(3)
    print("Vous voyez le plan qui vous indique la salle de controle")
    sleep(3)
    print("vous tournez a droite")
    Salle_de_controle = Modele_Salle("Salle de controle")
    #Continuer la salle final

#Salle Bonus
def CapsuleDeSauvetage(hero):
    sleep(2)
    print("vous etes devant la salle des capsule de sauvetage")
    Inventaire = input("Avez vous la clé de la salle ? y/n\n")
    if Inventaire == 'y':
        if searchInventaire(Inventaire,Cle_de_la_Salle_des_Capsules_de_sauvetage) :
            CapsuleDeSauvetage = Modele_Salle("Salle des capsules de sauvetage")



        else :
            print("Vous n'avez pas la clé du réfectoire !")
            
    VarHero(Hero)
    Sauve(Hero, Laboratoire, Inventaire)
    

def Vestiaire(Hero):
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
                sleep(4)
                print("Vous quittez le",Vestiaire.get_nomSalle(),". \n")
    VarHero(Hero)
    Sauve(Hero, Laboratoire, Inventaire)


def Hangar(Hero):
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
                print("*Vous rangez l'arme dans l'inventaire* \n")
                print(Robot.nomPersonnage, ": Suis moi, on s'en va d'ici ! \n")
                sleep(2)
                print("Vous sortez du vaisseau puis vous dirigez vers la sortie. \n")
                sleep(2)
                print("Vous quittez le", Hangar.get_nomSalle,". \n")                
            else:
                sleep(2)
                print("*Vous rangez l'arme dans l'inventaire* \n")
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
    VarHero(Hero)
    Sauve(Hero, Laboratoire, Inventaire)

def Laboratoire():
    Laboratoire = Modele_Salle("Laboratoire")
    print("Vous arrivez dans le", Laboratoire.get_nomSalle(),". La pièce est faiblement illuminée par les lampes de bureau laissées allumées. \n")
    sleep(4)
    print(Robot.get_nomPersonnage(),":", Hero.get_nomPersonnage() ,"il y a quelqu'un assis là-bas. Il a l'air mal en point... \n")
    sleep(4)
    print("? : Hé... approche... des aliens se sont introduits dans le vaisseau... on était censés être à l'abri mais il y a eu une explosion. \n")
    sleep(5)
    print("? : Un d'eux m'a eu... il devait être contagieux, la morsure s'est infectée... je ne peux déjà plus bouger, si ça continue je vais sûrement y rester... \n")
    sleep(6)
    print("? : Moi c'est", Soldat.get_nomPersonnage() ,"...et il va falloir que tu m'aide pour qu'on s'en sorte tout les deux. *kof**kof* \n")
    sleep(5)
    print(Robot.get_nomPersonnage(),":", Hero.get_nomPersonnage(),"tu veux l'aider je suppose ? \n")
    sleep(2)
    question1 = int(input("Que voulez vous faire ? 1 = L'aider | 2 = Passer mon chemin \n"))
    if question1 == 1:
        print("Vous décidez de l'aider. \n")
        sleep(2)
        print(Robot.get_nomPersonnage(),": Le contraire m'aurait étonné, mettons nous au travail alors ! \n")
        sleep(4)
        print(Soldat.get_nomPersonnage(),": Merci infiniment ! Il va falloir que tu crée un remède... tu vas devoir mélanger 10g de sodium... avec 20ml de soude *kof*. Tu passeras ensuite à la seconde partie... il s'agira de mélanger la poudre de carbone, il en faut 24g *kof* avec des cristaux d'uranium, mets en 3 maximum... et pour le dernier igrédient... c'est *kof**kof*... \n")
        sleep(10)
        print(Robot.get_nomPersonnage(),": C'est pas vrai ! Il a perdu connaissance...mais il respire encore, il est pas trop tard pour le sauver !\n")
        sleep(5)
        print(Robot.get_nomPersonnage(),": Donc résumons, 20g de sodium, 10ml de soude. Ensuite 24g de poudre de carbone et 4 cristaux d'uranium.\n")
        sleep(6)
        print("Vous avancez vers la table la plus proche et commencez à créer le remède.\n")
        sleep(4)
        remede = []
        while len(remede) < 4:
            Q1 = input("Que voulez vous ajouter ?")
            Q2 = input("Quelle quantité ?")
            remede.append(str(Q1) + " : " + str(Q2))
        sleep(2)
        print(Robot.get_nomPersonnage(),": Maintenant il reste le dernier ingrédient, il a pas eu le temps de nous le dire... Il reste que deux ingrédients, c'est forcément l'un d'eux.\n")
        sleep(5)
        print("À votre droite, un flacon rouge, de l'acide sulfurique. À votre gauche, un flacon bleu, du mercure. \n")
        sleep(5)
        print(Robot.get_nomPersonnage(),":", Hero.get_nomPersonnage(),"choisis bien, tu n'as qu'une seule chance. \n")
        sleep(4)
        question2 = int(input("Quel flacon choisissez vous ? 1 = L'acide sulfurique | 2 = Le mercure \n"))
        if question2 == 1:
            sleep(2)
            print(Robot.get_nomPersonnage(),": Très bien, ajoute lentement l'acide sulfurique dans notre préparation. \n")
            remede.append("acide sulfurique")
        else:
            sleep(2)
            print(Robot.get_nomPersonnage(),": D'accord, met le mercure dans la solution, n'en renverse pas surtout. \n")
            remede.append("mercure")
        sleep(1)
        print("Votre remède est constitué de :")
        sleep(1)
        for i in remede:
            print(i)
        sleep(4)
        print("Vous vous approchez de", Soldat.get_nomPersonnage(),", il respire lentement et est à bout de force. Vous lui faites boire le remède. \n")
        sleep(4)
        print(Robot.get_nomPersonnage(), ": Voilà une bonne chose de faite. \n")
        sleep(2)
        print("Soundain, sa peau se noircit, ses pupilles s'agrandissent et il a l'air de gonfler de l'intérieur. \n")
        sleep(4)
        print(Robot.get_nomPersonnage(),": On dirait que le remède n'a pas marché ! Attention",Hero.get_nomPersonnage(),"! \n")
        sleep(4)
        combat(Soldat,Hero)
        if Hero.get_viePersonnage() <= 0:
                return 0
        print(Robot.get_nomPersonnage(),": C'était plutôt impressionnant ! Bien joué",Hero.get_nomPersonnage(),"! \n")
        sleep(4)
        print("Vous vous dirigez vers la sortie. Il y a des kits médicaux dans un placard ouvert. \n")
        sleep(4)
        question3 = input("Voulez vous les ramasser ? y/n \n")
        if question3 == "y":
            Inventaire["Soins"].append(kit_de_soins)
            sleep(2)
            print("Vous avez trouvé des kits médicaux. Vous les rangez dans votre inventaire. \n")    
        else:
            pass
        sleep(4)
        print("Vous quittez le", Laboratoire.get_nomSalle(),". \n")
    else:
        print("Vous ne l'aidez pas.")
        sleep(2)
        print(Robot.get_nomPersonnage(),"Oh... euh d'accord continuons pas là. \n")
        sleep(4)
        print("Vous approchez de la serre où sont stockées les herbes médicinales. La porte est verrouillée. Un écran interactif s'allume.")
        sleep(4)
        print("BOT : Bienvenue à vous ! \n")
        sleep(2)
        passe = None
        while passe == None:
            question5 = int(input("BOT : Avez-vous le passe pour entrer ? 1 = Oui | 2 = Je l'ai perdu \n"))
            if question5 == 1:
                sleep(2)
                print("BOT : Aucun passe détecté. \n")
            else:
                passe = 1
        sleep(2)        
        print("BOT : Vous allez être soumis à un test pour vérifier votre identité. \n")
        sleep(4)
        print("BOT : Initialisation de l'épreuve d'authentification. \n")
        sleep(4)
        essais = 0
        while True:
            question6 = input()("BOT : Je commence la nuit, et finis au matin, on me trouve au fond du jardin, et au milieu de l'étang. Qui suis-je ? \n")
            if question6 == "n" or question6 == "N":
                print("BOT : Bonne réponse ! \n")
                sleep(2)
                break
            else:
                print("Mauvaise réponse ! \n")
                sleep(2)
            essais = essais + 1
            if essais > 3:
                print(Robot.get_nomPersonnage(),": C'est peut-être une lettre, non ? \n")
                sleep(1)
            if essais > 5:
                print(Robot.get_nomPersonnage(),": Je crois que j'ai trouvé ! C'est sûrement la lettre n ! \n")
                sleep(2)
        print("BOT : Ouverture de la porte en cours... \n")
        sleep(2)
        print("La porte s'ouvre et vous entrez dans la serre.")
        sleep(4)
        print(Robot.get_nomPersonnage(),": Waouh ça en fait des plantes ! Regarde par ici, elles ont de drôles de formes. Prenons en plusieurs, ça peut servir. \n")
        sleep(4)
        print("Des plantes bleues phosphorescentes sont plantées dans de la terre humide. À côté d'elles se trouvent des fleurs oranges dont les pétales flottent dans l'air. De l'autre côté, des champignons blancs produisent de la vapeur. \n")
        sleep(7)
        question7 = int(input("Quelle plante voulez vous prendre en premier ? 1 = Les plantes bleues | 2 = Les fleurs oranges | 3 = Les champignons blancs \n"))
        if question7 == 1:
            sleep(2)
            print("Vous arrachez les plantes bleues de la terre humide et les rangez dans votre inventaire. \n")
            Inventaire["Soins"].append(plantes_bleues)
        if question7 == 2:
            sleep(2)
            print("Vous arrachez les fleurs oranges et les rangez dans votre inventaire. \n")
            Inventaire["Soins"].append(fleurs_oranges)
        if question7 == 3:
            sleep(2)
            print("Vous arrachez les champignons blancs et les rangez dans votre inventaire. \n")
            Inventaire["Soins"].append(champignons_blancs)
        sleep(4)
        print("BOT : CODE ERREUR ! CODE ERREUR ! Un objet à été retiré de son emplacement initial ! \n")
        sleep(4)
        print("Des lumières rouges clignotent et la porte commence à se refermer. \n")
        sleep(4)
        print(Robot.get_nomPersonnage(),": Oh oh... Je crois qu'on était pas censés prendre ça.",Hero.get_nomPersonnage(),"tant pis pour les autres plantes on a pas le temps, si la porte se referme on restera coincés ici pour toujours ! \n")
        sleep(6)
        print("Vous courrez vers la sortie de la serre et quittez le", Laboratoire.get_nomSalle(),"par la même occasion. \n")
        
    VarHero(Hero)
    Sauve(Hero, Laboratoire, Inventaire)

    
def Armurerie(Hero):
    Armurerie = Modele_Salle("Armurerie")
    print("Vous arrivez devant la porte de l'", Armurerie.get_nomSalle(),". \n")
    sleep(2)
    print("Il y a un trou dans la porte. \n")
    sleep(2)
    print(Robot.get_nomPersonnage(),": C'est quelqu'un qui a du forcer pour entrer, c'est pas rassurant tout ça. \n")
    sleep(3)
    print("Vous vous faufillez par l'ouverture et entrez dans l'", Armurerie.get_nomSalle(),". \n")
    sleep(2)
    print("C'est une salle pleine de coffres et d'armoires.")
    sleep(2)
    print(Robot.get_nomPersonnage(),":", Hero.get_nomPersonnage(),"on devrait faire le plein d'armes tant qu'on est ici. \n")
    sleep(3)
    print("Vous ouvrez un coffre. Il est vide. \n")
    sleep(2)
    print(Robot.get_nomPersonnage(),": Quoi ?! Ah... maintenant que j'y pense c'est logique, les membres de l'équipage ont dû prendre les armes en entendant l'alerte d'intrusion... \n")
    sleep(4)
    print("Vous apercevez un atelier au fond de l'",Armurerie.get_nomSalle(),". \n")
    sleep(3)
    question1 = input("Voulez vous y aller ? y/n \n")
    if question1 == "y":
        print("Vous vous approchez de l'atelier. Il y a des outils pour fabriquer des armes. À côté, un carton d'objets non utilisés.")
        sleep(4)
        print(Robot.get_nomPersonnage(),": Tu veux construire une arme ?! Tu t'y connais au moins ? \n")
        sleep(3)
        input("1 = Biensûr que je m'y connais ! | 2 = Ça vaut le coup d'essayer... \n")
        sleep(2)
        print("Vous commencez la réalisation de l'arme avec les divers objets du carton. \n")
        sleep(2)
        objet1 = None
        objet2 = None
        while objet1 == None or objet2 == None:
            print("Que veux tu ajouter en premier ? \n")
            sleep(1)
            question2 = int(input("1 = Un sèche-cheveux | 2 = Une poignée de guidon d'un vélo | 3 = Des gants en microfibre \n"))
            sleep(2)
            if question2 == 1:
                objet1 = "le sèche-cheveux"
                print("Vous saisissez le sèche-cheveux. \n")
            elif question2 == 2:
                objet1 = "la poignée de guidon"
                print("Vous saisissez la poignée de guidon. \n")
            elif question2 == 3:
                objet1 = "les gants en microfibre"
                print("Vous saisissez les gants en microfibre. \n")
            while objet1 == None or objet2 == None:
                print("Que veux tu ajouter en deuxième ? \n")
                sleep(1)
                question2 = int(input("1 = des câbles électriques | 2 = un mini panneau solaire | 3 = un chalumeau \n"))
                sleep(2)
                if question2 == 1:
                    print("Vous assemblez les câbles électriques avec", objet1,". \n")
                    objet2 = "les câbles électriques"
                elif question2 == 2:
                    print("Vous attachez le panneau solaire avec", objet1,". \n")
                    objet2 = "le panneau solaire"
                elif question2 == 3:
                    print("Vous fixez le chalumeau sur", objet1,". \n")
                    objet2 = "le chalumeau" 
                    sleep(4)
                print("Ton objet est constitué de : \n")
                i = 1
                for arme in objet1, objet2:
                    print("Objet",i,":",arme)
                    i = i + 1
                    sleep(3)
                question3 = int(input("Que voulez vous faire ? 1 = Confirmez la sélection | 2 = Recommencer du début \n"))
                if question3 == 1:
                    pass
                elif question3 == 2:
                    objet1, objet2 = None, None
                    break
        if objet1 == "le sèche-cheveux":
            if objet2 == "les câbles électriques":
                sleep(2)
                print("C'est un pistolet à impulsion électrique ! L'énergie s'accumule dans ses câbles électriques et envoi une décharge de pas moins de 30 000 ampères, correspondant à une tension de 100 millions de volts. C'est l'équivalent de ce que la foudre libère en un éclair ! Vos ennemis auront le coup de foudre garantit ! \n")
                sleep(4)
                Inventaire["Armes"].append(Pistolet_electrique)
                print("Le nouvel objet a été ajouté à votre inventaire. \n")
            elif objet2 == "le panneau solaire":
                sleep(2)
                print("C'est un fusil ultraviolet ! Son panneau solaire concentre l'énergie qu'il reçoit et brûle à une forte intensité. Ce serait comme de s'approcher à 20km du Soleil. Parfait pour se faire griller un steak ( Un peu cramé... ). \n")
                sleep(4)
                Inventaire["Armes"].append(Fusil_ultraviolet)
                print("Le nouvel objet a été ajouté à votre inventaire. \n")
            elif objet2 == "le chalumeau":
                sleep(2)
                print("C'est un canon souffleur ! La puissance du sèche-cheveux combiné à la chaleur du chalumeau, ça fait beaucoup certes, mais c'est efficace ! Ça reviendrait à se placer en dessous du moteur d'une fusée en plein décollage ou dans le cratère d'un volcan en éruption. À cette chaleur, on n'a même pas le temps de se sentir brûler, promis ! \n")
                sleep(4)
                Inventaire["Armes"].append(Canon_souffleur)
                print("Le nouvel objet a été ajouté à votre inventaire. \n")
        elif objet1 == "la poignée de guidon":
            if objet2 == "les câbles électriques":
                sleep(2)
                print("C'est un fouet électrique ! Ses fils se chargent en électricité selon la puissance avec laquelle vous le lancez. Si vous avez une bonne poigne, vos ennemis ne s'en sortirons pas qu'avec des ampoules ! \n")
                sleep(4)
                Inventaire["Armes"].append(Fouet_electrique)
                print("Le nouvel objet a été ajouté à votre inventaire. \n")
            elif objet2 == "le panneau solaire":
                sleep(2)
                print("C'est un poignard solaire ! Sa lame est un concentré d'énergie solaire, elle est immatérielle, mais ce qui la traverse ressort en cendres. À tenir hors de portée des enfants ! \n")
                sleep(4)
                Inventaire["Armes"].append(Poignard_solaire)
                print("Le nouvel objet a été ajouté à votre inventaire. \n")
            elif objet2 == "le chalumeau":
                sleep(2)
                print("C'est un sabre laser ! Le chalumeau diffuse une flamme si puissance qu'elle se transforme en laser. Même le métal le plus puissant se coupe comme du beurre avec ça ! \n")
                sleep(4)
                Inventaire["Armes"].append(Sabre_laser)
                print("Le nouvel objet a été ajouté à votre inventaire. \n")
        elif objet1 == "les gants en microfibre":
            if objet2 == "les câbles électriques":
                sleep(2)
                print("Ce sont des gantelets électriques ! L'électricité  se propage dans les gants et quand elle atteind sa charge maximale, elle la projette directement sur la cible. Ça décoiffe ! \n")
                sleep(4)
                Inventaire["Armes"].append(Gantelets_electriques)
                print("Le nouvel objet a été ajouté à votre inventaire. \n")
            elif objet2 == "le panneau solaire":
                sleep(2)
                print("Ce sont des mitaines gamma  ! Le panneau accumule énormément d'énergie et la convertit en rayons gamma. Un coup vous filera un bon gros mal de tête avec un coma à la clé !  \n")
                sleep(4)
                Inventaire["Armes"].append(Mitaines_gamma)
                print("Le nouvel objet a été ajouté à votre inventaire. \n")
            elif objet2 == "le chalumeau":
                sleep(2)
                print("Ce sont des gants de combustion ! Le système du chalumeau permet de tirer des boules de feu sur vos ennemis. Et en prime vos mains seront gardées bien au chaud !  \n")
                sleep(4)
                Inventaire["Armes"].append(Gants_combustion)
                print("Le nouvel objet a été ajouté à votre inventaire. \n")
        print(Robot.get_nomPersonnage(),": Oh... voilà qui va te faciliter la tâche ! \n")
        
    print("Vous continuez d'avancer dans l'", Armurerie.get_nomSalle(),". \n")
    sleep(3)
    print("Vous apercevez un",Alien_blessé.get_nomPersonnage(),". Il est blessé à plusieurs endroits. \n")
    sleep(3)
    print(Robot.get_nomPersonnage(),": Tiens, il est lent et a l'air blessé. Quelqu'un à déjà du l'affronter, on devrait arriver à le semer facilement. \n")
    sleep(4)
    print("Vous apercevez un coffre derrière l'",Alien_blessé.get_nomPersonnage(),". Il est ouvert mais n'est pas vide. Pour y accéder il vous faudra affronter l'",Alien_blessé.get_nomPersonnage(),". \n")
    sleep(4)
    question4 = int(input("Que voulez-vous faire ? 1 = L'affronter | 2 = S'échapper \n"))
    sleep(2)
    if question4 == 1:
        print(Robot.get_nomPersonnage,": Sérieusement tu compte te battre ? Très bien c'est comme tu veux... \n")
        combat(Alien_blessé,Hero)
        if Hero.get_viePersonnage() <= 0:
            return 0
        print(Robot.get_nomPersonnage(),": Bon maintenant le coffre ! \n")
        sleep(1)
        print("Vous vous dirigez vers le coffre. Il y a une",Combinaison_Spatial_en_Carbone.get_nomArmure(),". \n")
        sleep(3)
        question5 = input("Voulez vous la prendre ? y/n \n")
        sleep(1)
        if question5 == "y":
            Inventaire["Armures"].append(Combinaison_Spatial_en_Carbone)
            print("Vous rangez l'armure dans l'inventaire \n")
            ouvrir = int(input("Voulez vous ouvrir l'inventaire pour l'équiper ? 1 = oui | 2 = non \n"))
            if ouvrir == 1:
                choix_inventaire(Inventaire, Hero)
                Hero.recap()
        else:
            print("Vous ne prenez pas l'armure")
    else:
        pass
    sleep(2)
    print("Vous vous dirigez vers la sortie et quittez l'",Armurerie.get_nomSalle(),". \n")
    VarHero(Hero)
    #Sauve(Hero, Armurerie, Inventaire)

#Random_Salle()
#choixSalles()
Alien_blessé = MonstresNormaux('Alien', 20, 2,0,8)
Soldat = MonstresForts('Oleg', 50, 5, 0, 5, 25)
Alien = MonstresNormaux('Alien',35,2,0,5)
Robot = MonstresNormaux('ROBOT',100,5,0,1)
Hero = hero('Kevin',10,10,10,10,0,0,0)
Armurerie(Hero)

