#1)
handleliste = ["salat", "fisk", "melk", "brod"]

prisListe = [
    {"salat" : 12, "fisk" : 99, "melk" : 12, "brod" :12},
    {"salat" : 22, "fisk" : 60, "melk" : 18, "brod" :21},
    {"salat" : 8, "fisk" : 120, "melk" : 10, "brod" :19},
    {"salat" : 18, "fisk" : 40, "melk" : 30, "brod" :59},
    {"salat" : 15, "fisk" : 200, "melk" : 40, "brod" :9},
    ]

butikker = ["Rema1000", "Meny", "Kiwi","Spar", "Joker"]



def finnButikk(handleliste, butikker, prisListe):
    minstePris = 2000
    butikkIndeks = 0
    teller = 0
    for butikk in prisListe:
        prisPaaButikk = 0
        for vare in butikk:
            if (vare in handleliste):
                prisPaaButikk += butikk[vare]
        if (prisPaaButikk < minstePris):
            minstePris = prisPaaButikk
            butikkIndeks = teller
        teller += 1
    return butikker[butikkIndeks]


print(finnButikk(handleliste, butikker, prisListe))
