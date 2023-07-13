streng1 = "eih"
streng2 = "hei"


def kal(streng1, streng2):
    returStreng = ""
    for bokstav in streng1:
        for bokstav2 in streng2:
            if bokstav == bokstav2:
                streng2 = streng2.replace(bokstav2, "", 1)
                returStreng += bokstav
                break
    return returStreng == streng1

print(kal(streng1, streng2))
