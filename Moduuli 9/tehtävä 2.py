class Auto:
    class Auto:
        def __int__(self, rekisteritunnus, huippunopeus, nopeusnyt, kuljettumatka):
            auto = Auto("ABC-123", 142, 0, 0)

    auto = Auto()
    auto.rekisteritunnus = "ABC-123"
    auto.huippunopeus = 142
    auto.nopeusnyt = 0
    auto.kuljettumatka = 0
    print(f"{auto.rekisteritunnus}, {auto.huippunopeus}, {auto.nopeusnyt}, {auto.kuljettumatka}")


    def __init__(self, huippunopeus):
        self.nopeus = 0
        self.huippunopeus = huippunopeus

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus < 0:
            self.nopeus = 0
        elif uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = uusi_nopeus

auto = Auto(200)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

print("Auton nopeus:", auto.nopeus)

auto.kiihdyta(-200)

print("Uusi nopeus hätäjarrutuksen jälkeen:", auto.nopeus)
