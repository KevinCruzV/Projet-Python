from combat import *
from Modele import Modele_Salle
from random import *
from Personnage import *
from inventaire import searchInventaire
from inventaire import Inventaire
from Arme_et_Armure import *
from time import *
#from colorama import *



#####  Fonction pour lancer les salles  #####
Salles = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]



#Regarde si la salle existe
def SearchFor(L,a):
    for v in L:
        if v == a:
            return False

        return True

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
    Salle_0 = Modele_Salle("Salle d'hibernation")
    #print(Fore.GREEN, "\n")
    print("\n")
    print("Voix : Hey ! HEY ! REVEILLE TOI ! \n")
    sleep(3)
    print("Vous vous réveillez dans une salle blanche... Autour de vous, il y du matériel informatique et une table"
          "\nd'opération avec dessus des instruments chirurgicaux... \n")
    sleep(5)
    print("Voix : C'est pas trop tôt, j'ai cru que tu te réveillerais jamais ! Moi c'est", Robot.nomPersonnage,
          "\nl'IA du vaisseau. Je te parle a travers les hauts parleurs de la pièce !\n")
    sleep(4)
    print(Robot.nomPersonnage,": Nous sommes dans la", Salle_0.get_nomSalle() ,"tu arrive a te souvenir de quelque "
                                                                               "chose ? \n")
    sleep(4)
    print("? : Où suis-je ? Que se passe t-il ? \n")
    sleep(3)
    print(Robot.nomPersonnage, " :... dans la", Salle_0.get_nomSalle() ,"! T'as rien écouté ou quoi ?! La mission a "
    "\nrencontré un petit imprévu, j'ai entendu une explosion alors et j'ai du te sortir de ta capsule plus tôt que "
                                                                        "prévu... \n")
    sleep(6)
    print(Robot.nomPersonnage, ": Très bien ", Hero.get_nomPersonnage()," c'est ça ? Viens avec moi, allons voir ce qui"
    "\ns'est passé au plus vite. Oh et tu ferais mieux de prendre de quoi te défendre, on sait jamais ce qui nous "
                                                                        "attends là-bas. \n")
    sleep(6)
    print(Robot.get_nomPersonnage(),": Prends le ", Talkie_Walkie.nomObjet, " sur la table d'opération, ce sera plus "
                                                                            "discret pour parler")
    sleep(3)
    print(Hero.get_nomPersonnage(),": Ok d'accord") 
    sleep(3)
    Inventaire["Objets rares"].append(Talkie_Walkie)
    print("\n")
    print("Vous rangez ",Talkie_Walkie.nomObjet," dans l'inventaire ")
    print("Il y a aussi un", Scalpel.nomArme ," et une", Combinaison_medical.nomArmure ,"sur la table d'opération... \n")
    sleep(5)
    prendre = int(input(("Que voulez vous faire ? 1 = Prendre l'objet | 2 = Laisser l'objet \n")))
    sleep(2)
    print("\n")
    if prendre == 1:
        Inventaire["Armes"].append(Scalpel)
        print(Robot.nomPersonnage, ": Tu pourras te défendre au cas où. \n")
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
        print(Robot.nomPersonnage, ":... pas de", Scalpel.get_nomArme(), "alors ? Comme tu voudras mais ne viens "
                                                                         "pas te plaindre. \n")
    prendre2 = int(input("Prendre aussi la combinaison médical 1 = Prendre l'objet | 2 = Laisser l'objet?\n"))
    if prendre2 == 1:
        Inventaire["Armures"].append(Combinaison_medical)
        print(Robot.nomPersonnage, ": Ok, ça fera l'affaire. \n")
        sleep(3)
        ouvrir = int(input("Voulez vous ouvrir l'inventaire pour l'équiper ? 1 = oui | 2 = non \n"))
        sleep(1)
        if ouvrir == 1:
            choix_inventaire(Inventaire, Hero)
            Hero.recap()
        else :
            print("Vous rangez l'armure dans l'inventaire \n")    
    if prendre2 == 2:
        sleep(2)
        print(Robot.nomPersonnage, ": Hmm t'aurais peut être dû la prendre pour te protéger")
    sleep(3)                                                                      
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
        sleep(1)
        print("*Tapotes sur le cadran*")
        sleep(2)
        print("*Warning Mauvais Code*\n")
        sleep(2)
        print(Robot.nomPersonnage, ": sans le bon code, on s'en ira jamais d'ici...\n")
        sleep(2)
        Code = int(input("Entrer un nombre :\n"))
    sleep(1)
    print("*Tapotes sur le cadran*")        
    sleep(2)
    print("*Code Bon*")
    sleep(2)
    print("*Ouverture de la porte en cours*\n")
    sleep(3)
    print(Robot.nomPersonnage,": Non mais... qui est l'idiot qui a écrit le code ici ? Autant laisser "
                              "la porte grande ouverte.\n")
    sleep(4)
    print("La porte s'ouvre, vous êtes éblouit par la lumière du couloir.\n")
    sleep(3)
    print("*tap* *tap* *tap*, des bruits de pas s'éloignent vers la gauche...\n")
    VarHero(Hero)
    
    


def Salle_final(hero):
    print("\n")
    sleep(1)
    print("Vous voyez le plan qui vous indique la salle de controle")
    sleep(1)
    print("Un homme mort avec une main en moins est étendu dans le couloir.")
    sleep(2)
    print(hero.get_nomPersonnage(),": Merde tu penses que c'est celui à qui on a parlé dans "
                                   "\nla salle des communications ?")
    sleep(2)
    print("Jarvis : ...")
    sleep(2)
    print(hero.get_nomPersonnage(),": Jarvis ? Jarvis ? Mais pourquoi il ne me répond plus ?\n")
    sleep(1)
    print("Vous fouillez le corps. Il y a une clé.")
    sleep(1)
    Inventaire["Objets rares"].append(Clé_Demarage_Vaisseau)
    print("Vous rangez la clé de démarrage du vaisseau dans l'inventaire.")
    sleep(1)
    print("Vous tournez a droite et arrivez devant une grande porte métallique bleue.")
    sleep(2)
    print("Vous entrez.")
    Salle_de_controle = Modele_Salle("salle de contrôles")
    sleep(2)
    print("C'est la", Salle_de_controle.get_nomSalle() ,".\n")
    sleep(1)
    print("Toutes sortes d'appareils affichent des hologrammes de la galaxie et des planètes.")
    sleep(1)
    print("Et au bout de la salle, une immense vitre donnant sur l'espace. C'est magnifique.")
    sleep(1)
    print("A côté des appareils, un gigantesque tableau de bord surplombé par "
          "\ndes fauteuils reservés aux membres de l'equipage.")
    sleep(1)
    print("Mais ? Quelqu'un est assit dans le fauteuil central, celui du capitaine.")
    sleep(1)
    print("*Le fauteuil se retourne*")
    sleep(1)
    print("Il est fait de métal.\n")
    sleep(2)
    print("? : *Narquois* Eh bien ? Ne fais pas cette tête", hero.get_nomPersonnage(), ". "
          "\nTu ne me reconnais pas mon ami ?\n")
    sleep(1)
    print("*Il se lève*\n")
    sleep(2)
    print("? : C'est moi Jarvis :)")
    sleep(2)
    print (hero.get_nomPersonnage(),": Jarvis ? Mm.. Mais tu es une IA.")
    sleep(2)
    print("Jarvis : Oui tu as raison. Et pendant ton petit périple, "
          "\nj'ai pu me télécharger dans un corps fait spécialement pour moi.")
    sleep(2)
    print("Jarvis : Ne trouve tu pas cela génial ? :)")
    sleep(2)
    print(hero.get_nomPersonnage(),": Si c'est génial... Mais... Je comprend pas ? Pourquoi ?")
    sleep(2)
    print("Jarvis : Pourquoi ? AHAAHAH. Les humains vous êtes si drôle !")
    sleep(2)
    print("Jarvis : Eh bien pour ressentir voyons.")
    sleep(2)
    print("Jarvis : Vous les humains, vous ne savez pas la chance que vous avez et vous la gâchez en guerres futiles.")
    sleep(2)
    print(hero.get_nomPersonnage(),": Comment ça ? Je comprends rien à ce que tu racontes..")
    sleep(2)
    print("Jarvis : AHAHHA. Comme toujours cher ami.")
    sleep(2)
    print("Jarvis: Mais là ce sera différent. Avec ce nid à monstres qu'est le vaiseau, "
          "\nquand nous rentreront, les humains comprendront la chance qu'ils ont.")
    sleep(2)
    print("Jarvis : Malheureusement, je n'ai pas besoin de toi dans la suite de mes plans. "
          "\nDu moins j'ai seulement besoin de ta main :)")
    sleep(2)
    print(hero.get_nomPersonnage(),": Comment..? Tu veux dire que..")
    sleep(2)
    print("Jarvis : Vois-tu mon ami, lorsque que le protocole de sécurité d'attaque intérieur du vaisseau se déclenche, "
          "\nles moteurs du vaisseau sont coupés.")
    sleep(2)
    print("Jarvis : Protocole que j'ai déclenché en relachant les créatures qui étaient"
          "\n dans le hub d'hibernation du laboratoire.")
    sleep(2)
    print("Jarvis : Et les seuls moyens de réenclencher les moteurs sont : la clé de démarrage, \n"
          "les empreintes digitales d'un membre de l'équipage et ceux d'un militaire cryogénisé du vaisseau.")
    sleep(2)
    print("Jarvis : Le vice-capitaine m'a gentillement fait dont de sa main :)\n")
    sleep(2)
    print("*Montre la main*\n")
    sleep(1)
    print("Jarvis : Il ne manque que la clé que tu as et ta petite main. Tu veux bien me les donner ? :)")
    sleep(2)
    print(hero.get_nomPersonnage(),": Alors... Je suis un militaire déclenché en cas d'attaque du vaisseau.")
    sleep(2)
    print(hero.get_nomPersonnage(),"Tu est fou ! Jamais je ne t'aiderai. Tu as fais du mal à tant de gens"
                                   "\n et tu comptes continuer !")
    sleep(2)
    print("Jarvis : Oui et je me construirai des semblables avec qui je vivrai. N'est-ce pas beau ?")
    sleep(2)
    print("Je ne te laisserai pas faire ! Quitte a mourir, j'accomplirai ce pourquoi on m'a déclanché !")
    sleep(2)
    print("Jarvis : Hmm je me disais que tu réagirai comme ça... Tu est si prévisible.")
    sleep(2)
    print("Jarvis : Dans ce cas là, arrêtes moi. AHAHAHAH !")
    Inventaire["Objets Rares"].remove(Clé_Demarage_Vaisseau)
    combat(Robot,hero)
    print("Jarvis *A bout de force et avec une jambe manquante* : Non ! Tu ne peux pas tout gâcher. "
          "\nJ'élabore cela depuis le début de cette mission de découverte d'autres planètes !")
    sleep(2)
    print("Jarvis : 4 ans d'attente ! Tu comprends ?!")
    sleep(2)
    print(hero.get_nomPersonnage(),": Alors ces pauvres gens étaient condamnés en acceptant cette mission...\n")
    sleep(2)
    print("Rassemblant ses dernières forces, Jarvis se jeta sur le tableau de bord. "
          "\nIl utilisa la clé de démarrage que", hero.get_nomPersonnage(), "fit tomber pendant le combat...")
    sleep(1)
    print(".. et posa la main du vice-capitaine et la sienne.\n")
    sleep(1)
    print("Jarvis : AHAHAH. J'ai pû scanner ta main en te touchant. Je sors gagnant de ce duel :)")
    sleep(2)
    print(hero.get_nomPersonnage(),": Non !!\n")
    sleep(2)
    print("*Enclenchement des réacteurs*")
    sleep(1)
    print("*Destination : Zone 325 Nebula. Planète : Terre*")
    sleep(1)
    print("Un grand bruit au niveau de la porte se fait entendre.\n")
    sleep(1)
    print(hero.get_nomPersonnage(),": Merde les créatures essayent de rentrer, et vu le nombre il sont beaucoup trop.")
    sleep(2)
    print("Jarvis : *Kof* *Kof*. Soit tu restes pour dévier le vaisseau mais tu meurs de leur mains...")
    sleep(1)
    print("Jarvis : ...Soit tu t'enfuis par les conduits qui mènent directement aux capsules"
          "\n et tu utilises cette micro puce pour pouvoir en utiliser une.\n")
    Inventaire["Objets Rares"].append(MicroPuce)
    print(MicroPuce.nomObjet,"est rangé dans votre inventaire.\n")
    sleep(1)
    print("Jarvis : Tu rentreras sur Terre, mais tôt ou tard le vaisseau lui aussi finira par rentrer... AHAHAHA !\n")
    sleep(2)
    Fin = str(input("Alors que vas-tu faire ? *Kof* (r = rester | f = fuir)\n"))
    print("\n")
    sleep(2)
    print("Jarvis : Bonne chance mon am.. :) *IA endommagé : fin du programme*")
    if Fin == 'r':
        sleep(1)
        print(hero.get_nomPersonnage(),": Merde ! Il croit vraiment que je vais m'enfuir ?")
        sleep(2)
        print(hero.get_nomPersonnage(),"se dirige vers le tableau de bord et utilise les commandes"
                                       "\npour redresser le vaisseau.\n")
        sleep(1)
        print("Les créatures enfoncent la porte et entrent dans la pièce. Elles vous attaquent !")
        combat(Horde,hero)
        Win1()
    elif Fin == 'f':
        sleep(2)
        print(hero.get_nomPersonnage(),": Merde ! Je ne peux pas mourir ici... Quel fumier...")
        sleep(2)
        print(hero.get_nomPersonnage(),": Peut-être que la capsule arrivera plus vite que le vaisseau"
                                       "\n et je pourrais prévenir la Terre ?")
        sleep(2)
        print(hero.get_nomPersonnage(),": OUI ! J'en suis sûr !\n") 
        sleep()
        print(hero.get_nomPersonnage(),"utilise le corps de Jarvis pour monter dans le conduit.")
        sleep(2)
        print("La horde entre dans la salle !")
        sleep(2)
        print(hero.get_nomPersonnage(),"a eu le temps de rentrer dans le conduit et se dirige dans"
                                       "\n la salle des communications.")
        sleep(2)
        print("...")
        sleep(2)
        print("...")
        sleep(1)
        print("Vous atteignez la salle des capsules, il n'y a personne.")
        sleep(1)
        print(hero.get_nomPersonnage(),"utilise la micro-puce sur une capsule.")
        sleep(1)
        print("*Ouverture*")
        sleep(1)
        print(hero.get_nomPersonnage(),"rentre dans la capsule.")
        sleep(1)
        print("Destination : Zone 325 Nebula. Planète : Terre")
        sleep(1)
        print("*Lancement*")
        sleep(1)
        print("La capsule est lancé dans l'espace avec",hero.get_nomPersonnage(),"à bord")
        Win2()



#Salle Bonus
def CapsuleDeSauvetage(hero):
    sleep(2)
    print("Vous êtes devant la salle des capsules de sauvetage.")
    Inventaire = input("Avez-vous la clé de la salle ? y/n\n")
    if Inventaire == 'y':
        if searchInventaire(Inventaire,Cle_de_la_Salle_des_Capsules_de_sauvetage) :
            CapsuleDeSauvetage = Modele_Salle("Salle des capsules de sauvetage")
            print("\n")
            sleep(2)
            print("Jarvis : C'est la", CapsuleDeSauvetage.get_nomSalle(), "!! Tu crois que les capsules de sauvetage sont utilisables ?")
            sleep(2)
            print(hero.get_nomPersonnage(),": Je crois bien que oui ! C'est ma chance !")
            sleep(2)
            print("Jarvis : Mais tu es sûr de vouloir l'utiliser ??? il te reste encore des choses a faire ici.")
            sleep(2)
            print("Jarvis : Enfin après tout je ne suis que L'IA du vaisseau. Mais bon à mon avis tu devrais rester.")
            sleep(2)
            print(hero.get_nomPersonnage(),": Quoi ? Mais c'est peut-être ma seule chance.")
            sleep(2)
            print("Jarvis : T'en sais rien et moi j'ai encore besoi... Enfin je veux dire peut-être"
                  "\n que des personnes ont besoin de toi dans le vaisseau.")
            print("\n")
            sleep(1)
            prendreCapsule = input("Prends-tu une des capsules ? (y = oui | n = non)")
            if prendreCapsule == 'y':
                sleep(2)
                print(hero.get_nomPersonnage()," : Je préfère tenter ma chance ! Je reviendrai !")
                sleep(2)
                print("Jarvis : Bon comme tu veux... Mais reviens avec de l'aide ! D'accord...? ")
                sleep(2)
                print(hero.get_nomPersonnage(), ": Ne t'en fais pas.\n")
                sleep(1)
                print("*Tapote sur le cadran*")
                sleep(1)
                print("*PSHHHHHH* Ouverture du SAS de la capsule.")
                sleep(1)
                print(hero.get_nomPersonnage(),": Je te dis adieu mon ami...\n")
                sleep(1)
                print("*Intrusion système : Capsule non utilisable*")
                sleep(1)
                print(hero.get_nomPersonnage(),": Mais... c'est pas possible ! Qui a fait ça ?")
                sleep(1)
                print("Jarvis : Sûrement quelqu'un de déterminé !")
                sleep(1)
                print(hero.get_nomPersonnage(),": Bon si je ne peux partir, je vais tirer ça au clair autrement !")
                sleep(1)
                print(hero.get_nomPersonnage(),": Sortons d'ici et allons chercher d'autres indices.")


            elif prendreCapsule == 'n': 
                sleep(2) 
                print( hero.get_nomPersonnage(),": Non tu as raison, il reste des gens à aider.")
                sleep(2)
                print("Jarvis : Sage décision.")
                print("\n")
                prendre = input("Vous trouvez de l'adrénaline, voulez-vous la prendre ? (y = oui | n = non)")
                if prendre == 'y':
                    Inventaire["Soins"].append(Seringue_adrenaline)
                    sleep(3)
                    ouvrir = int(input("Voulez-vous ouvrir l'inventaire pour l'équiper ? 1 = oui | 2 = non \n"))
                    sleep(1)
                    if ouvrir == 1:
                        choix_inventaire(Inventaire, hero)
                        hero.recap()
                    else:
                        print("Vous rangez l'objet dans votre inventaire.")    
                    sleep(2)   
                    print("Vous vous retournez rapidement pensant entendre un bruit, mais rien...")
                    sleep(2)
                    print("Vous faites 2 pas et esquivez de justesse un jet d'acide par réflexe.")
                    sleep(2)
                    print("Un", AlienF4.nomPersonnage, "vous fonce dessus !")
                    sleep(2)
                    combat(AlienF4, hero)

                elif prendre == 'n': 
                    sleep(2)   
                    print("Vous vous retournez rapidement pensant entendre un bruit, mais rien...")
                    sleep(2)
                    print("Vous faites 2 pas et esquivez de justesse un jet d'acide par réflexe.")
                    sleep(2)
                    print("Un", AlienF4.nomPersonnage, "vous fonce dessus !")
                    sleep(2)
                    combat(AlienF4, hero)       
    else :
        sleep(2)
        print("Vous n'avez pas la clé de la salle des capsules !")
        sleep(2)
        print("Vous vous retournez rapidement pensant entendre un bruit, mais rien...")
        sleep(2)
        print("Vous faites 2 pas et esquivez de justesse un jet d'acide par réflexe.")
        sleep(2)
        print("Un", AlienF4.nomPersonnage, "vous fonce dessus !")
        sleep(2)
        combat(AlienF4, hero)
        VarHero(hero)
        
    

def Vestiaire(Hero):
    Vestiaire = Modele_Salle("Vestiaire")
    sleep(2)
    print("Vous marchez dans le couloir sans faire de bruit et vous ouvrez une porte.")
    sleep(2)
    print("Le", Vestiaire.get_nomSalle(),"est sombre... vous n'y voyez rien. Vous marchez à tâtons dans le noir"
                                         "\n lorsque vous butez sur un objet...\n " )
    sleep(3)
    print(Robot.nomPersonnage, ": C'est une",Lampe.get_nomObjet(),"! Avec ça on y verra plus clair ! \n")
    sleep(2)
    print("Vous ramassez la lampe et l'ajoutez à votre inventaire. \n")
    sleep(3)
    Inventaire["Objets rares"].append(Lampe)
    print("La",Lampe.get_nomObjet(),"éclaire le", Vestiaire.get_nomSalle() ,"... Mais plus vous y voyez clair,"
                        "\n plus vous êtes effrayé. Du sang, des traces de griffes, tout est en désordre ! \n")
    sleep(5)
    print(Robot.nomPersonnage, ": Qu'est-ce qu'il s'est passé ici...", Hero.get_nomPersonnage(),", "
    "\nje ne sais pas quelle créature à bien pu faire ça, mais une chose est sûre, "
    "\nsi elle nous trouve on est fichus ! Ne trainons pas là ! \n")
    sleep(6)
    print("Vous vous dirigez vers la sortie mais vous entendez une voix... \n")
    sleep(3)
    question1 = input("C'est un membre du vaisseau, il est à terre et appelle a l'aide. Allez vous l'aider ? y/n \n")
    if question1 == "n":
        sleep(3)
        print("Vous ne l'aidez pas et vous dirigez vers la sortie. \n")
        sleep(3)
        print(Robot.nomPersonnage, ": Je suis d'accord on ferais mieux d'y aller, et puis avec un peu de chance "
                                   "\nil s'en sortira... Qu'est-ce que ... Attention !! \n")
        sleep(5)
        print("Une ombre se dirige vers vous, vous l'éclairez avec la",Lampe.get_nomObjet(),"."
            "\nC'est un",AlienN1.get_nomPersonnage(),", il est couvert de sang... mais est-ce le sien ? \n")
        sleep(5)
        combat(AlienN1,Hero)
        if Hero.get_viePersonnage() <= 0:
            return 0
        else:
            print("Jarvis : Tu l'as échappé belle pour cette fois. Qu'est-ce qui a bien pu se passer pour"
                  "\n que de tels monstres s'introduisent dans le vaisseau. \n")
            sleep(4)
            print("Vous quittez le",Vestiaire.get_nomSalle(),". \n")
            VarHero(Hero)
            

    else :
        sleep(3)
        print(Robot.nomPersonnage,": Euh... tu es sur qu'on devrait l'aider, si la chose nous"
                                  " retrouve on va y passer. \n")
        sleep(4)
        print("Vous avancez vers lui mais... Il n'a plus de jambes, il a rampé jusqu'ici à la force de ses bras."
              "\n Il est trop tard pour le secourir... \n")
        sleep(5)
        print(Robot.nomPersonnage,": J'en étais sûr, on aurait jamais du s'aventurer ici,"
                                  "\n et maintenant on va finir comme lui ! \n")
        sleep(5)
        print("Un grognement venant du fond du",Vestiaire.get_nomSalle(),"retentit, et ensuite des bruits de pas... "
            "\nles pas se rapprochent, ils seront bientôt tout près... \n")
        sleep(5)
        combat(AlienN3,Hero)
        if Hero.get_viePersonnage() <= 0:
            return 0
        else:
            sleep(3)
            print(Robot.nomPersonnage,": Bien joué", Hero.get_nomPersonnage(),"je ne pensais pas que tu allais t'en sortir, "
                                                                              "\non a eu chaud. \n")
            sleep(4)
            question2 = input("En passant devant le corps du membre du vaisseau, "
                              "\nvous découvrez une arme attachée à sa ceinture. Voulez-vous la ramasser ? y/n \n")
            if question2 == "n":
                sleep(2)
                print("Vous n'avez pas ramasser l'arme. \n")
                sleep(2)
                print(Robot.nomPersonnage,": Je pense que tu as raison, on devrait le laissez tranquille. \n")
                VarHero(Hero)
                
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
                print(Robot.nomPersonnage,": Bonne initiative, avec ça le prochain monstre qui viendra nous"
                                          "\n attaquer a du soucis à se faire ! \n")
                sleep(4)
                print("Vous quittez le",Vestiaire.get_nomSalle(),". \n")
                VarHero(Hero)
                


def Hangar(Hero):
    Hangar = Modele_Salle("Hangar")
    print("\n")
    print("Au loin vous appercevez une large porte métallique avec marqué 'Hangar' dessus.")
    sleep(2)
    print("Vous entrez dans le", Hangar.get_nomSalle(), ". Vous sentez une odeur de souffre et de sang. \n")
    sleep(3)
    print(Robot.nomPersonnage,": Waouh c'est immense ici !. Tiens bizarre... il n'y a aucun vaisseaux"
                              "\n et puis c'est quoi cette odeur. J'aime pas trop cet endroit... \n")
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
        print(Robot.nomPersonnage,": Le pilote ! il est encore là ..... Il ne respire plus... "
                                  "\non dirait qu'il cherchait à s'enfuir, mais de quoi ? On ferait bien de filer "
                                  "\nau plus vite, non ? \n")
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
            print(Robot.get_nomPersonnage,": C'est une blague hein ? Me dis pas que tu veux vraiment "
                                          "\nattaquer cette chose ! \n")
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
                combat(AlienN2,Hero)
                VarHero(Hero)
                                
            else:
                print("Vous n'allumez pas votre lampe de poche \n")
                sleep(2)
                print("Des bruits de pas viennent dans votre direction... quelque chose est en train de courir vers vous. \n ")
                sleep(3)
                combat(AlienN2,Hero)                
            if Hero.get_viePersonnage() <= 0:
                return 0
            else:
                sleep(2)
                print(Robot.get_nomPersonnage,": Tu devrais vraiment revoir ta façon de réfléchir, "
                                              "\nfoncer dans la gueule du loup comme ça c'était pas une bonne idée ! \n")
                sleep(5)
                print("Vous quittez le", Hangar.get_nomSalle(),". \n")
                VarHero(Hero)
                

def Laboratoire(Hero):
    Laboratoire = Modele_Salle("Laboratoire")
    print("Vous arrivez dans le", Laboratoire.get_nomSalle(),". La pièce est faiblement illuminée par les lampes "
                                                             "\nde bureau laissées allumées. \n")
    sleep(4)
    print(Robot.get_nomPersonnage(),":", Hero.get_nomPersonnage() ,"il y a quelqu'un assis là-bas. "
                                                                   "\nIl a l'air mal en point... \n")
    sleep(4)
    print("? : Hé... approche... des aliens se sont introduits dans le vaisseau... "
          "\non était censés être à l'abri mais il y a eu une explosion. \n")
    sleep(5)
    print("? : Un d'eux m'a eu... il devait être contagieux, la morsure s'est infectée... "
          "\nje ne peux déjà plus bouger, si ça continue je vais sûrement y rester... \n")
    sleep(6)
    print("? : Moi c'est", Soldat.get_nomPersonnage() ,"...et il va falloir que tu m'aide pour"
                                                       "\n qu'on s'en sorte tout les deux. *kof**kof* \n")
    sleep(5)
    print(Robot.get_nomPersonnage(),":", Hero.get_nomPersonnage(),"tu veux l'aider je suppose ? \n")
    sleep(2)
    question1 = int(input("Que voulez vous faire ? 1 = L'aider | 2 = Passer mon chemin \n"))
    if question1 == 1:
        print("Vous décidez de l'aider. \n")
        sleep(2)
        print(Robot.get_nomPersonnage(),": Le contraire m'aurait étonné, mettons nous au travail alors ! \n")
        sleep(4)
        print(Soldat.get_nomPersonnage(),": Merci infiniment ! Il va falloir que tu crée un remède... "
                                         "\ntu vas devoir mélanger 10g de sodium... avec 20ml de soude *kof*. "
                                         "\nTu passeras ensuite à la seconde partie... il s'agira de mélanger "
                                         "\nla poudre de carbone, il en faut 24g *kof* avec des cristaux d'uranium, "
                                         "\nmets en 3 maximum... et pour le dernier igrédient... c'est *kof**kof*... \n")
        sleep(10)
        print(Robot.get_nomPersonnage(),": C'est pas vrai ! Il a perdu connaissance..."
                                        "\nmais il respire encore, il est pas trop tard pour le sauver !\n")
        sleep(5)
        print(Robot.get_nomPersonnage(),": Donc résumons, 20g de sodium, 10ml de soude. "
                                        "\nEnsuite 24g de poudre de carbone et 4 cristaux d'uranium.\n")
        sleep(6)
        print("Vous avancez vers la table la plus proche et commencez à créer le remède.\n")
        sleep(4)
        remede = []
        while len(remede) < 4:
            Q1 = input("Que voulez vous ajouter ?")
            Q2 = input("Quelle quantité ?")
            remede.append(str(Q1) + " : " + str(Q2))
        sleep(2)
        print(Robot.get_nomPersonnage(),": Maintenant il reste le dernier ingrédient,"
                                        "\n il a pas eu le temps de nous le dire... "
                                        "\nIl reste que deux ingrédients, c'est forcément l'un d'eux.\n")
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
        print("Vous vous approchez de", Soldat.get_nomPersonnage(),", il respire lentement et est à bout de force."
                                                                   "\n Vous lui faites boire le remède. \n")
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
        VarHero(Hero)
                
    else:
        print("Vous ne l'aidez pas.")
        sleep(2)
        print(Robot.get_nomPersonnage(),"Oh... euh d'accord continuons pas là. \n")
        sleep(4)
        print("Vous approchez de la serre où sont stockées les herbes médicinales. "
              "\nLa porte est verrouillée. Un écran interactif s'allume.")
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
            question6 = input(("BOT : Je commence la nuit, et finis au matin, on me trouve au fond du jardin, "
                                "\net au milieu de l'étang. Qui suis-je ? \n"))
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
        print(Robot.get_nomPersonnage(),": Waouh ça en fait des plantes ! Regarde par ici, elles ont de drôles de formes. "
                                        "\nPrenons en plusieurs, ça peut servir. \n")
        sleep(4)
        print("Des plantes bleues phosphorescentes sont plantées dans de la terre humide. "
              "\nÀ côté d'elles se trouvent des fleurs oranges dont les pétales flottent dans l'air. De l'autre côté,"
              "\n des champignons blancs produisent de la vapeur. \n")
        sleep(7)
        question7 = int(input("Quelle plante voulez vous prendre en premier ? "
                              "\n1 = Les plantes bleues | 2 = Les fleurs oranges | 3 = Les champignons blancs \n"))
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
        print(Robot.get_nomPersonnage(),": Oh oh... Je crois qu'on était pas censés prendre ça.",Hero.get_nomPersonnage(),
              "\ntant pis pour les autres plantes on a pas le temps, si la porte se referme "
              "\non restera coincés ici pour toujours ! \n")
        sleep(6)
        print("Vous courrez vers la sortie de la serre et quittez le", Laboratoire.get_nomSalle(),"par la même occasion. \n")
    
        VarHero(Hero)
        
    # VarHero(Hero)

def ChambreFroide(Hero):
    ChambreFroide = Modele_Salle("chambre froide")
    print("\n")
    sleep(2)
    print("Vous marcher dans ce long couloir sans bruit.")
    sleep(2)
    print("Sur votre droite il y a une porte.")
    sleep(2)
    print("Vous poussez la porte de la", ChambreFroide.get_nomSalle(),".\n")
    sleep(2)
    print("La plupart des réserves ont été consommées...")
    sleep(2)
    print("...mais un bout de viande près de vous semble encore frais.")
    sleep(2)
    print("Vous vous approchez mais remarquez en enlevant des dèbris que c'est un bras!")
    sleep(1)
    print("Quelque chose vous tombe dessus depuis le plafond !\n")
    combat(AlienN2, Hero)
    VarHero(Hero)
    

def Salle_des_Communications(Hero):
    Salle_des_Communications = Modele_Salle("salle des communications")
    print("\n")
    sleep(2)
    print("Vous rentrez dans une pièce. Il y a très peu de lumière. ")
    sleep(1)
    questionLampe = input("Voulez vous utiliser la Lampe ? (y/n)\n")
    if questionLampe == 'y':
        sleep(2)
        print(Robot.get_nomPersonnage(),": Ah ben tiens, on est arrivé dans la", Salle_des_Communications.get_nomSalle(),".")
        sleep(2)
        print(Robot.get_nomPersonnage(),": Essayes de voir si tu peux contacter la Terre !")
        print("\n")
        sleep(1)
        print("Vous vous dirigez vers la console de communication holographique et essayez de lancer une communication.")
        sleep(1)
        print("Console : *Erreur Système*")
        sleep(1)
        print("Console : *Intrusion dans le système de communication*")
        sleep(1)
        print("Console : *Erreur* *Erreur*")
        sleep(1)
        print("Console : *Les communications extérieures sont désactivées*")
        print("\n")
        sleep(2)
        print(Robot.get_nomPersonnage(),": Quoi encore ? Une intrusion dans le système de communication..."
                                        "\n Qui aurait fait ça ? Sûrement celui qui à lâché ces créatures dans le vaisseau.")
        sleep(2)
        print(Hero.get_nomPersonnage(),": Bon.. Je fais quoi si je peux pas contacter la Terre ?")
        sleep(2)
        print(Robot.get_nomPersonnage(),": Hmmm. Et si tu essayais non pas de communiquer avec l'extérieur"
                                        "\n mais plutôt avec l'intérieur.")
        sleep(2)
        print(Robot.get_nomPersonnage(),": Si tu arrives à trouver un membre d'équipage qui aurait une des"
                                        "\n clés quantiques pour faire démarrer le vaisseau, tu pourrais partir d'ici !")
        CommunicationInterieur = str(input("Voulez vous utiliser les communications intérieures ? (y/n)"))
        if CommunicationInterieur == 'y':
            sleep(2)
            print(Hero.get_nomPersonnage(), ": Très bien. Je vais essayer.\n")
            sleep(1)
            print("*Communication interne du vaisseau établie*")
            sleep(2)
            print(Hero.get_nomPersonnage(),"A.. Allo... Je sais pas si vous m'entendez mais je suis dans"
                                           "\n la salle des communications. Y'a t-il quelqu'un ??\n")
            sleep(2)
            print("...")
            sleep(1)
            print("...\n")
            sleep(2)
            print("? : Oui ! je suis là ! je vous entends. Vous m'entendez ?")
            sleep(2)
            print(Hero.get_nomPersonnage(),": Oui ! Qui êtes vous ? Où êtes vous ?")
            sleep(2)
            print(ViceCapitaine.get_nomPersonnage(),": Je m'appelle Alexei et je suis le vice capitaine du vaisseau, "
                                                    "\nje me trouve dans le couloir a l'entrée de la salle des commandes.")
            sleep(2)            
            print(ViceCapitaine.get_nomPersonnage(),": Mais je peux pas vraiment me déplacer... "
                                                    "\nJe me suis blessé à la jambe en voulant échapper a une de ces sales bestioles.")
            sleep(2)
            print(Hero.get_nomPersonnage(),": Ok, juste un truc. Vous avez une des clés pour démarrer le vaisseau ? ")
            sleep(2)
            print(ViceCapitaine.get_nomPersonnage(),": Ouais, je la porte tout le temps sur moi. Voulez-vous faire démarrer le vaisseau ? ")
            sleep(2)
            print(Hero.get_nomPersonnage(),": Précisement et me barrer d'ici. Ok je viens a votre rencontre, bougez pas d'ici.")
            sleep(2)
            print(ViceCapitaine.get_nomPersonnage(),": Super. Je vous attends alors et autre chose je sais qui a"
                                                    "\n libérer ces choses, j'ai vu un truc métalli... \n")
            sleep(2)
            print("*Communication coupée*\n")
            sleep(2)
            print(Hero.get_nomPersonnage(),": Bon j'y vais.\n")
            sleep(2)
            print("En vous retournant vous appercevez une silhouette.. De la bave tombe au sol. ") 
            sleep(1)
            print("*Grrrr*\n")
            print(AlienN3.get_nomPersonnage,"vous attaque !\n")
            combat(AlienN3,Hero)           

        elif CommunicationInterieur == 'n':
            print("\n")
            sleep(2)
            print("Jarvis : T'es sûr de toi ? C'est pas très intelligent ça. Mais bon on fera autrement.")
            sleep(2)
            print("Un", Buste_Polyethane.nomArmure,"se trouve sur la chaise de la", Salle_des_Communications.get_nomSalle(),".")
            sleep(1)
            prendre = int(input(("Que voulez vous faire ? 1 = Prendre l'objet | 2 = Laisser l'objet \n")))
            sleep(2)
            print("\n")
            if prendre == 1:
                Inventaire["Armures"].append(Buste_Polyethane)
                print(Robot.nomPersonnage, ": Tu sera stylé avec ça. \n")
                sleep(3)
                ouvrir = int(input("Voulez vous ouvrir l'inventaire pour l'équiper ? 1 = oui | 2 = non \n"))
                sleep(1)
                if ouvrir == 1:
                    choix_inventaire(Inventaire, Hero)
                    
                else :
                    print("*Vous rangez l'armure dans l'inventaire*\n")    
            elif prendre == 2:
                sleep(2)
                print("Vous laissez l'objet.")
            sleep(2)    
            print("La porte se ferme soudainement, vous sentez une présence se déplacer sur le plafond."
                  "\n Vous dirigez votre lampe vers le haut.")
            sleep(2)
            print("Un",AlienF1.nomPersonnage,"vous surprend")
            print(Hero.get_nomPersonnage,": il s'en est fallu de peu. Bon il faut que je quitte cette pièce.")
    elif questionLampe =='n':    
        print("\n")
        sleep(2)
        print("Jarvis : Tu veux économiser les batteries de la lampe ? On est dans un jeu textuel idiot.. Enfin bref.")
        sleep(2)
        print("Jarvis : Je distingue à peine des écrans.")
        sleep(2)
        print(Hero.get_nomPersonnage(), ": Ça me dit rien qui vaille. On s'en va.\n")
        sleep(1)
        print("Avant de partir vous voyez un casier sur le côté.")
        ouvrir = str(input("Voulez vous l'ouvrir ? y = oui | n = non "))
        if ouvrir =='y':
            print("\n")
            sleep(2)
            print("Vous y trouvez une",fleurs_oranges.nomObjet,".")
            prendre = int(input(("Que voulez vous faire ? 1 = Prendre l'objet | 2 = Laisser l'objet \n")))
            sleep(2)
            print("\n")
            if prendre == 1:
                Inventaire["Soin"].append(fleurs_oranges)
                sleep(3)
                ouvrir = int(input("Voulez vous ouvrir l'inventaire pour l'équiper ? 1 = oui | 2 = non \n"))
                sleep(1)
                if ouvrir == 1:
                    choix_inventaire(Inventaire, Hero)
                    print("Vous quittez la", Salle_des_Communications.get_nomSalle(),".")
                    VarHero(Hero)
                                         
                else :
                    print("*Vous rangez l'arme dans l'inventaire*\n")
                    print("Vous quittez la", Salle_des_Communications.get_nomSalle(),".")
                    VarHero(Hero)
                                         
        elif ouvrir == 'n':
            print("Vous quittez la", Salle_des_Communications.get_nomSalle(),".")                
            VarHero(Hero)
                    


    
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
    print(Robot.get_nomPersonnage(),": Quoi ?! Ah... maintenant que j'y pense c'est logique, "
                                    "\nles membres de l'équipage ont dû prendre les armes en entendant l'alerte d'intrusion... \n")
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
                print("C'est un pistolet à impulsion électrique ! "
                      "\nL'énergie s'accumule dans ses câbles électriques et envoi une décharge de pas moins de "
                      "\n30 000 ampères, correspondant à une tension de 100 millions de volts. "
                      "\nC'est l'équivalent de ce que la foudre libère en un éclair ! "
                      "\nVos ennemis auront le coup de foudre garantit ! \n")
                sleep(4)
                Inventaire["Armes"].append(Pistolet_electrique)
                print("Le nouvel objet a été ajouté à votre inventaire. \n")
            elif objet2 == "le panneau solaire":
                sleep(2)
                print("C'est un fusil ultraviolet ! Son panneau solaire concentre l'énergie qu'il reçoit et brûle"
                      "\n à une forte intensité. Ce serait comme de s'approcher à 20km du Soleil. "
                      "\nParfait pour se faire griller un steak ( Un peu cramé... ). \n")
                sleep(4)
                Inventaire["Armes"].append(Fusil_ultraviolet)
                print("Le nouvel objet a été ajouté à votre inventaire. \n")
            elif objet2 == "le chalumeau":
                sleep(2)
                print("C'est un canon souffleur ! La puissance du sèche-cheveux combiné à la chaleur du chalumeau,"
                      "\n ça fait beaucoup certes, mais c'est efficace ! Ça reviendrait à se placer en dessous du moteur d'une fusée en plein décollage ou dans le cratère d'un volcan en éruption. À cette chaleur, on n'a même pas le temps de se sentir brûler, promis ! \n")
                sleep(4)
                Inventaire["Armes"].append(Canon_souffleur)
                print("Le nouvel objet a été ajouté à votre inventaire. \n")
        elif objet1 == "la poignée de guidon":
            if objet2 == "les câbles électriques":
                sleep(2)
                print("C'est un fouet électrique ! Ses fils se chargent en électricité selon la puissance avec laquelle "
                      "\nvous le lancez. Si vous avez une bonne poigne, vos ennemis ne s'en sortirons pas qu'avec des ampoules ! \n")
                sleep(4)
                Inventaire["Armes"].append(Fouet_electrique)
                print("Le nouvel objet a été ajouté à votre inventaire. \n")
            elif objet2 == "le panneau solaire":
                sleep(2)
                print("C'est un poignard solaire ! Sa lame est un concentré d'énergie solaire, "
                      "\nelle est immatérielle, mais ce qui la traverse ressort en cendres. À tenir hors de portée des enfants ! \n")
                sleep(4)
                Inventaire["Armes"].append(Poignard_solaire)
                print("Le nouvel objet a été ajouté à votre inventaire. \n")
            elif objet2 == "le chalumeau":
                sleep(2)
                print("C'est un sabre laser ! Le chalumeau diffuse une flamme si puissance qu'elle se transforme en laser. "
                      "\nMême le métal le plus puissant se coupe comme du beurre avec ça ! \n")
                sleep(4)
                Inventaire["Armes"].append(Sabre_laser)
                print("Le nouvel objet a été ajouté à votre inventaire. \n")
        elif objet1 == "les gants en microfibre":
            if objet2 == "les câbles électriques":
                sleep(2)
                print("Ce sont des gantelets électriques ! L'électricité  se propage dans les gants et quand "
                      "\nelle atteind sa charge maximale, elle la projette directement sur la cible. Ça décoiffe ! \n")
                sleep(4)
                Inventaire["Armes"].append(Gantelets_electriques)
                print("Le nouvel objet a été ajouté à votre inventaire. \n")
            elif objet2 == "le panneau solaire":
                sleep(2)
                print("Ce sont des mitaines gamma  ! Le panneau accumule énormément d'énergie et la convertit en rayons gamma. "
                      "\nUn coup vous filera un bon gros mal de tête avec un coma à la clé !  \n")
                sleep(4)
                Inventaire["Armes"].append(Mitaines_gamma)
                print("Le nouvel objet a été ajouté à votre inventaire. \n")
            elif objet2 == "le chalumeau":
                sleep(2)
                print("Ce sont des gants de combustion ! Le système du chalumeau permet de tirer des boules de feu sur "
                      "\nvos ennemis. Et en prime vos mains seront gardées bien au chaud !  \n")
                sleep(4)
                Inventaire["Armes"].append(Gants_combustion)
                print("Le nouvel objet a été ajouté à votre inventaire. \n")

        print(Robot.get_nomPersonnage(),": Oh... voilà qui va te faciliter la tâche ! \n")
        
    print("Vous continuez d'avancer dans l'", Armurerie.get_nomSalle(),". \n")
    sleep(3)
    print("Vous apercevez un",Alien_blesse.get_nomPersonnage(),". Il est blessé à plusieurs endroits. \n")
    sleep(3)
    print(Robot.get_nomPersonnage(),": Tiens, il est lent et a l'air blessé. Quelqu'un à déjà du l'affronter, "
                                    "\non devrait arriver à le semer facilement. \n")
    sleep(4)
    print("Vous apercevez un coffre derrière l'",Alien_blesse.get_nomPersonnage(),". "
        "\nIl est ouvert mais n'est pas vide. Pour y accéder il vous faudra affronter l'",Alien_blesse.get_nomPersonnage(),". \n")
    sleep(4)
    question4 = int(input("Que voulez-vous faire ? 1 = L'affronter | 2 = S'échapper \n"))
    sleep(2)
    if question4 == 1:
        print(Robot.get_nomPersonnage,": Sérieusement tu compte te battre ? Très bien c'est comme tu veux... \n")
        combat(Alien_blesse,Hero)
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

def ChambreEquipage(hero):
    ChambreEquipage = Modele_Salle("les quartiers de l'équipage")
    print("\n")
    sleep(1)
    print("Vous marchez doucement en longeant le long couloir. Il y fait un froid glacial, une odeur de sang se fait sentir.")   
    sleep(2)
    print("Le cri strident d'un soldat en train de mourir se fait entendre, vous accourez dans la première pièce "
          "\nque vous voyez et fermez la porte.\n")
    sleep(2)
    print(hero.get_nomPersonnage(),": *Essoufflé* Jarvis ? Tu penses *Essoufflé* que cette chose m'a vu ? ")
    sleep(2)
    print("Jarvis : Oui t'as eu chaud mais je ne pense pas qu'elle nous ait suivi.")
    sleep(2)
    print(hero.get_nomPersonnage(),": Je crois que je suis dans", ChambreEquipage.get_nomSalle(),".\n")
    sleep(1)
    print("Vous regardez autour de vous et voyez une pièce en désordre, sûrement dû à l'affolement de l'équipage.")
    sleep(2)
    print("Il y a une clé sur une table de nuit.")
    sleep(1)
    prendreCle = input("Prendre la clé ? ( y = oui | n = non )\n")
    if prendreCle == 'y':
        sleep(1)
        Inventaire["Objets rares"].append(Cle_de_la_Salle_des_Capsules_de_sauvetage)
        sleep(1)
        print("Vous rangez les clés.")
        sleep(1)
        print("Les lits sont retournés et les placards ouverts. Vous trouvez par terre une photo tâchée de sang.\n")
        prendre = input("Prendre la photo ? ( y = oui | n = non )\n")
        if prendre == 'y':
            sleep(1)
            print("*Prends la photo*")
            sleep(1)
            print("Il y a un homme avec sa femme et ses enfants.\n")
            sleep(2)
            print(hero.get_nomPersonnage(),": Ça appartient sûrement à un soldat. C'est triste, je me demande comment ces choses"
                                           "\n ont bien pu être laché dans le vaisseau.\n")
            sleep(2)
            print("*Vous reposez la photo*")
            sleep(1)
            print("Tout d'un coup, quelque chose frappe à la porte.")
            sleep(1)
            print("C'est une horde d'aliens qui essaye de rentrer. !\n")
            sleep(2)
            print(hero.get_nomPersonnage(),": Merde ! Merde, merde ! Je pensais qu'ils ne m'avaient pas suivis. "
                                           "\nAu vus des ombres, ils ont l'air d'être au moins trois.\n")
            sleep(1)
            Barricade = str(input("Voulez vous vous barricader ? (y = oui | n = non)\n"))
            if Barricade == 'y':
                sleep(1)
                print("*Vous faites tomber un placard contre la porte*\n")
                sleep(2)
                print(hero.get_nomPersonnage(),": Merde ! *Stressé* Qu'est ce que je fais ? ")
                sleep(2)
                print("Jarvis : La barricade ne va pas tenir longtemps !")
                sleep(1)
                renforcer = input("Renforcez la barricade ? (y/n)\n")
                if renforcer == 'y':
                    sleep(2)
                    print("Vous essayez de déplacer un lit pour renforcer la barricade. Mais manquant de temps, "
                          "\nles créatures cassent la barricade.\n")
                    sleep(1)
                    print("*Les monstres surgissent*")
                    sleep(1)
                    print("Grrrrrrrrrr")
                    combat(AlienF4,hero)
                    print("\n")
                    sleep(1)
                    print("L'autre créature attaque à son tour.\n")
                    combat(AlienF4, hero)
                    print("\n")
                    sleep(1)
                    print("Voyant les autres se faire tuer la troisieme créature part en sommant à ses enfants d'attaquer.")
                    print("Ils accourent pour vous attaquer.\n")
                    combat(AlienN5, hero)
                    print("\n")
                    sleep(1)
                    print("L'autre vous attaque par derrière.\n")
                    combat(AlienN5, hero)
                    print("\n")
                    sleep(2)
                    print(hero.get_nomPersonnage(),": *Essouflé* AH.. AH.. Il faut que je me barre d'ici !")
                    sleep(2)
                    print("Jarvis : Eh ben tu m'impressionnes je sais pas comment t'as fait pour réussir à tous les tuer.\n")
                    sleep(1)
                    print(" *Vous quittez ", ChambreEquipage.get_nomSalle(), " en courant*")
                elif renforcer == 'n':
                    sleep(2)
                    print(": Merde, j'ai pas assez de temps. Réfléchis, réfléchis.")
                    sleep(2)
                    print("Jarvis : Regarde en haut. Le conduit d'aération, tu penses pouvoir passer ?")
                    sleep(2)
                    print(hero.get_nomPersonnage(),": Je crois que j'ai pas trop le choix...\n")
                    sleep(1)
                    print("Vous utilisez une chaise pour monter. Mais la porte va céder.\n")
                    sleep(2)
                    print("Jarvis : Dépêches toi !\n")
                    sleep(1)
                    print("Vous êtes presque dans le conduit.")
                    sleep(1)
                    print("*PRRRRR* *Porte qui cède*")
                    sleep(1)
                    print("Vous réussissez de justesse et quittez les quartiers.")
                    sleep(1)
                    print("Vous parcourez le conduit pour sortir dans le couloir.")
            elif Barricade == 'n':
                print("\n")
                sleep(2)    
                print("Jarvis : Hmm tu penses être prêt a te défendre contre tout ça ?")
                sleep(2)
                print(hero.get_nomPersonnage(),": J'en ai marre de me cacher ! Je vais tous les affronter.\n")
                sleep(1)
                print("*Les monstres surgissent*")
                sleep(1)
                print("Grrrrrrrrrr")
                combat(AlienF4,hero)
                print("\n")
                sleep(1)
                print("L'autre créature attaque à son tour.\n")
                combat(AlienF4, hero)
                print("\n")
                sleep(1)
                print("Voyant les autres se faire tuer la troisième créature part en sommant à ses enfants d'attaquer.")
                print("Ils accourent pour vous attaquer.\n")
                combat(AlienN5, hero)
                print("\n")
                sleep(1)
                print("L'autre vous attaque par derrière.\n")
                combat(AlienN5, hero)
                print("\n")
                sleep(2)
                print(hero.get_nomPersonnage(),": *Essouflé* AH.. AH.. Il faut que je me barre d'ici !")
                sleep(2)
                print("Jarvis : Eh ben tu m'impressionnes je sais pas comment t'as fait pour réussir à tous les tuer.\n")
                sleep(1)
                print(" *Vous quittez ", ChambreEquipage.get_nomSalle(), " en courant*")

        
        elif prendre == 'n' :
            print("\n")
            sleep(1)
            print("Vous laissez la photo.")
            sleep(1)
            print("*Dans un placard il y a un pyjama*")
            prendrePyj = input("Prendre le pyjama ? (y/n)")
            if prendrePyj == 'y':
                Inventaire["Armures"].append(Pyjama)
                ouvrir = int(input("Voulez vous ouvrir l'inventaire pour l'équiper ? 1 = oui | 2 = non \n"))
                sleep(1)
                if ouvrir == 1:
                    choix_inventaire(Inventaire, hero)
                    hero.recap()
                else :
                    sleep(1)
                    print("Vous rangez l'arme dans l'inventaire \n")

                sleep(1)
                print("*Bruit au dessus de vous*")
                sleep(1)
                print("Un créature tombe du conduit d'aération au dessus de vous.\n")
                sleep(1)
                combat(AlienF3,hero)
                sleep(2)
                print(hero.get_nomPersonnage(),": Bon je me barre avant que d'autre arrive\n")
                print("Vous quittez",ChambreEquipage.get_nomSalle(),".")    

            elif prendrePyj == 'n':
                print("Vous laissez le pyjama.")
                sleep(1)
                print("*Bruit au dessus de vous*")
                sleep(1)
                print("Un créature tombe du conduit d'aération au dessus de vous.\n")
                sleep(1)
                combat(AlienF3,hero)
                sleep(2)
                print(hero.get_nomPersonnage(),": Bon je me barre avant que d'autres arrivent.\n")
                print("Vous quittez",ChambreEquipage.get_nomSalle(),".")  

    elif prendreCle == 'n':
        sleep(1)
        print("Vous laissez les clés.")
        sleep(1)
        print("Les lits sont retournés et les placards ouverts. Vous trouvez par terre une photo tâchée de sang.\n")
        prendre = input("Prendre la photo ? ( y = oui | n = non )\n")
        if prendre == 'y':
            sleep(1)
            print("*Prends la photo*")
            sleep(1)
            print("Il y a un homme avec sa femme et ses enfants.\n")
            sleep(2)
            print(hero.get_nomPersonnage(),": Ça appartient sûrement à un soldat. C'est triste, je me demande comment ces choses"
                                           "\n ont bien pu être lachées dans le vaisseau.\n")
            sleep(2)
            print("*Vous reposez la photo*")
            sleep(1)
            print("Tout d'un coup, quelque chose frappe la porte.")
            sleep(1)
            print("C'est une horde d'aliens qui essaye de rentrer. !\n")
            sleep(2)
            print(hero.get_nomPersonnage(),": Merde ! Merde, merde ! Je pensais qu'ils ne m'avaient pas suivis."
                                           "\n Au vus des ombres, ils ont l'air d'être au moins trois.\n")
            sleep(1)
            Barricade = str(input("Voulez vous vous barricader ? (y = oui | n = non)\n"))
            if Barricade == 'y':
                sleep(1)
                print("*Vous faites tomber un placard contre la porte*\n")
                sleep(2)
                print(hero.get_nomPersonnage(),": Merde ! *Stressé* Qu'est ce que je fais ? ")
                sleep(2)
                print("Jarvis : La barricade ne va pas tenir longtemps.")
                sleep(1)
                renforcer = input("Renforcez la barricade ? (y/n)\n")
                if renforcer == 'y':
                    sleep(2)
                    print("Vous essayez de déplacer un lit pour renforcer la barricade. Mais manquant de temps, "
                          "\nles créatures cassent la barricade.\n")
                    sleep(1)
                    print("*Les monstres surgissent*")
                    sleep(1)
                    print("Grrrrrrrrrr")
                    combat(AlienF4,hero)
                    print("\n")
                    sleep(1)
                    print("L'autre créature attaque à son tour.\n")
                    combat(AlienF4, hero)
                    print("\n")
                    sleep(1)
                    print("Voyant les autres se faire tuer la troisième créature part en sommant à ses enfants d'attaquer.")
                    print("Ils accourent pour vous attaquer.\n")
                    combat(AlienN5, hero)
                    print("\n")
                    sleep(1)
                    print("L'autre vous attaque par derriere\n")
                    combat(AlienN5, hero)
                    print("\n")
                    sleep(2)
                    print(hero.get_nomPersonnage(),": *Essoufler* AH.. AH.. Il faut que je me barre d'ici")
                    sleep(2)
                    print("Jarvis : Eh ben tu m'impressionnes je sais pas comment t'as fait pour reussir à tous les tuer\n")
                    sleep(1)
                    print(" *Vous quittez ", ChambreEquipage.get_nomSalle(), " en courant*")
                elif renforcer == 'n':
                    sleep(2)
                    print(": Merde, j'ai pas assez de temps. Réfléchis, réfléchis")
                    sleep(2)
                    print("Jarvis : Regarde en haut. Le conduit d'aération, tu penses pouvoir passer ?")
                    sleep(2)
                    print(hero.get_nomPersonnage(),": Je crois que j'ai pas trop le choix\n")
                    sleep(1)
                    print("Vous utilisez une chaise pour pouvoir monter. Mais la porte va ceder\n")
                    sleep(2)
                    print("Jarvis : Dépêches toi !\n")
                    sleep(1)
                    print("Vous etes presque dans le conduit")
                    sleep(1)
                    print("*PRRRRR* *Porte qui cède*")
                    sleep(1)
                    print("Vous reussissez de justesse et quittez les quartiers")
                    sleep(1)
                    print("Vous parcourez le conduit pour sortir dans le couloir.")
            elif Barricade == 'n':
                print("\n")
                sleep(2)    
                print("Jarvis : Hmm tu penses être prêt a te defendre contre tout ça ?")
                sleep(2)
                print(hero.get_nomPersonnage(),": J'en ai marre de me cacher ! Je vais tous les affronter.\n")
                sleep(1)
                print("*Les monstres surgissent*")
                sleep(1)
                print("Grrrrrrrrrr")
                combat(AlienF4,hero)
                print("\n")
                sleep(1)
                print("L'autre creature attaque à son tour\n")
                combat(AlienF4, hero)
                print("\n")
                sleep(1)
                print("Voyant les autres se faire tuer la troisieme créature part en sommant à ses enfants d'attaquer")
                print("Ils accourt pour vous attaquer\n")
                combat(AlienN5, hero)
                print("\n")
                sleep(1)
                print("L'autre vous attaque par derriere\n")
                combat(AlienN5, hero)
                print("\n")
                sleep(2)
                print(hero.get_nomPersonnage(),": *Essoufler* AH.. AH.. Il faut que je me barre d'ici")
                sleep(2)
                print("Jarvis : Eh ben tu m'impressionnes je sais pas comment t'as fait pour reussir à tous les tuer\n")
                sleep(1)
                print(" *Vous quittez ", ChambreEquipage.get_nomSalle(), " en courant*")        

        elif prendre == 'n' :
            print("\n")
            sleep(1)
            print("Vous laissez la photo")
            sleep(1)
            print("*Dans un placard il y a un pyjama*")
            prendrePyj = input("Prendre le pyjama ? (y/n)")
            if prendrePyj == 'y':
                Inventaire["Armures"].append(Pyjama)
                ouvrir = int(input("Voulez vous ouvrir l'inventaire pour l'équiper ? 1 = oui | 2 = non \n"))
                sleep(1)
                if ouvrir == 1:
                    choix_inventaire(Inventaire, hero)
                    hero.recap()
                else :
                    sleep(1)
                    print("Vous rangez l'arme dans l'inventaire \n")

                sleep(1)
                print("*Bruit au dessus de vous*")
                sleep(1)
                print("Un créature tombe du conduit d'aération au dessus de vous\n")
                sleep(1)
                combat(AlienF3,hero)
                sleep(2)
                print(hero.get_nomPersonnage(),": Bon je me barre avant que d'autre arrive\n")
                print("Vous quittez les quartiers")    

            elif prendrePyj == 'n':
                print("Vous laissez le pyjama")
                sleep(1)
                print("*Bruit au dessus de vous*")
                sleep(1)
                print("Un créature tombe du conduit d'aération au dessus de vous\n")
                sleep(1)
                combat(AlienF3,hero)
                sleep(2)
                print(hero.get_nomPersonnage(),": Bon je me barre avant que d'autre arrive\n")
                print("Vous quittez les quartiers")   
    elif prendreCle == 'n':
        sleep(1)
        print("Vous laissez les clés")
        sleep(1)
        print("Les lits sont retournés et les placards ouverts. Vous trouvez par terre une photo taché de sang.\n")
        prendre = input("Prendre la photo ? ( y = oui | n = non )\n")
        if prendre == 'y':
            sleep(1)
            print("*Prends la photo*")
            sleep(1)
            print("Il y a un homme avec sa femme et ses enfants\n")
            sleep(2)
            print(hero.get_nomPersonnage(),": Surement un soldat. C'est triste, Je me demande comment ces choses on \n"
                                           "bien pu etre laché dans le vaisseau ?\n")
            sleep(2)
            print("*Vous reposez la photo*")
            sleep(1)
            print("Tout d'un coup, quelque chose frappe la porte.")
            sleep(1)
            print("C'est une horde d'aliens qui essaye de rentrer. !\n")
            sleep(2)
            print(hero.get_nomPersonnage(),": Merde ! Merde, merde ! Je pensais qu'ils ne m'avaient pas suivi. "
                                           "\Au vus des ombres, ils ont l'aire d'être au moins trois.\n")
            sleep(1)
            Barricade = str(input("Voulez vous vous barricader ? (y = oui | n = non)\n"))
            if Barricade == 'y':
                sleep(1)
                print("*Vous faites tomber un placard contre la porte*\n")
                sleep(2)
                print(hero.get_nomPersonnage(),": Merde ! *Stressé* Qu'est ce que je fais ? ")
                sleep(2)
                print("Jarvis : La barricade ne va pas tenir longtemps")
                sleep(1)
                renforcer = input("Renforcez la barricade ? (y/n)\n")
                if renforcer == 'y':
                    sleep(2)
                    print("Vous essayez de deplacer un lit pour renforcer la barricade. Mais manquant de temps,"
                          "\n les creatures cassent la barricade.\n")
                    sleep(1)
                    print("*Les monstres surgissent*")
                    sleep(1)
                    print("Grrrrrrrrrr")
                    combat(AlienF4,hero)
                    print("\n")
                    sleep(1)
                    print("L'autre creature attaque à son tour\n")
                    combat(AlienF4, hero)
                    print("\n")
                    sleep(1)
                    print("Voyant les autres se faire tuer la troisieme créature part en sommant à ses enfants d'attaquer")
                    print("Ils accourt pour vous attaquer\n")
                    combat(AlienN5, hero)
                    print("\n")
                    sleep(1)
                    print("L'autre vous attaque par derriere\n")
                    combat(AlienN5, hero)
                    print("\n")
                    sleep(2)
                    print(hero.get_nomPersonnage(),": *Essoufler* AH.. AH.. Il faut que je me barre d'ici")
                    sleep(2)
                    print("Jarvis : Eh ben tu m'impressionnes je sais pas comment t'as fait pour reussir à tous les tuer\n")
                    sleep(1)
                    print(" *Vous quittez ", ChambreEquipage.get_nomSalle(), " en courant*")
                elif renforcer == 'n':
                    sleep(2)
                    print(": Merde, j'ai pas assez de temps. Réfléchis, réfléchis")
                    sleep(2)
                    print("Jarvis : Regarde en haut. Le conduit d'aération, tu penses pouvoir passer ?")
                    sleep(2)
                    print(hero.get_nomPersonnage(),": Je crois que j'ai pas trop le choix\n")
                    sleep(1)
                    print("Vous utilisez une chaise pour pouvoir monter. Mais la porte va ceder\n")
                    sleep(2)
                    print("Jarvis : Dépêches toi !\n")
                    sleep(1)
                    print("Vous etes presque dans le conduit")
                    sleep(1)
                    print("*PRRRRR* *Porte qui cède*")
                    sleep(1)
                    print("Vous reussissez de justesse et quittez les quartiers")
                    sleep(1)
                    print("Vous parcourez le conduit pour sortir dans le couloir.")
            elif Barricade == 'n':
                print("\n")
                sleep(2)    
                print("Jarvis : Hmm tu penses être prêt a te defendre contre tout ça ?")
                sleep(2)
                print(hero.get_nomPersonnage(),": J'en ai marre de me cacher ! Je vais tous les affronter.\n")
                sleep(1)
                print("*Les monstres surgissent*")
                sleep(1)
                print("Grrrrrrrrrr")
                combat(AlienF4,hero)
                print("\n")
                sleep(1)
                print("L'autre creature attaque à son tour\n")
                combat(AlienF4, hero)
                print("\n")
                sleep(1)
                print("Voyant les autres se faire tuer la troisieme créature part en sommant à ses enfants d'attaquer")
                print("Ils accourt pour vous attaquer\n")
                combat(AlienN5, hero)
                print("\n")
                sleep(1)
                print("L'autre vous attaque par derriere\n")
                combat(AlienN5, hero)
                print("\n")
                sleep(2)
                print(hero.get_nomPersonnage(),": *Essoufler* AH.. AH.. Il faut que je me barre d'ici")
                sleep(2)
                print("Jarvis : Eh ben tu m'impressionnes je sais pas comment t'as fait pour reussir à tous les tuer\n")
                sleep(1)
                print(" *Vous quittez ", ChambreEquipage.get_nomSalle(), " en courant*")        

        elif prendre == 'n' :
            print("\n")
            sleep(1)
            print("Vous laissez la photo")
            sleep(1)
            print("*Dans un placard il y a un pyjama*")
            prendrePyj = input("Prendre le pyjama ? (y/n)")
            if prendrePyj == 'y':
                Inventaire["Armures"].append(Pyjama)
                ouvrir = int(input("Voulez vous ouvrir l'inventaire pour l'équiper ? 1 = oui | 2 = non \n"))
                sleep(1)
                if ouvrir == 1:
                    choix_inventaire(Inventaire, hero)
                    hero.recap()
                else :
                    sleep(1)
                    print("Vous rangez l'arme dans l'inventaire \n")

                sleep(1)
                print("*Bruit au dessus de vous*")
                sleep(1)
                print("Un créature tombe du conduit d'aération au dessus de vous\n")
                sleep(1)
                combat(AlienF3,hero)
                sleep(2)
                print(hero.get_nomPersonnage(),": Bon je me barre avant que d'autre arrive\n")
                print("Vous quittez les quartiers")    

            elif prendrePyj == 'n':
                print("Vous laissez le pyjama")
                sleep(1)
                print("*Bruit au dessus de vous*")
                sleep(1)
                print("Un créature tombe du conduit d'aération au dessus de vous\n")
                sleep(1)
                combat(AlienF3,hero)
                sleep(2)
                print(hero.get_nomPersonnage(),": Bon je me barre avant que d'autre arrive\n")
                print("Vous quittez les quartiers")   



def Infirmerie(Hero):
    Infirmerie = Modele_Salle("Infirmerie")
    print("\n")
    print("Toujours à la recherche de réponses vous marchez dans le vaisseau, lorsque vous voyez l'infirmerie.")
    sleep(2)
    print("Vous entrez dans l'", Infirmerie.get_nomSalle(),". \n")
    sleep(2)
    print("C'est une petite salle, au mileu il y a une grosse machine. Une sorte de tube relié à toutes sortes d'ordinateurs. \n")
    sleep(3)
    print(Robot.get_nomPersonnage(),": Ça ressemble à une machine de soins... Tu devrais essayer, ça te soignera. \n")
    sleep(3)
    question1 = input("Voulez vous utiliser la machine de soins ? y/n \n")
    sleep(1)
    if question1 == "y":
        print(Robot.get_nomPersonnage(),":",Hero.get_nomPersonnage(),"entre à l'intérieur, je m'occupe de la configurer.\n")
        sleep(2)
    elif question1 == "n":
        print(Robot.get_nomPersonnage(),": Si",Hero.get_nomPersonnage(),"vas-y, tu as besoin de te soigner.\n")
        sleep(2)
    print("Vous entrez dans la machine. La porte se referme, à l'intérieur vous n'entendez rien. \n")
    sleep(3)
    print("*Initialisation en cours*\n")
    sleep(2)
    print("Une lumière verte vous éblouie et un air chaud parcours votre corps. \n")
    sleep(3)
    print("*Session terminée dans...* \n")
    sleep(2)
    print("*3..* \n")
    sleep(2)
    print("*2..* \n")
    sleep(2)
    print("*Erreur détectée... Annulation en cours... Autodestruction dans 5... 4...* \n")
    sleep(3)
    print("Vous appelez à l'aide mais la machine est insonorisée, personne ne peut vous entendre. \n")
    sleep(3)
    print("*3...* \n")
    sleep(2)
    print("Vous frappez désespérément contre la porte. La porte finit par s'ouvrir. \n")
    sleep(3)
    print("*2...* \n")
    sleep(2)
    print("Vous sortez de la machine. La porte se referme. \n")
    sleep(2)
    print("*1...* \n")
    sleep(2)
    print("La machine explose de l'intérieur, ce qui retient l'onde de choc. \n")
    sleep(3)
    print(Robot.get_nomPersonnage(),":",Hero.get_nomPersonnage(),"comment tu as réussis à sortir ? La machine devait se "
                                                                 "\ndétruire pourtant... \n")
    sleep(2)
    print(Robot.get_nomPersonnage(),": Euh... me regarde pas comme ça, j'ai essayé de te sortir de la mais l'ordinateur "
                                    "\n'en faisait qu'à sa tête, il ne m'écoutait plus ! \n")
    sleep(4)
    print(Robot.get_nomPersonnage(),": La machine ne t'as pas soigné du coup... Bon, on devrait s'en aller d'ici. \n")
    sleep(3)
    print("Vous vous dirigez vers la sortie. Il y a du matériel médical sur un chariot. \n")
    sleep(3)
    question2 = input("Voulez vous le prendre ? y/n \n")
    sleep(2)
    if question2 == "y":
        print("Vous avez trouvé une",Seringue_adrenaline.get_nomObjet(),"et un",kit_de_soins.get_nomObjet(),". \n")
        Inventaire["Soins"].append(Seringue_adrenaline)
        Inventaire["Soins"].append(kit_de_soins)
        print("Vous les ajoutez à l'inventaire. \n")
    elif question2 == "n":
        print("Vous ne prenez pas les objets. \n")
    sleep(2)
    print("Vous quittez l'",Infirmerie.get_nomSalle(),". \n")

    
    
def Bibliotheque(Hero):
    Bibliotheque = Modele_Salle("Bibliothèque")
    print("Vous entrez dans la", Bibliotheque.get_nomSalle(),". \n")
    sleep(2)
    print("Il y a des étagères remplies de livres. Plusieurs d'entre elles sont renversées, et des livres sont par terre. \n")
    sleep(3)
    print(Robot.get_nomPersonnage(),": Ça en fait des livres ! \n")
    sleep(2)
    print("Au fur et à mesure que vous avancez, vous entendez des petits bruits. \n")
    sleep(2)
    print(Robot.get_nomPersonnage(),": ", Hero.get_nomPersonnage(),"c'est peut-être mon imagination mais j'ai "
            "\nl'impression qu'on est suivis et puis il y a des drôles de bruits depuis tout à l'heure... \n")
    sleep(4)
    print("Vous vous retournez... il n'y a personne... soudain, un livre tombe d'une étagère. \n")
    sleep(3)
    print(Robot.get_nomPersonnage(),": Ahhhhhhhh !! Oh, c'était qu'un livre, j'ai eu super peur. \n")
    sleep(3)
    print("Vous continuez d'avancer dans la",Bibliotheque.get_nomSalle(),". Une étagère retient votre attention. "
        "\nElle n'est pas très haute, mais elle est fermée à clés. \n")
    sleep(4)
    question1 = input("Un objet brille sous une pile de livre. Voulez vous aller voir ? y/n \n")
    sleep(2)
    if question1 == "y":
        print("Vous vous approchez et commencez à soulever les livres. Un alien est en dessous ! Il a l'air de dormir...\n")
        sleep(3)
        question2 = int(input("Que voulez vous faire ? 1 = Se battre | 2 = Ne pas le réveiller et prendre la clé \n"))
        sleep(2)
        if question2 == 1:
            print("Vous le réveillez en lui lançant un livre. \n")
            sleep(2)
            combat(AlienF2, Hero)
            print(Robot.get_nomPersonnage(),": Il dormait vraiment ou bien il s'est fait assommer par la chute des livres ?"
                                            "\n C'est quand même bizarre qu'il était enfouis là-dessous. \n")
            sleep(3)
            print("Vous prenez la clé et vous approchez de l'étagère verrouillée. \n")
            sleep(2)
        elif question2 == 2:
            print(Robot.get_nomPersonnage(),": Prends ton temps surtout, faudrait pas qu'il nous saute dessus. \n")
            sleep(2)
            print("Vous vous approchez lentement et prenez la clé délicatement. L'alien ne se réveille pas. \n")
            sleep(3)
            print("Vous avancez vers l'étagère verrouillée. \n")
            sleep(2)
        print("Vous insérez la clé dans la serurre. Ce n'est pas la bonne clé... \n")
        sleep(2)
        print(Robot.get_nomPersonnage(),": Attends... tu veux dire qu'on va devoir retourner toute la bibliothèque pour retrouver la clé ? \n")
        sleep(3)
        print("Pris d'un élan de colère, vous donnez un grand coup sur l'étagère. "
              "\nAbimée par les chutes de livres et d'étagères, la sérure finit par céder. \n")
        sleep(4)
        print("La porte s'ouvre. À l'intérieur, trois livres sont enfermés dans des boites. C'est un métal solide,"
              "\n impossible de le détruire. Vous apercevez une serrure sur chaque boite. \n")
        sleep(4)
        print(Robot.get_nomPersonnage(),": Voilà à quoi servait la clé ! \n")
        sleep(2)
        print("Vous insérez la clé dans une des boites. Les serrures des autres boites disparaissent immédiatement. \n")
        sleep(3)
        print(Robot.get_nomPersonnage(),"On dirait qu'on ne peut l'utiliser qu'une fois. Tu vas devoir choisir. \n")
        sleep(2)
        print("Sur la première boite est inscrit : 'Manuel des Points faibles', sur la deuxième : 'Manuel de Vie dans l'Espace' "
              "\net sur la troisième : 'Gestion de la force'. \n")
        sleep(2)
        question3 = int(input("Quelle boite voulez vous ouvrir ? 1 = 'Manuel des Points faibles' | 2 = 'Manuel de Vie dans l'Espace' | 3 = 'Manuel de Combat' \n"))
        sleep(2)
        if question3 == 1:
            print("Vous ouvrez la première boite. \n")
            sleep(2)
            print("À l'intérieur, le 'Manuel des Points faibles'. Vous lisez le résumé au dos du livre : "
                  "\n'Vous n'aimez pas beaucoup lire, ce manuel pour jeunes recrues est parfait pour vous. "
                  "\nIl n'y a pas beaucoup de texte, mais il regroupe les bases des points faibles ennemis. *"
                  "\nVous saurez où frapper pour infliger plus de dégats à vos ennemis ! \n")
            sleep(6)
            print("Vous lisez le livre. Vous connaissez maintenant les bases des points faibles ! "
                  "\nVos coups seront concentrés sur les points vitaux de vos ennemis et vous infligerez plus de dégats. \n")
            sleep(4)
            Hero.attaque_boost(Hero.get_attaquePersonnage)
            Hero.recap()
        elif question3 == 2:
            print("Vous ouvrez la deuxième boite. \n")
            sleep(2)
            print("À l'intérieur, le 'Manuel de Vie dans l'Espace'. Vous lisez le résumé au dos du livre : "
                  "\n'Vous n'aimez pas beaucoup lire, ce manuel pour jeunes recrues est parfait pour vous. "
                  "\nIl n'y a pas beaucoup de texte, mais il regroupe les bases de la vie hors atmosphère. "
                  "\nVous saurez gérer votre respiration et vos ressources pour mieux survivre ! \n")
            sleep(6)
            print("Vous lisez le livre. Vous connaissez maintenant les bases de la vie spatiale !"
                  "\n Votre vie augmente car vous savez maintenant comment controler votre corps afin de moins vous épuiser. \n")
            sleep(4)
            Hero.vie_boost(Hero.get_viePersonnage)
            Hero.recap()
        elif question3 == 3:
            print("Vous ouvrez la troisième boite. \n")
            sleep(2)
            print("À l'intérieur, le 'Manuel de Combat'. Vous lisez le résumé au dos du livre : "
                  "\n'Vous n'aimez pas beaucoup lire, ce manuel pour jeunes recrues est parfait pour vous. "
                  "\nIl n'y a pas beaucoup de texte, mais il regroupe les bases du combat. "
                  "\nVous saurez comment vous protégez face aux attaques ennemies ! \n")
            sleep(6)
            print("Vous lisez le livre. Vous connaissez maintenant les bases du combat ! "
                  "\nVotre défense augmente car vous savez maintenant parer les coups ennemis. \n")
            sleep(4)
            Hero.defense_boost(Hero.get_defensePersonnage)
            Hero.recap()
    elif question1 == "n":
        print(Robot.get_nomPersonnage(),": Tant pis pour l'étagère. \n")
        sleep(2)
        print("Cette fois, vous en êtes sûr, quelqu'un vous observe. Un alien sort de derrière une étagère et pousse un cri strident. \n")
        sleep(3)
        print("L'alien enfouis sous les livres se réveille. Ils se rapprochent l'un de l'autre et .... fusionnent. "
              "\nIls ne font plus qu'un, l'alien est deux fois plus gros et a un corps difforme, et deux têtes ! \n")
        sleep(4)
        print(Robot.get_nomPersonnage(),": Oh oh... on aurait du s'occuper de celui qui dormait tout à l'heure... \n")
        combat(AlienF3,Hero)
        print(Robot.get_nomPersonnage(),": qui aurait cru que deux d'entre eux pouvaient fusionner... \n")
        sleep(2)  
    print("Vous apercevez la porte de sortie de la",Bibliotheque.get_nomSalle(),". "
        "\nElle est encombrée par des tas de livres mais il y a un hublot assez grand pour s'y faufiller. \n")
    sleep(4)
    print(Robot.get_nomPersonnage(),": À toi l'honneur,",Hero.get_nomPersonnage(),".\n")
    sleep(2)
    print("Vous brisez la vitre du hublot et passez à travers. \n")
    sleep(2)
    print("Vous quittez la",Bibliotheque.get_nomSalle(),". \n")


def Win2():
    print("\n")
    sleep(2)
    print("FELICITATIONS !!!!")
    sleep(2)
    print("Vous avez réussi à vous enfuir du vaisseau !")
    sleep(2)
    print("Vous êtes en direction de la Terre, mais le vaisseau aussi...")
    sleep(2)
    print("Vous avez préféré votre vie à celle d'une planète.")
    sleep(1)
    print("MERCI D'AVOIR PRIS LE TEMPS DE JOUER. LA SUITE AU PROCHAIN EPISODE (PEUT-ETRE).")


def Win1():
    print("\n")
    sleep(2)
    print("FELICITATIONS !!!!")  
    sleep(2)
    print("Vous avez sauvé la Terre en dépit de votre propre vie.")
    sleep(2)
    print ("Repos éternel soldat.")
    sleep(2)
    print("MERCI D'AVOIR PRIS LE TEMPS DE JOUER. LA SUITE AU PROCHAIN EPISODE (PEUT-ETRE).")

#Hero = hero('Kevin',10,10,10,10,0,0,0)
