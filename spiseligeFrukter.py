class Frukt:

    def __init__(self, navn, vannPer100Gram, spiselig):
        self._navn = navn
        self._vannPer100 = vannPer100Gram
        self._spiselig = spiselig

    def hentNavn(self):
        return self._navn

    def hentVannPr100(self):
        return self._vannPer100

    def erSpiselig(self):
        return self._spiselig

groentEple = Frukt("Grønt Eple", 86, True)
roedtEple = Frukt("Rødt Eple", 89, True)
hasselNoett = Frukt("Hasselnøtt", 12, True)
sukkerert = Frukt("Sukkerert", 89, True)
trollhegg = Frukt("Trollhegg", 90, False)

fruktListe = [groentEple, roedtEple, hasselNoett, sukkerert, trollhegg]

spiseligeVannfrukter = []

for enfrukt in fruktListe:
    if enfrukt.erSpiselig() and enfrukt.hentVannPr100() > 85:
        spiseligeVannfrukter.append(enfrukt)

print("Spiselige vannfrukter:")
for enfrukt in spiseligeVannfrukter:
    print(enfrukt.hentNavn())
