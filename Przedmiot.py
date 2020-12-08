

class Przedmiot:                         #klasa bazowa dla przedmiotow
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __str__(self):                  #zwraca tylko nazwe
        return self.nazwa


class Zwykly(Przedmiot):                #klasa dziedziczy po bazowej przedmiot
    def __init__(self, nazwa, cena):
        super().__init__(nazwa)         #odowlanie do bazowej klasy przez 'super().'
        self.cena = cena

    def __str__(self):                 # zwraca nazwe + pozostala czesc
        return super().__str__() + " |cena: " + str(self.cena) + " monet."

    def sprzedaz(self):         #funkcja do sprzedazy ale tylko przedmiotow co maja cene.
        cena = self.cena
        cena = int(cena)        #zmiana na int-a zeby mozna bylo odjac wartosci.

        if cena == 0:
            cena = 1
        return cena

    def kupno(self):
        cena = self.cena
        cena = int(cena) / 2

        if cena == 0:
            cena = 1
        return cena


class Bron(Zwykly):                  #dziedziczenie po klasie
    def __init__(self, nazwa, cena, obrazenia):
        super().__init__(nazwa, cena)
        self.obrazenia = obrazenia

    def __str__(self):             #zwraca nazwe + pozostala czesc
        return super().__str__() + " |obrażenia: +" + str(self.obrazenia)


class Pancerz(Zwykly):
    def __init__(self, nazwa, cena, blok):
        super().__init__(nazwa, cena)
        self.blok = blok

    def __str__(self):             #zwraca nazwe + pozostala czesc
        return super().__str__() + " |blok: +" + str(self.blok)


    #LISTA PRZEDMIOTOW:
brylka = Zwykly("bryłka złota", 30)

kilof = Przedmiot("kilof")
mlotek = Przedmiot("młotek kowalski")
oselka = Przedmiot("osełka")
potrawka = Przedmiot("potrawka")
olow = Przedmiot("ołów")

#LISTA BRON |PANCERZ |HEŁM |TARCZA:
miecz_zwykly = Bron("Zwykły miecz", 250, 4)
miecz_zardzewialy = Bron("Zardzewiały miecz", 140, 2)
miecz_doskonaly = Bron("Doskonały miecz", 450, 6)

pancerz_sierzanta = Pancerz("Pancerz sierżanta", 100, 1)
pancerz_straznika = Pancerz("Pancerz strażnika", 200, 2)
pancerz_oficera = Pancerz("Pancerz oficera", 350, 4)

helm_skorzany = Pancerz("Skórzany hełm", 150, 1)
helm_stalowy = Pancerz("Stalowy hełm", 210, 2)
helm_zelazny = Pancerz("Żelazny hełm", 340, 3)
helm_rogaty = Pancerz("Rogaty hełm", 500, 4)

tarcza_stalowa = Pancerz("Stalowa tarcza", 140, 2)
tarcza_drewniana = Pancerz("Drewniana tarcza", 30, 1)
tarcza_zelazna = Pancerz("Żelazna tarcza", 210, 3)
tarcza_rogata = Pancerz("Rogata tarcza", 380, 4)



