
#a)
def oppskrift_fra_sukker(tall):
    oppskrift = {}
    oppskrift["sukker"] = tall
    oppskrift["mel"] = tall * 2
    oppskrift["smør"] = tall * 3
    return oppskrift

#b)
def skriv_oppskrift(sukker, mel, smør):
    print("Oppskriften på kaken er:")
    print(f"Sukker: {sukker}g")
    print(f"Mel: {mel}g")
    print(f"Smør: {smør}g")


#c)
def bake_kaker():
    gram_sukker = int(input("Hvor mye sukker har du i gram: "))
    oppskrift_fra_sukker(gram_sukker)
    sukker = oppskrift_fra_sukker(gram_sukker)["sukker"]
    mel = oppskrift_fra_sukker(gram_sukker)["mel"]
    smør = oppskrift_fra_sukker(gram_sukker)["smør"]
    skriv_oppskrift(sukker, mel, smør)


bake_kaker()
