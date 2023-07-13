liste = ["en", "pluss", "to", "pluss", "tre", "er", "seks"]


def reverserListe(liste):
    reversertListe = []
    lengdeList = len(liste)
    for i in liste:
        reversertListe.insert(0, i)
    return reversertListe

print(reverserListe(liste))
