

class Przedmiot:                         # klasa bazowa dla przedmiotow
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __str__(self):                  # zwraca tylko nazwe
        return self.nazwa


class Zwykly(Przedmiot):                # klasa dziedziczy po bazowej przedmiot
    def __init__(self, nazwa, cena):
        super().__init__(nazwa)         # odowlanie do bazowej klasy przez 'super().'
        self.cena = cena

    def __str__(self):                 # zwraca nazwe + pozostala czesc
        return super().__str__() + " |cena: " + str(self.cena) + " monet."

    def kupno(self):            # funkcja kupa przedmiotu
        cena = self.cena
        cena = int(cena)        # zmiana na int-a zeby mozna bylo odjac wartosci.

        if cena == 0:
            cena = 1
        return cena

    def sprzedaz(self):        # funkcja sprzedazy przedmiotu za 1/4 ceny
        cena = self.cena
        cena = int(cena) / 4

        if cena <= 0:
            cena = 1                 # minimalna cena to 1
        return cena.__round__(0)     # zaokraglenie liczby


class Bron(Zwykly):                  # dziedziczenie po klasie
    def __init__(self, nazwa, cena, obrazenia):
        super().__init__(nazwa, cena)
        self.obrazenia = obrazenia

    def __str__(self):             # zwraca nazwe i cene + pozostala czesc
        return super().__str__() + " |obrażenia: +" + str(self.obrazenia)


class Pancerz(Zwykly):
    def __init__(self, nazwa, cena, blok):
        super().__init__(nazwa, cena)
        self.blok = blok

    def __str__(self):             # zwraca nazwe i cene + pozostala czesc
        return super().__str__() + " |blok: +" + str(self.blok)


class Metal(Zwykly):
    def __init(self, nazwa, cena):
        super().__init__(nazwa, cena)

    def __str__(self):
        return self.nazwa + " (minerał)"


class Sztaba(Zwykly):
    def __init(self, nazwa, cena):
        super().__init__(nazwa, cena)

    def __str__(self):
        return self.nazwa + " (materiał rzemieślniczy)"


class Surowiec(Zwykly):
    def __init__(self, nazwa, cena):
        super().__init__(nazwa, cena)

    def __str__(self):
        return self.nazwa + " (surowiec źielarski)"


class Mikstura(Zwykly):
    def __init__(self, nazwa, cena, moc, rodzaj):
        super().__init__(nazwa, cena)
        self.moc = moc
        self.rodzaj = rodzaj

    def __str__(self):
        return self.nazwa + " |" + str(self.moc) + " %| " + str(self.rodzaj)


# LISTA PRZEDMIOTOW:
brylka = Zwykly("bryłka złota", 30)
kilof = Zwykly("kilof", 50)
mlotek = Zwykly("młotek kowalski", 40)
oselka = Zwykly("osełka", 40)
potrawka = Zwykly("potrawka", 100)
olow = Zwykly("ołów", 15)
korona = Zwykly("Korona Lilith", 170)
mieso = Zwykly("mięso", 2)
skora = Zwykly("skóra", 3)
watroba = Zwykly("wątroba", 3)
jelita = Zwykly("jelita", 2)

patyki = Przedmiot("kawałek drewna")

# LISTA PRZEDMIOTOW U KOWALA BRON |PANCERZ |HEŁM |TARCZA:
miecz_zwykly = Bron("Zwykły miecz", 380, 4)
miecz_zardzewialy = Bron("Zardzewiały miecz", 85, 1)
miecz_doskonaly = Bron("Doskonały miecz", 620, 6)
miecz_stalowy = Bron("Stalowy miecz", 190, 2)
miecz_zelazny = Bron("Żelazny miecz", 240, 3)

pancerz_sierzanta = Pancerz("Pancerz sierżanta", 150, 1)
pancerz_straznika = Pancerz("Pancerz strażnika", 230, 2)
pancerz_oficera = Pancerz("Pancerz oficera", 350, 4)

helm_skorzany = Pancerz("Skórzany hełm", 150, 1)
helm_stalowy = Pancerz("Stalowy hełm", 210, 2)
helm_zelazny = Pancerz("Żelazny hełm", 340, 3)
helm_rogaty = Pancerz("Rogaty hełm", 500, 4)

tarcza_stalowa = Pancerz("Stalowa tarcza", 140, 2)
tarcza_drewniana = Pancerz("Drewniana tarcza", 30, 1)
tarcza_zelazna = Pancerz("Żelazna tarcza", 210, 3)
tarcza_rogata = Pancerz("Rogata tarcza", 380, 4)

# SZTABKI I RUDY
ruda_zelaza = Metal("ruda żelaza", 3)
ruda_miedzi = Metal("ruda miedzi", 2)
ruda_brazu = Metal("ruda brązu", 2)
ruda_niklu = Metal("ruda niklu", 3)
ruda_zlota = Metal("ruda złota", 8)
ruda_srebra = Metal("ruda srebra", 5)

sz_zelaza = Sztaba("sztabka żelaza", 12)
sz_miedzi = Sztaba("sztabka miedzi", 8)
sz_brazu = Sztaba("sztabka brązu", 8)
sz_niklu = Sztaba("sztabka niklu", 12)
sz_zlota = Sztaba("sztabka złota", 30)
sz_srebra = Sztaba("sztabka srebra", 19)

# ZIOŁA I MIKSTURY
czerw_ziele = Surowiec("Czerwone źiele", 7)
nieb_ziele = Surowiec("Niebieskie źiele", 4)
korz_piem = Surowiec("Korzeń piementu", 3)
kwi_drug = Surowiec("Kwiat drugrotu", 5)
bag_ziele = Surowiec("Bagienne źiele", 6)
kulczyba = Surowiec("Kulczyba wronie oko", 10)
tr_ziele = Surowiec("Trójkolorowe źiele", 8)
jask_ziele = Surowiec("Jaskółcze źiele", 8)
ziar_spor = Surowiec("Ziarna sporyszu", 6)

m_lecze = Mikstura("Mała mikstura leczenia", 65, 23, "lęcząca")
d_lecze = Mikstura("Duża mikstura leczenia", 150, 35, "lęcząca")
m_pd = Mikstura("Mikstura 'Powrót do korzeni'", 98, 40, "regenerująca")
nap_ut = Mikstura("Napar z utopca", 40, 20, "regenerująca")
strych = Mikstura("Strychnina", 85, 15, "trucizna")
botul = Mikstura("Botulina", 55, 5, "trucizna")

