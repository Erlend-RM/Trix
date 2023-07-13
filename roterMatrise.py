matriseEn = [
    [1,4,7],
    [2,5,8],
    [3,6,9]
    ]

def roterMatrise(matriseEn):

    matriseTo = []
    for i in range(len(matriseEn)):
        matriseTo.append([])
    for rad in matriseEn:
        teller = 0
        for nr in rad:
            matriseTo[teller].append(nr)
            teller += 1
    return matriseTo

print(roterMatrise(matriseEn))
