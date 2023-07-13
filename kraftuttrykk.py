#a)
def skriv_med_trykk(streng):
    kraftStreng = streng + "!"
    return kraftStreng

print(skriv_med_trykk("Hei hva heter du?"))

def kraft5():
    holderPa = True
    while holderPa:
        kraft = input("Gi meg et kraftuttrykk!: ")
        if kraft == "nei":
            return
        nyKraft = skriv_med_trykk(kraft)
        print(nyKraft)


kraft5()
