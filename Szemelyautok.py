from Auto import Auto

class Szemelyautok(Auto):
    def __init__(self, rendszam, tipus, berleti_dij):
        super().__init__(rendszam, tipus, berleti_dij)

    def info(self):
        return f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Bérleti díj {self.berleti_dij} Ft"




sz_auto1 = Szemelyautok("AA-BB-12", "Audi", "10000")
sz_auto2 = Szemelyautok("FF-CC-10", "BMW", "12000")
sz_auto3 = Szemelyautok("XX-YY-00", "Mercedes", "15000")





