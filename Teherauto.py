from Auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij):
        super().__init__(rendszam, tipus, berleti_dij)

    def info(self):
        return f"Teherautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Bérleti díj: {self.berleti_dij} Ft"



t_auto1=Teherauto("XX-XX-99","Scania","25000")
t_auto2=Teherauto("XX-XX-88","Volvo","22000")
t_auto3=Teherauto("XX-XX-77","Ford","20000")