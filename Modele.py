class Modele_Personnage :
    
    def __init__(self, nom, vie, attaque, defense, level):
        self.nom = nom
        self.vie = vie 
        self.attaque = 0
        self.defense = 0
        
        self.level = level

    def get_nom(self):
        return self.nom

    def get_vie(self):
        return self.vie

    def get_attaque(self):
        return self.attaque

    def get_defense(self):
        return self.defense
   
    def get_level(self):
        return self.level    

    def dommage(self, dommage):
        self.vie = self.vie - dommage

    def attack_player(self, cible):
        cible.dommage(self.attaque)
        print(cible.get_nom(), "a prit", self.attaque, "de dégats.")


class Modele_Salle :

    def __init__(self, nom) :
        self.nom = nom
        print("Vous etes dans la salle", nom)

    def get_nom(self):
        return self.nom


class Modele_Arme :

    def __init__(self, nom, dommage) :
        self.nom = nom
        self.dommage = dommage

    def get_nom(self) :
        return self.nom  

    def get_dommage_enplus(self):
        return self.dommage 


class Modele_Armure :
    
    def __init__(self, nom, defense) :
        self.nom = nom
        self.defense = defense

    def get_nom(self):
        return self.nom  

    def get_defense_enplus(self):
        return self.defense 