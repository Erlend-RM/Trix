class Buss:


    def __init__(self, makskapasitet):
        self._maks = makskapasitet
        self._antallPassasjerer = 0


    def hentAntall(self):
        print(f"Det er {self._antallPassasjerer} på bussen.")


    def erTom(self):
        return self._antallPassasjerer == 0


    def erFull(self):
        return self._antallPassasjerer >= self._maks


    def plukkOpp(self):
        if self.erFull():
            print("Bussen er full,")
        else:
            print("Tok opp en passasjer.")
            self._antallPassasjerer += 1


    def slippAv(self):
        if self.erTom():
            print("Det er ingen passasjer på bussen.")
        else:
            print("Slapp av en passasjer")
            self._antallPassasjerer -=1


def hovedprogram():
    buss1 = Buss(20)
    for i in range(10):
        buss1.plukkOpp()
    buss1.hentAntall()
    for i in range(12):
        buss1.plukkOpp()
    buss1.hentAntall()
    for i in range(18):
        buss1.slippAv()
    buss1.hentAntall()
    for i in range(3):
        buss1.slippAv()
    buss1.hentAntall()


hovedprogram()
