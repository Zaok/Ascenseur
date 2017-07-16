#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ascenseur
# 20170716
# V 0.1
# Auteur : AD

# Simulateur d'ascenseur

class Ascenseur():
    def __init__ (self, numero, etage_min, etage_max):
        self.numero = numero
        self.etage_min = etage_min
        self.etage_max = etage_max

    etage_actuel = 0
    vitesse = 1
    disponible = True
    direction = "Neutre"

    def description(self):
        print ("Numero : ",self.numero, 
            "\n", "Etage min : ", self.etage_min, 
            "\n", "Etage max : ", self.etage_max, 
            "\n", "Etage actuel : ", self.etage_actuel, 
            "\n", "Vitesse : ", self.vitesse,
            "\n", "Diponible : ", self.disponible
            "\n", "Direction : ", self.direction)

    def appel(self, etage_demandeur, direction):
        #Change l'état de l'ascenseur
        #todo
        self.disponible = False
        self.direction = direction
        self.etage_actuel = etage_demandeur
    
    def utilisation(self, etage_destination):
        #todo : rename
        pass

def menu():
    choix = raw_input("Que voulez-vous faire ? \n1 - Monter \n2 - Descendre")
    if choix == 1 or choix.lower() == "monter":
        if asc.disponible == True:
            asc.appel(etage_demandeur, "haut")
        else:
            print "aucun ascenseur disponible"
        print choix

    elif choix == 2 or choix.lower() == "descendre":
        asc.appel(etage_demandeur, "bas")
        print choix

    else :
        print "Choix invalide !"

asc = Ascenseur(1, -2, 15)
asc.description()

menu()