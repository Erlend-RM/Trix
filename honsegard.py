from random import choice

def honerIGarden():
    honer = int(input("Hvor mange Høner er det i gården: "))
    return honer

def revenKommerOgSoverBonen(honer):
    tjent = 0
    netter = 0
    while honer > 0:
        reven = choice(["ja", "nei"])
        bonden = choice(["ja", "nei"])
        print(f"Hvor mange høner bor i gården: {honer}")
        print(f"Kommer reven?\n{reven}")
        print(f"Sover bonden?\n{bonden}")
        netter += 1
        if netter == 5:
            break
        if reven == "ja" and bonden == "ja":
            honer = honer - 3
            print(f"Det bor nå {honer} på gården.")
        elif reven == "ja" and bonden == "nei":
            tjent = tjent + 190
            if tjent >= 570:
                break
            print(f"Det bor nå {honer} på gården. Bonden selger ett reveskinn, og tjener {tjent}kr.")
        else:
            print(f"Det bor nå {honer} på gården.")

honer = honerIGarden()
revenKommerOgSoverBonen(honer)
