#a)
def lesFil(filnavn):
    fil = open(filnavn)
    ordbok = {}
    for linje in fil:
        liste = linje.strip().split(":")
        ordbok[liste[0]] = liste[1]
    return ordbok

print(lesFil("bil.txt"))


#b)
def euroSong(filnavn):
    fil = open(filnavn)
    ordbok = {}
    aar = []
    land = []
    for linje in fil:
        liste = linje.strip().split(" ")
        aar.append(liste[0])
        land.append(liste[1])
    ordbok["år"] = aar
    ordbok["land"] = land
    return ordbok

print(euroSong("song_contest.txt"))


#c)
def flestPoeng(filnavn):
    fil = open(filnavn)
    ordbok = {}
    sum = 0
    for linje in fil:
        liste = linje.strip().split(":")
        poengliste = liste[1].split(",")

        for poeng in poengliste:
            tall = int(poeng)
            sum += tall
        ordbok[liste[0]] = sum

    return ordbok

print(flestPoeng("poeng.txt"))
