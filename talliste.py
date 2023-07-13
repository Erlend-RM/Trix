#a) b) c) d)
i = 0
sum = 0
liste = []
minderEnnTi = []


print("Skriv in 5 tall under.")
while i in range(5):
    tall = int(input("Skriv inn tall: "))
    sum += tall
    liste.append(tall)
    if tall < 10:
        minderEnnTi.append(tall)
    i += 1

if 5 in liste:
    print("5 finnes i denne listen.")
else:
    print("5 finnes ikke i denne listen.")


print(liste)
print(sum)
print(minderEnnTi)

#e)
nyNyListe = []

def sumAvListe(liste):
    sum = 0
    for nr in liste:
        sum += nr
    return sum

def laveVerdier(liste):
    for nr in liste:
        if nr < 10:
            nyNyListe.append(nr)
    return(nyNyListe)

def sok(liste):
    if 5 in liste:
        print("5 finnes i listen.")
    else:
        print("5 finnes ikke i listen.")

print(sumAvListe(liste))
print(laveVerdier(liste))
sok(liste)
