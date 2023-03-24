class Julkaisu:

    julkaisujen_maara = 0

    def __init__(self, etunimi, sukunimi, ammatti, teos,):
        Julkaisu.julkaisujen_maara = Julkaisu.julkaisujen_maara+ 1
        self.tekijännumero = Julkaisu.julkaisujen_maara
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.ammatti = ammatti
        self.teos = teos
    def tulosta_tiedot(self):
        print(f"{self.tekijännumero}: {self.etunimi} {self.sukunimi} {self.teos}")

Julkaisu = []
Julkaisu.append(Julkaisu("Aki", "Hyyppä"))
Julkaisu.append(Julkaisu("Rosa", "Liksom"))

for t in Julkaisu:
    t.tulosta_tiedot()