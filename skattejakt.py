#a)
skattekart = []
stoerrelse = 5
for e in range(stoerrelse):
    a = []
    for e in range(stoerrelse):
        a.append("O")
    skattekart.append(a)


#b)
riktigKoordinat = False
while riktigKoordinat == False:
    koordinatX = int(input("Spiller 1, Skriv inn x koordinat(1-5): "))
    koordinatY = int(input("Skriv inn y koordinat(1-5): "))
    if koordinatX < 6 and koordinatY < 6 or koordinatX >= 1 and koordinatY >= 1:
        riktigKoordinat = True
        skattekart[koordinatX-1][koordinatY-1] = "X"
    else:
        print("Ikke gyldige koordinater, prøv igjen...")


#a)
for e in skattekart:
    for f in e:
        print(f, end="")
    print("")

#c)
for e in range(5):
    print("")

for e in range(3):# riktigKoordinat == False:
    koordinatX2 = int(input("Spiller 2, gjett x koordinat(1-5): "))
    koordinatY2 = int(input("Gjett her y koordinat(1-5): "))
    if koordinatX < 6 and koordinatY < 6 or koordinatX >= 1 and koordinatY >= 1:
        if skattekart[koordinatX-1][koordinatY-1] == skattekart[koordinatX2-1][koordinatY2-1]:
            print("Riktig du VANT!")
            for e in skattekart:
                for f in e:
                    print(f, end="")
                print("")
            break
        elif e == 2:
            print("Du Tapte...")
            for e in skattekart:
                print("Her lå skatten:")
                for f in e:
                    print(f, end="")
                print("")
            break
        else:
            print("Det var dessverre feil gjett igjen...")
