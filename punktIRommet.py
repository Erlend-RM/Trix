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


def hovedprogram():
    p1 = Punkt(1, 2, 3)
    punkter = [Punkt(5, 5, 3), Punkt(1, 2, 5), Punkt(6, 4, 1)]
    naermest = p1.faaNaermestePunkt(punkter)

    print(f"Naermeste punktet til {p1} er {naermest}")


hovedprogram()
