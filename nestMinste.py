tall = [1, 1, 2, 2, 3, 4, 5]

def nestMinst(liste):
    minst = liste[0]
    for i in liste:
        if minst > i:
            minst = i
    while(minst in liste):
        liste.remove(minst)
    minst = liste[0]
    for i in liste:
        if minst > i:
            minst = i
    return minst

print(nestMinst(tall))
