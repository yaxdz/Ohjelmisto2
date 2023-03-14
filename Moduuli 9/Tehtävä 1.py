class Auto:
  def __int__(self,rekisteritunnus, huippunopeus, nopeusnyt, kuljettumatka):
      auto = Auto("ABC-123", 142, 0, 0)
auto = Auto()
auto.rekisteritunnus = "ABC-123"
auto.huippunopeus = 142
auto.nopeusnyt = 0
auto.kuljettumatka = 0
print(f"{auto.rekisteritunnus}, {auto.huippunopeus}, {auto.nopeusnyt}, {auto.kuljettumatka}")