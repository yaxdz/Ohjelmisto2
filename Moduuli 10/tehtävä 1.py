class Hissi:
    def __init__(self, alin_kerros, ylimmäinen_kerros):
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylimmäinen_kerros = ylimmäinen_kerros

    def siirry_kerrokseen(self, kerros):
        if kerros > self.ylimmäinen_kerros:
            kerros = self.ylimmäinen_kerros
        elif kerros < self.alin_kerros:
            kerros = self.alin_kerros

        while self.kerros != kerros:
            if self.kerros < kerros:
                self.kerros_ylös()
            else:
                self.kerros_alas()

    def kerros_ylös(self):
        if self.kerros < self.ylimmäinen_kerros:
            self.kerros += 1
            print("Hissi on kerroksessa", self.kerros)

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print("Hissi on kerroksessa", self.kerros)

hissi = Hissi(1, 10)
hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(1)
