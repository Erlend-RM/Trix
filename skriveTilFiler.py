#a)
def skriv_dna(filnavn):
    fil = open(filnavn, "a")
    fil.write("0---o\n 0-o \n  0  \n o-0 \no---0\n")
    fil.close()

skriv_dna("dna.txt")
skriv_dna("dna.txt")
skriv_dna("dna.txt")
