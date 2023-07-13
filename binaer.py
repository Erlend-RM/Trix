tallet = int(input("Skriv inn et tall: "))

while tallet != 0:
    tall = tallet % 2
    print(tall)
    tallet = tallet // 2
