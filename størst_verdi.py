tall1 = int(input("Skriv inn et tall: "))
tall2 = int(input("Skriv inn et tall til: "))
tall3 = int(input("Skriv inn et siste tall: "))

# <>

if tall1 >= tall2 and tall1 >= tall3:
    print(tall1)
elif tall2 > tall1 and tall2 > tall3:
    print(tall2)
elif tall3 > tall2 and tall3 > tall1:
    print(tall3)

if tall1 == tall2 and tall3 == tall1:
    print(3)
elif tall1 == tall2:
    print(2)
elif tall2 == tall3 and tall1 == tall3:
    print(3)
elif tall2 == tall3:
    print(2)
