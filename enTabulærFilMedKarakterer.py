def sorter_etter_karakter(filnavn):
    fil = open(filnavn, "r")
    karakterbok = {}
    for linje in fil:
        navn, karakter = linje.strip().split(",")
        if karakter in karakterbok:
            karakterbok[karakter].append(navn)
        else:
            karakterbok[karakter] = [navn]
    fil.close()
    return karakterbok

print(sorter_etter_karakter("karakter.csv"))


def skriv_ut_sortert(ordbok):
    for karakter in sorted(ordbok.keys()):
        print(f"{karakter}: {ordbok[karakter]}")

skriv_ut_sortert(sorter_etter_karakter("karakter.csv"))

def hent_vanligste_karakter(ordbok):
    mest = 0
    vanligste = ""
    for karakter in ordbok:
        if len(ordbok[karakter]) > mest:
            mest = len(ordbok[karakter])
            vanligste = f"{karakter}"
    return vanligste, mest

print(hent_vanligste_karakter(sorter_etter_karakter("karakter.csv")))
