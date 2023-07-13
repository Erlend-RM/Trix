beholdning = {}

grønnsak = input("Vil du legge inn grønnsaker i beholdning: 'ja' eller 'nei'(skriv 'nei' for å stoppe innlegg til beholdning.) ")

while "nei" != grønnsak:
    grønnsak = input("Oppgi en grønnsak: ")
    if grønnsak == "nei":
        for x, y in beholdning.items():
            print(x, y)
        break
    pris = int(input("Oppgi prisen på grønnsaken: "))
    if isinstance(pris, int):
        beholdning[grønnsak] = pris
