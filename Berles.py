class Berles:
    def __init__(self, auto, berles_datum):
        self.auto = auto
        self.berles_datum = berles_datum

    def __str__(self):
        return f"Bérlés - {self.auto.info()}, Dátum: {self.berles_datum.strftime('%Y-%m-%d')}"