import time
import threading

class Horloge:
    def __init__(self):
        self.heure = 0
        self.minute = 0
        self.seconde = 0
        self.alarme = None
        self.thread = threading.Thread(target=self.incrementer_temps)

    def incrementer_temps(self):
        while True:
            if self.seconde == 60:
                self.seconde = 0
                self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.heure += 1
            if self.heure == 24:
                self.heure = 0
            self.seconde += 1
            self.afficher_heure()
            if self.alarme is not None and (self.heure, self.minute, self.seconde) == self.alarme:
                print("Alarme !")
            time.sleep(1)

    def afficher_heure(self):
        print("{:02d}:{:02d}:{:02d}".format(self.heure, self.minute, self.seconde))

    def regler_heure(self, h, m, s):
        self.heure = h
        self.minute = m
        self.seconde = s

    def regler_alarme(self, h, m, s):
        self.alarme = (h, m, s)

    def demarrer(self):
        self.thread.start()

# Test de la classe Horloge
horloge = Horloge()
horloge.regler_heure(0, 0, 0)
horloge.regler_alarme(7, 30, 10)
horloge.demarrer()