#1)
def lesInnMatFil(filnavn):
    fil = open(filnavn, "r")
    matretter = []
    for linje in fil:
        info = linje.split(",")
        matretter.append(info[0])
    fil.close()
    return matretter

lesInnMatFil("matFil.txt")

#2)
from random import choice
def velgMatretter(tall, filnavn):
    matretter = lesInnMatFil(filnavn)
    valgtematretter = []
    for i in range(tall):
        tilfeldig = choice(matretter)
        valgtematretter.append(tilfeldig)
    return valgtematretter

print(velgMatretter(5, "matFil.txt"))

def skrivMatretterTilFil(tall, innfil, utfil):
    filut = open(utfil, "w")
    matretter = velgMatretter(tall, innfil)
    for matrett in matretter:
        filut.write(matrett+"\n")
    filut.close()

skrivMatretterTilFil(5, "matFil.txt", "matFil2.txt")
