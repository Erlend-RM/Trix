class Bil:


    def __init__(self, eier):
        self._eier = eier


    def skrivUtNavn(self):
        print(self._eier)


bil1 = Bil("Erlend Ronæss Melleby")
bil1.skrivUtNavn()
