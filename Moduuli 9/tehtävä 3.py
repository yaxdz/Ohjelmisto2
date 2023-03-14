class Auto:
    def __init__(self, huippunopeus):
        self.nopeus = 0
        self.huippunopeus = huippunopeus
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus < 0:
            self.nopeus = 0
        elif uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus2
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tuntimaara):
        matka = self.nopeus * tuntimaara
        self.kuljettu_matka += matka

    def __str__(self):
        return "Auton nopeus: {} km/h, kuljettu matka: {} km".format(self.nopeus, self.kuljettu_matka)

auto = Auto(200)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

auto.kulje(1.5)

print(auto)

auto.kiihdyta(-200)

print(auto)
