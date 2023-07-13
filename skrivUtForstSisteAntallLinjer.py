def forsteLinjer(filnavn, antall_linjer):
    fil = open(filnavn, "r")
    idx = 0
    for linje in fil:
        if idx < antall_linjer:
            print(linje.strip())
        idx += 1
    fil.close()

def sisteLinjer(filnavn, antall_linjer):
    fil = open(filnavn, "r")
    linjene = []
    for linje in fil:
        linjene.append(linje.strip())
    fil.close()
    indeks = (len(linjene) - antall_linjer) - 1
    for linje in linjene[indeks:]:
        print(linje)


forsteLinjer("maksOrdPerLinje.txt", 2)
sisteLinjer("maksOrdPerLinje.txt", 2)
