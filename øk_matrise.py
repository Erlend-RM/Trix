#a)
liste = [69, 420, 12, 5]
tall = 48


def leggerTil(liste, tall):
    nyttTall = 0
    nyListe = []
    for nr in liste:
        nyttTall =nr + tall
        nyListe.append(nyttTall)
    return nyListe


print(leggerTil(liste, tall))


#b)
nostetListe = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]


def leggerTilUnderveis(nostetListe):
    nyNostetListe =[]
    lengdeList = len(nostetListe)
    for i in range(lengdeList):
        nyNostetListe.append(leggerTil(nostetListe[i],i+1))
    return nyNostetListe


print(leggerTilUnderveis(nostetListe))

#c)
def skriverUtNostetListe(nostetListe):
    for liste in nostetListe:
        print(liste)

skriverUtNostetListe(leggerTilUnderveis(nostetListe))

#d)
eksempel_matrise = [[0, 1, 2], [3, 2, 1], [1, 1, 0]]

skriverUtNostetListe(leggerTilUnderveis(eksempel_matrise))
