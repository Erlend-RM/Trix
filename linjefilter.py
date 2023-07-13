def filter(inputFilnavn, outputFilnavn):
    liste = []
    fil1 = open(inputFilnavn)
    fil2 = open(outputFilnavn, "w")
    for linje in fil1:
        linjeSplit = linje.strip().split(",")
        liste.append(linjeSplit)
        if "NA" not in linje:
            fil2.write(linje)
    fil1.close()
    fil2.close()

filter("linjefilter.txt", "linjefilterUt.txt")
