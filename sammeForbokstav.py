#1)
personer = {}


#2)
svar = input("Vil du legge til 'y'(yes) eller 'n'(no): ")
while svar == "y":
    navn = input("Skriv inn navnet til en person: ")
    alder = input("Skriv inn alderen til personen: ")
    personer[navn] = alder
    svar = input("Vil du legge til 'y'(yes) eller 'n'(no): ")

svar2 = input("Skriv inn en bokstav: ")
loekke = False
lengdeSvar2 = len(svar2)
while loekke == False:
    if lengdeSvar2 == 1:
        break
    elif svar2 not in personer.keys():
        svar2 = input(f"Svaret er ugyldig")
    svar2 = input("Skriv inn en bokstav: ")
    lengdeSvar2 = len(svar2)

for key in personer.keys():
    foersteBok = key[0]
    if svar2 == foersteBok.lower() or svar2 == foersteBok:
        print(f"Navnet: {key}\nAlder: {personer[key]}")
    else:
        print("Finnes ingen navn på denne bokstaven")
