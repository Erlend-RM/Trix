class EspressoMaskin:

    def __init__(self, makskapasitet):
        self._MAKS = makskapasitet
        self._vannmengde = 1000

    def lagEspresso(self):
        if self._vannmengde >= 40:
            self._vannmengde -= 40
            print("Lager Espresso")
            print("Ferdig, nyt!")

    def lagLungo(self):
        if self._vannmengde >= 110:
            self._vannmengde -= 110
            print("Lager Lungo")
            print("Ferdig, nyt!")
        else:
            print("Ikke nok vann")


    def fyllVann(self, ml):
        if ml <= self._MAKS - self._vannmengde:
            self._vannmengde += ml
            print(f"Fylte på med {ml} ml vann.")
            print(f"Det er nå {self._vannmengde} ml igjen")
        else:
            print("Det er ikke plass til så mye vann...")


    def hentVannmengde(self):
        return self._vannmengde


def hovedprogram():
    maskin1 = EspressoMaskin(10)
    stoerrelse = input("Vil du ha Espresso (liten) eller Lungo (stor) kaffe?: ")
    paa = True
    while paa == True:
        stoerrelse = input("Vil du ha Espresso (liten) eller Lungo (stor) kaffe?: ")
        if stoerrelse == "liten" or stoerrelse == "Espresso" or stoerrelse == "espresso":
            maskin1.lagEspresso()
        elif stoerrelse == "stor" or stoerrelse == "Lungo" or stoerrelse == "lungo":
            maskin1.lagLungo()
        elif stoerrelse == "Fyll paa" or stoerrelse == "fyll paa":
            ml = int(input("Hvor mye vil du fylle på?(ml): "))
            maskin1.fyllVann(ml)
        elif stoerrelse == "skru av" or stoerrelse == "Skru av":
            paa = False

hovedprogram()
