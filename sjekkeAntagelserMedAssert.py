#a)

liste = [2, 5, 5, 6, 3]
def to_stoerste_tall(liste):
    tall1 = 0
    tall2 = 0

    for tall in liste:
        if tall > tall1:
            tall1 = tall
        elif tall > tall2:
            tall2 = tall

    return [tall1, tall2]

assert len(to_stoerste_tall(liste)) == 2
assert to_stoerste_tall(liste) == [6, 5]

#b)
def format_navn(fullt_navn):
    for navn in fullt_navn.split():
        navn = navn[0].upper() + navn[1:]
    return navn

assert format_navn("erlend") == "Erlend"
