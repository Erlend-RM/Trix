oliste = []

for i in range(5):
    oliste.append("o")

print(oliste)

stjerneliste = []

for i in range(5):
    stjerneliste.append("*")

print(stjerneliste)

rutenett = []
rutenett.append(oliste)
rutenett.append(stjerneliste)
rutenett.append(oliste)

print(rutenett)
"""
print(rutenett[0])
print(rutenett[1])
print(rutenett[2])
"""

for i in rutenett:
    print(i)
