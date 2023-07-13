dyr = ["katt", "hund", "hest"]
mat = ["brokkoli", "potet", "pølse"]

kombinert_pluss = dyr + mat
kombinert_pluss_liste = [dyr + mat]
kombinert_komma_liste = [dyr, mat]

#a)
# kombinert_pluss = ["katt", "hund", "hest", "brokkoli", "potet", "pølse"]
# kombinert_pluss_liste = [["katt", "hund", "hest", "brokkoli", "potet", "pølse"]]
# kombinert_komma_liste = [["katt", "hund", "hest"], ["brokkoli", "potet", "pølse"]]
# den første er kun slått sammen, den neste slås sammen inni en annen liste (så er nøstet)
# og den siste er nøstet med vær for seg
print(kombinert_pluss)
print(kombinert_pluss_liste)
print(kombinert_komma_liste)


#b)
# kombinert_pluss[0] = "katt"
# kombinert_pluss_liste[0] = ["katt", "hund", "hest", "brokkoli", "potet", "pølse"]
# kombinert_komma_liste[0] = ["katt", "hund", "hest"]
print(kombinert_pluss[0])
print(kombinert_pluss_liste[0])
print(kombinert_komma_liste[0])

#c)
# kombinert_pluss[0][1] = "a"
# kombinert_pluss_liste[0][1] = "hund"
# kombinert_komma_liste[0][1] = "hund"
print(kombinert_pluss[0][1])
print(kombinert_pluss_liste[0][1])
print(kombinert_komma_liste[0][1])
