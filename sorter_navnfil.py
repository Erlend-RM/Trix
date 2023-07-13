def sortererPersonerOgHunder(filnavn):
    fil = open(filnavn)
    personer = []
    hunder = []
    for linje in fil:
        linjeS = linje.strip().split()
        if "P" in linjeS:
            personer.append(linjeS[1])
        elif "H" in linjeS:
            hunder.append(linjeS[1])
    return personer, hunder


print(sortererPersonerOgHunder("navn1.txt"))
