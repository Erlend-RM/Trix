#a)
#Hva skjer når vi forsøker å kjøre følgende pragam?
#En tekst!
#En tekst!
#10
"""
a = "En tekst!"
def prosedyre_en(parameter):
    parameter = parameter + "12"

print(a)
prosedyre_en(a)
print(a)

b = 10
print(b)

"""
#b)
#Hva skjer når vi forsøker å kjøre følgende pragam?
#Feil, b er i lokal variabel og ikke global
"""
def prosedyre_to():
    b = b + 10

prosedyre_to()
print(b)
"""

#c)
#Hva skjer når vi forsøker å kjøre følgende pragam?
#hei
#heiverden
c = "hei"
print(c)

def funksjon_en(parameter):
    parameter = parameter + "verden"
    return parameter

print(funksjon_en(c))

#d)
#Hva betyr begrepet "global variabel"?
#Betyr at et variabel er mulig å bruke "over alt"
#Hvilken av de foregående øvelsene (a/b/c) bruker global variabel?
#a og c bruker global variabel
#Når bør du bruke global variabel i IN1000? Forklar svaret ditt.
#Aldri
