navn = open("navn.txt")

liste = []

for linje in navn:
    liste.append(linje.strip())

navn.close()

print(liste)
