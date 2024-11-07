from Berles import Berles
from datetime import datetime
from datetime import date
class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def auto_hozzaadasa(self, auto):
        self.autok.append(auto)

    def autok_listazasa(self):
        for auto in self.autok:
            print(auto.info())

    def auto_berlese(self, rendszam, datum_str):
        try:
            berles_datum = datetime.strptime(datum_str, "%Y-%m-%d")

            if berles_datum < datetime.today():
                raise Exception("Múltbéli dátum!!!!!")

        except:
            return "Hibás dátumformátum, vagy múltbéli dátum. Használd az ÉÉÉÉ-HH-NN formátumot."

        auto = next((a for a in self.autok if a.rendszam == rendszam), None)
        foglalt_datumok = []
        for b in self.berlesek:
            if auto == b.auto:
                foglalt_datumok.append(b.berles_datum)
        if auto and berles_datum not in foglalt_datumok:
            berles = Berles(auto, berles_datum)
            self.berlesek.append(berles)
            return f"A bérlés sikeres a következő dátumra: {berles_datum.strftime('%Y-%m-%d')}. Ár: {auto.berleti_dij} Ft"
        else:
            return "Az autó nem elérhető vagy már bérlés alatt van."

    def berles_lemondasa(self, rendszam, datum_str):
        try:
            berles_datum = datetime.strptime(datum_str, "%Y-%m-%d")
        except ValueError:
            return "Hibás dátumformátum. Használd az ÉÉÉÉ-HH-NN formátumot."
        berles = next((b for b in self.berlesek if b.auto.rendszam == rendszam and b.berles_datum ==berles_datum), None)
        if berles:
            self.berlesek.remove(berles)
            berles.auto.berelt = False
            return "A bérlés lemondása sikeres."
        else:
            return "A bérlés nem található."

    def berlesek_listazasa(self):
        if not self.berlesek:
            print("Nincs aktuális bérlés.")
        for berles in self.berlesek:
            print(berles)

