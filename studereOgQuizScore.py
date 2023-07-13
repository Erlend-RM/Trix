class Student:

    def __init__(self, navn, poeng, antallDeltatt):
        self._navn = navn
        self._poeng = poeng
        self._antdel = antallDeltatt


    def leggTilQuizScore(self, nyepoeng):
        self._poeng += nyepoeng
        self._antdel += 1
        return self._poeng, self._antdel


    def gjennomsnittligScore(self):
        gjennomsnittlig = self._poeng / self._antdel
        return f"Din gjennomsnittlige score {self._navn} er {gjennomsnittlig:.2f}."

    def skrivUtScore(self):
        return f"Din score {self._navn} er {self._poeng}"

def hovedprogram():
    joakim = Student("Joakim", 50, 4)
    kristin = Student("Kristin", 15, 1)
    dag = Student("Dag", 34, 3)
    joakim.leggTilQuizScore(5)
    joakim.leggTilQuizScore(13)
    kristin.leggTilQuizScore(15)
    kristin.leggTilQuizScore(12)
    dag.leggTilQuizScore(10)
    dag.leggTilQuizScore(14)
    print(joakim.skrivUtScore())
    print(kristin.skrivUtScore())
    print(dag.skrivUtScore())
    print(joakim.gjennomsnittligScore())
    print(kristin.gjennomsnittligScore())
    print(dag.gjennomsnittligScore())


hovedprogram()
