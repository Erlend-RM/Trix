tall = int(input("Skriv inn et tall: "))

def primtall(tall):
    teller = tall - 1
    er_primtall = True
    while teller > 1:
        if tall % teller == 0:
            er_primtall = False
        teller -= 1
    if er_primtall:
        print("Fant primtall ", tall)
while tall > 1:
    primtall(tall)
    tall -= 1

primtall(tall)
