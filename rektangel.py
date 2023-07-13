class Rektangel:

    def __init__(self, lengde, bredde):
        self._lengde = lengde
        self._bredde = bredde


    def oekLengden(self, oekning):
        self._lengde += oekning
        return self._lengde


    def oekBredde(self, oekning):
        self._bredde += oekning
        return self._bredde


    def reduserLengden(self, reduksjon):
        self._lengde -= reduksjon
        return self._lengde


    def reduserBredden(self, reduksjon):
        self._bredde -= reduksjon
        return self._bredde


    def areal(self):
        areal = self._lengde * self._bredde
        return f"Arealet er: {areal} cm^2"


    def omkrets(self):
        omkrets = (self._lengde * 2) + (self._bredde * 2)
        return f"Omkretsen er: {omkrets} cm"

langtRektangel = Rektangel(15, 3)
bredtRektangel = Rektangel(2, 9)
print(langtRektangel.areal())
print(bredtRektangel.areal())
bredtRektangel.oekLengden(5)
langtRektangel.oekBredde(10)
print(langtRektangel.omkrets())
print(bredtRektangel.omkrets())
bredtRektangel.reduserLengden(5)
langtRektangel.reduserBredden(10)
print(langtRektangel.omkrets())
print(bredtRektangel.omkrets())
