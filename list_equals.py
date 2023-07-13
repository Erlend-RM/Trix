liste_en = [1, 2, 3]
liste_to = [2, 1, 3]

#a)
def equals(liste_en, liste_to):
    if liste_en == liste_to:
        print("Ja listene er like!")
    else:
        print("Nei listenen er ikke like...")


equals(liste_en, liste_to)


#b)
def sameset(liste_en, liste_to):
    teller = 0
    for nr in set(liste_en):
        if nr in liste_to:
            teller += 1
    if teller == len(set(liste_to)):
        print("Ja disse listene har samme elementer!")
    else:
        print("nei disse har ikke samme elementer...")

sameset(liste_en, liste_to)
