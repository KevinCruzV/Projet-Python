class Modele_Personnage :
    
    def __init__(self, nomPersonnage, viePersonnage, attaquePersonnage, defensePersonnage, levelPersonnage):
        self.nomPersonnage = nomPersonnage
        self.viePersonnage = viePersonnage 
        self.attaquePersonnage = attaquePersonnage
        self.defensePersonnage = defensePersonnage 
        self.levelPersonnage = levelPersonnage

    def get_nomPersonnage(self):
        return self.nomPersonnage

    def get_viePersonnage(self):
        return self.viePersonnage

    def get_attaquePersonnage(self):
        return self.attaquePersonnage

    def get_defensePersonnage(self):
        return self.defensePersonnage
   
    def get_levelPersonnage(self):
        return self.levelPersonnage   

    def dommage(self, dommage):
        self.viePersonnage = self.viePersonnage - dommage

    def attack_player(self, cible):
        cible.dommage(self.attaquePersonnage)
        print(cible.get_nomPersonnage(), "a prit", self.attaquePersonnage, "de dégats.")
        


class Modele_Salle :

    def __init__(self, nomSalle) :
        self.nomSalle = nomSalle

    def get_nomSalle(self):
        return self.nomSalle


class Modele_Arme :

    def __init__(self, nomArme, dommageArme):
        self.nomArme = nomArme
        self.dommageArme = dommageArme

    def get_nomArme(self):
        return self.get_nomArme

    def get_dommageArme(self):
        return self.dommageArme

class Modele_Armure :
    
    def __init__(self, nomArmure, defenseArmure) :
        self.nomArmure = nomArmure
        self.defenseArmure = defenseArmure

    def get_nomArmure(self):
        return self.nomArmure  

    def get_defenseArmure(self):
        return self.defenseArmure


class Objet_de_Quete:
    def __init__(self, nomObjet):
        self.nomObjet = nomObjet

    def get_nomObjet(self):
        return self.nomObjet



