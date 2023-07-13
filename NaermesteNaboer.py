import math


class Punkt:


    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
        self._punkt = None


    def __str__(self):
        return f"x: {self._x}, y: {self._y} og z: {self._z}"


    def faaAvstand(self, annetPunkt):
        avstandMellom = math.sqrt((annetPunkt._x - self._x)**2 + (annetPunkt._y - self._y)**2 + (annetPunkt._z - self._z)**2)
        return avstandMellom


    def faaNaermestePunkt(self, punkter):
        naermestePunkt = None
        minsteAvstand = None
        for annetPunkt in punkter:
            avstand = self.faaAvstand(annetPunkt)
            if minsteAvstand is None:
                minsteAvstand = avstand
                naermestePunkt = annetPunkt
            elif avstand < minsteAvstand:
                minsteAvstand = avstand
                naermestePunkt = annetPunkt
        return naermestePunkta



    def faaPunktFraBruker():
        x = input("Skriv in x verdi: ")
        y = input("Skriv in y verdi: ")
        z = input("Skriv in z verdi: ")
        p1 = Punkt(x, y, z)
        return p1


    def lesPunkterFraFil(filnavn):
        punkter = []
        fil = open(filnavn, "r")

        for linje in fil:
            tall = linje.split(",")
            x = float(tall[0])
            y = float(tall[1])
            z = float(tall[2])
            punkt = Punkt(x, y, z)
            punkter.append(punkt)
        fil.close()
        return punkter
