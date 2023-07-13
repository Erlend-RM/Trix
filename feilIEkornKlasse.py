class Ekorn:
    def __init__(self, pelsfarge, bosted):
        self._pelsfarge = pelsfarge
        self._bosted = bosted

    def hentPelsfarge(self):
        return self._pelsfarge

    def hentBosted(self):
        return self.bosted

ekorn1 = Ekorn("brunt", "Drammen")
ekorn2 = Ekorn("svart", "Stavanger")
ekorn3 = Ekorn("grått", "Tjøme")
