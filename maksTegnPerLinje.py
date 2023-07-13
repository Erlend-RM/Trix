teksten = "Hei, mitt navn er Erlend. Jeg er 27 år gammel og kommer fra Stavanger men bor i Oslo nå. "

def format_text(tekst, filnavn, maks_tegn):
    fil = open(filnavn, "w")
    listeMedOrd = tekst.split()
    teller = 0
    for ord in listeMedOrd:
        for bokstav in ord:
            teller += 1
            fil.write(bokstav + " ")
            if teller == maks_tegn:
                teller = 0
                fil.write("\n")
    fil.close()



format_text(teksten, "maksTegnPerLinje.txt", 5)
