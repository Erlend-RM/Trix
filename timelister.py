#1) leser timeliter og lager ordbok
def leserTimeliste(filnavn):
    fil = open(filnavn, "r")
    forsteLinje = True

    for linje in fil:
        if forsteLinje:
            navn = linje.strip().split(",")
            timelisteBok = {}
            for ord in navn:
                timelisteBok[ord] = []
            forsteLinje = False
        else:
            timer = linje.strip().split(",")
            for i in range(len(navn)):
                ord = navn[i]
                time = int(timer[i])
                timelisteBok[ord].append(time)
    fil.close()

    return timelisteBok


print(leserTimeliste("fil1.txt"))
print(leserTimeliste("fil2.txt"))

#2) Slår sammen timelister
def slarSammenTimeLister(filnavn1, filnavn2):
    fil1 = leserTimeliste(filnavn1)
    fil2 = leserTimeliste(filnavn2)
    nyTimebok = {}
    for key in fil1:
        nyTimebok[key] = fil1[key]
    for key in fil2.keys():
        if key in nyTimebok.keys():
            for i in range(5):
                nyTimebok[key][i] += fil2[key][i]
            else:
                nyTimebok[key] = fil2[key]
    return fil1

print(slarSammenTimeLister("fil1.txt", "fil2.txt"))

#3)
timelisteOrdbok = {
'Louise': [8, 8, 4, 8, 8],
'Sven': [6, 6, 6, 6, 6],
'Kaja': [7, 7, 0, 4, 0],
'Anna': [6, 7, 6, 8, 6],
'Odd': [4, 4, 5, 5, 5],
'Paal': [8, 8, 8, 8, 0],
}

def lagerFilTimeliste(ordbok, filnavn):
    fil = open(filnavn, "w")
    for key in ordbok:
        fil.write(key + ",")
    fil.write("\n")
    for value in ordbok.values():
        for tall in value:
            fil.write(str(tall) + ",")
        fil.write("\n")
    fil.close()


lagerFilTimeliste(timelisteOrdbok, "fil3.txt")
