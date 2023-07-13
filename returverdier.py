#a)
#Hva returnerer hver funksjon?
#Sum funksjonen returnerer svaret på a+b
#Og hva skriver programmet ut?
#programmet skriver ut 5
def sum(a, b):
    return a + b

x = sum(2, 3)
print(x)

#b)
#Hva returnerer hver funksjon?
# funksjonen returnerer brukernavnet som personen skriver inn
#Og hva skriver programmet ut?
#programmet skriver ikke ut noe du får bare opp input teksten som du
#må fylle inn.
def hent_brukernavn():
    navn = input("Skriv inn brukernavn: ")
    return navn

x = hent_brukernavn()

#c)
#Hva returnerer hver funksjon?
#denne funksjonen retunerer ikke noe
#Og hva skriver programmet ut?
#Skriver ut None
def jeg_returnerer_ingenting():
    x = 1 + 2

x = jeg_returnerer_ingenting()

print(x)
