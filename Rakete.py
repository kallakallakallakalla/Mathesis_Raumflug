#Gruppe: Raketenbahn
import time
import scipy as sp
import numpy as np
import math as m



Sol_Objekte = []
Raumschiffe = []
t = 0 # si : s




class Rakete:
    def __init__(self, Ausrichtung, Bewegung, Drehbewegung, Position, Treibstoff, RCS_Treibstoff, m):
        self.Ausrichtung = (0,0,0) # Bezugspunkt : Ekliptik der Erde  in Grad
        self.Bewegung = (0,0,0) # Bezugspunkt : Ekliptik der Erde  si : m/s
        self.Drehbewegung = (0,0,0)          # in Grad / s
        self.Position = (0,0,0) # Bezugspunkt : Ekliptik der Erde  si : m
        self.Treibstoff = 10 # in Δv ?
        self.RCS_Treibstoff = 0 # reaction control system
        self.m = 0 #    si : kg

    def treibstoff_verbrauch(self):
        self.Treibstoff -= 1
        if Treibstoff >= 8:
            print("Wir haben noch viel Treibstoff. ")
        elif Treibstoff <= 3:
            print("Wir haben kaum noch Treibstoff, wir müssen bald landen. ")
        else:
            print("Wir haben noch genug Treibstoff. ")

    def Beschleunigung(self, a):
        if self.Treibstoff != 0 :


    def Einwirkung_anderer_Objekte():
        for objekt in Objekte:
            gravitation = objekt.m * self.m / entfernung**2 * sp.constants.gravitational_constant






    def Rotationsa(self, drehung, achse):
        if self.RCS_Treibstoff != 0 :
            if achse == 1:
                self.RCS_Treibstoff -= 1
                self.Drehbewegung[0] += drehung
            elif achse == 2:
                self.RCS_Treibstoff -= 1
                self.Drehbewegung[1] += drehung
            if achse == 3:
                self.RCS_Treibstoff -= 1
                self.Drehbewegung[2] += drehung
        else:
            print("RCS_Treibstoff = 0")

    def Update(self):
        while True:
            time.sleep(1)
            self.Ausrichtung = self.Ausrichtung + self.Drehbewegung
            self.Position = self.position + self.Bewegung











class Planet:
    def __init__(self, m, position, monde_anzahl):
        self.m = 0
        self.position = (0,0,0)
        self.monde_anzahl


class Mond:
    def  __init__(self, m, position, zug_Koerper):
        self.position = (0,0,0) # Bezugspunkt zugehörigere Körper????
        pass

class Sonne:
    def __init__(self, m, position):
        self.m = 0
        self.position(0,0,0)

class Asteroid:
    def __init__(self, m, position):
        self.m = 0
