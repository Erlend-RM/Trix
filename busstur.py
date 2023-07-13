def busstur():
    buss = 0
    stasjon1 = int(input("Stasjon 1! Hvor mange går på bussen? "))
    buss += stasjon1
    if buss == 30:
        print("Bussen er full.")
    elif buss > 30:
        print(f"Bussen er full. {buss-30} må gå til fots.")
    stasjon2 = int(input("Stasjon 2! Hvor mange går på bussen? "))
    buss += stasjon2
    if buss == 30:
        print("Bussen er full. ")
    elif buss > 30:
        print(f"Bussen er full. {buss-30} må gå til fots.")
    stasjon3 = int(input("Stasjon 3! Hvor mange går på bussen? "))
    buss += stasjon3
    if buss == 30:
        print("Bussen er full. ")
    elif buss > 30:
        print(f"Bussen er full. {buss-30} må gå til fots.")

busstur()
