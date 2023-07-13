class Bilde:
    def __init__(self, hoyde, bredde, salgspris):
        self._hoeyde = hoyde
        self._bredde = bredde
        self._salgspris = salgspris

    def hentForhold(self):
        sideforhold = self._bredde / self._hoeyde
        return sideforhold

    def hentSalgspris(self):
        return self._salgspris

#1
#Hva skrives ut?
# sideforholdet skrives ut som vil bli 1,5
# Riktig!
#mittBilde = Bilde(10, 15, 20000)
#print(mittBilde.hentForhold())


#2
#Hva skrives ut?
# 2000
#Riktig!
#annetBilde = Bilde(160, 150, 10500)
#annetBilde = Bilde(160, 150, 2000)
#print(annetBilde.hentSalgspris())


#3
#Hva skrives ut?
#Forholdet til skrik og salgsprisen til monalisa
#Ikke helt riktig, De blir plusset sammen siden begge er integers
#monaLisa = Bilde(250, 150, 5000)
#skrik = Bilde(400, 400, 1000)

#print(skrik.hentForhold() + monaLisa.hentSalgspris())


#4
#Hva skrives ut?
# her vil man få feil melding mangler salgspris
#riktig!
#rhein2 = Bilde(73, 143)
#print(rhein2.hentSalgspris())

#5
#Hva skrives ut?
# og her vil det bli feil siden bredde og lengde er strings isteden for integers
#Riktig!
#sisteBilde = Bilde("100", "200", 4000)
#print(sisteBilde.hentForhold())

#6
#Hva skrives ut?
#her vil det printes 4500 men er ikke lagret som en variabel
#Riktig!
#print(Bilde(200, 200, 4500).hentSalgspris())
