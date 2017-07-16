# Ascenseur
# 20170716
# V 0.1
# Auteur : AD

# Simulateur d'ascenseur

class Ascenseur(Object):
    
    def __init__ (self, etage_min, etage_max):
        self.etage_min = etage_min
        self.etage_max = etage_max

    vitesse = 1

    def description():
        print "Etage min : ", self.etage_min, "\n Etage max : ", self.etage_max, "\n Etage actuel : ", self.etage_actuel