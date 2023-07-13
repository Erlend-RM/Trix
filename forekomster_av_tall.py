#a)
def les_tall_fra_fil(filnavn):
    fil = open(filnavn, "r")
    tallListe = []
    for tall in fil:
        tallS = int(tall.strip())
        tallListe.append(tallS)
    return tallListe


#b)
def antall_forekomster(liste, tall):
    teller = 0
    for tallL in liste:
        if tall == tallL:
            teller += 1
    return teller


#c)
def flest_formkomster(liste):
    antallForekomster = 0
    flest = 0
    for tallL in liste:
        antallForekomster = antall_forekomster(liste, tallL)
        if antallForekomster >= flest:
            flest = antallForekomster
            tall = tallL
    return tall


#d)
def hovedprogram(filnavn, tall):
    liste = les_tall_fra_fil(filnavn)
    forekomster = antall_forekomster(liste, tall)
    flestForekomster = flest_formkomster(les_tall_fra_fil(filnavn))
    return f"Liste: {liste}\n{tall} forkommer: {forekomster} ganger\nTallet som forekommer mest er {flestForekomster}"

print(hovedprogram("_tall.txt",2))
