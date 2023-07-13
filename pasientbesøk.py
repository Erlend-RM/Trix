pasientListe1 = [[31], [14, 15, 16, 17, 18]]
pasientListe2 = [[1, 2, 3], [2, 3, 4], [28, 31], [14, 15, 16, 17, 18]]
pasientListe3 = [[1, 2, 3], [2, 3, 4], [28, 31], [14, 15, 16, 17, 18], [1, 2, 4, 5], [9, 12, 16, 19], [21, 23, 25, 27, 28]]


#1)
def maxBesok(liste):
    flestBesok = len(liste[0])
    pasientNr = 0
    for i in range(len(liste)):
        if len(liste[i]) > flestBesok:
            flestBesok = len(liste[i])
            pasientNr = i
    return f"Pasient nr. {pasientNr + 1} har flest besøk."

print(maxBesok(pasientListe1))
print(maxBesok(pasientListe2))
print(maxBesok(pasientListe3))


#2)
def faerrestBesok(liste):
    minstBesok = len(liste[0])
    pasientNr = 0
    for i in range(len(liste)):
        if len(liste[i]) < minstBesok:
            minstBesok = len(liste[i])
            pasientNr = i
    return f"Pasient nr. {pasientNr+1} har færrest besøk."

print(faerrestBesok(pasientListe1))
print(faerrestBesok(pasientListe2))
print(faerrestBesok(pasientListe3))


#3)
def alleBesok(liste):
    totaltBesok = 0
    for dato in liste:
        totaltBesok += len(dato)
    return f"Totalt pasient besøk: {totaltBesok}"

print(alleBesok(pasientListe1))
print(alleBesok(pasientListe2))
print(alleBesok(pasientListe3))


#4
def hvemVarPaaDato(dato,liste):
    pasientListe = []
    if dato < 1 or dato > 31:
        return pasientListe
    for i in range (len(liste)):
        for dag in liste[i]:
            if dag == dato:
                pasientListe.append(i+1)
    return f"Pasient nr. {pasientListe} var der den {dato}."

print(hvemVarPaaDato(31,pasientListe1))
print(hvemVarPaaDato(2, pasientListe2))
print(hvemVarPaaDato(2, pasientListe3))
