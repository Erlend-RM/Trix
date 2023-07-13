def finnAlleFibTall(tall):
    fibTall = []
    tall1 = 0
    tall2 = 1
    fibTall.append(tall1)
    while tall2 <= tall:
        fibTall.append(tall2)
        nesteTall = tall1 + tall2
        tall1 = tall2
        tall2 = nesteTall
    return fibTall


def laBrukerSkriveInnTall():
    tall = int(input("Skriv inn et tall: "))
    return tall


print(finnAlleFibTall(laBrukerSkriveInnTall()))
