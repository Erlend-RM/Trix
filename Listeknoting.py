listeA = ["a", "b", "c"]
listeB = [1, 2, 3]

#a)
def vanligKonkat(liste1, liste2):
    nyListe = []
    nyListe.extend(liste1)
    nyListe.extend(liste2)
    return nyListe


liste = vanligKonkat(listeA, listeB)
print(listeA)
print(listeB)
print(liste)


#b)
def annenHverKonkat(liste1, liste2):
    nyListeA =[]
    for bokstav, nr in zip(liste1, liste2):
        nyListeA.append(bokstav)
        nyListeA.append(nr)
    return nyListeA

print(annenHverKonkat(listeA, listeB))

#c)
def tallTilListe(tall):
    tallListe = []
    for i in str(tall):
        tallListe.append(int(i))
    return tallListe

print(tallTilListe(8000))
