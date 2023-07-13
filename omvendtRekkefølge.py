def omvent_fil(inputFil, outputFil):
    innfil = open(inputFil, "r")
    utfil = open(outputFil, "w")
    list = []
    for linje in innfil:
        linjeS = linje.strip().split()
        list.append(linjeS)
    list.reverse()
    for linje in list:
        strLinje = " ".join(linje)
        utfil.write(strLinje)
        utfil.write("\n")
    innfil.close()
    utfil.close()


omvent_fil("onceUponATime.txt", "thereIsNoHappyEnding.txt")
