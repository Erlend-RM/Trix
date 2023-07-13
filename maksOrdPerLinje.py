teksten = "Hei, mitt navn er Erlend. Jeg er 27 år gammel og kommer fra Stavanger men bor i Oslo nå. "

def format_text(tekst, filnavn, maks_ord):
    fil = open(filnavn, "w")
    listeMedOrd = tekst.split()
    teller = 0
    for ord in listeMedOrd:
        teller += 1
        fil.write(ord + " ")
        if teller == maks_ord:
            teller = 0
            fil.write("\n")
    fil.close()



format_text(teksten, "maksOrdPerLinje.txt", 5)
