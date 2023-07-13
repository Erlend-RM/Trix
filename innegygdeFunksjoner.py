string = "Hei!"

#a) len() funksjonen
def lengde(string):
    teller = 0
    for bokstav in string:
        teller += 1
    return teller


print(f"Med len funk: {len(string)}")
print(f"Laget selv: {lengde(string)}")


#b) str.count() funksjonen
string = "Hei!!!!..!!"
karakter = "!!"
def teller(string, karakter):
    teller = 0
    for bokstav in string:
        if karakter == bokstav:
            teller += 1
    return teller


print(f"Med str.count(): {str.count(string,karakter)}")
print(f"Laget selv: {teller(string, karakter)}")

#c) range() funksjonen
fra = 1
til = 10

def fraTil(fra, til):
    omrade = []
    teller = til
    while teller != fra:
        teller -= 1
        omrade.append(teller)
    omrade.reverse()
    return omrade


print(f"Med range(): {range(fra, til)}")
print(f"Laget selv: {fraTil(fra, til)}")
