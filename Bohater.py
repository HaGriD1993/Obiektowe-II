import random
import time
import Przedmiot


class Bohater:
    def __init__(self, imie, specjalnosc, plecak, pkt_ataku, pkt_obrony, pkt_zycia):
        self.imie = imie
        self.specjalnosc = specjalnosc
        self.plecak = plecak
        self.pkt_ataku = pkt_ataku
        self.pkt_obrony = pkt_obrony
        self.pkt_zycia = pkt_zycia
        self.stan_pancerz = 0
        self.stan_bron = 0
        self.sakwa = int(0)
        self.pkt_maxzycia = 100
        self.pkt_dosw = 0
        self.poziom = 1

    def mininfo(self):

        if self.pkt_zycia > self.pkt_maxzycia:   # ZEBY POSTAC NIE MIALA WIECEJ ZYCIA NIZ MOZE.
            self.pkt_zycia = self.pkt_maxzycia

        print("\nPoziom:", self.poziom)
        print("Punkty życia:", self.pkt_zycia, "/", self.pkt_maxzycia)
        print("Sakwa:", self.sakwa)

    def status(self):

        print("________" * 3)
        print("Imie:", self.imie, "\nKlasa:", self.specjalnosc,
              "\nPoziom: ", self.poziom, "\nDoświadczenie: ", self.pkt_dosw,
              "\nAtak: ", self.pkt_ataku)
        print("________" * 3)
        print("\nPunkty życia:", self.pkt_zycia, "/", self.pkt_maxzycia,
              "\nStan pancerza:", self.stan_pancerz, "/ 5",
              "\nStan broni:", self.stan_bron, "/ 5",
              "\n\nSakwa:", self.sakwa, "monet"
              "\nIlość bryłek:", self.plecak.count(Przedmiot.brylka))
        print("________" * 3)

    def awans(self):

        if self.pkt_dosw >= 10:     # AWANS NA KOLEJNY POZIOM PO UZYSKANIU 10 PKT DOSWIACZENIA
            self.poziom += 1        # POZIOM +1
            self.pkt_dosw -= 10     # DOWSWIADCZENIE - 10
            self.pkt_maxzycia += 5   # WZROST MAX ZYCIA O 5 PKT
            self.pkt_ataku += 2       # WZROST ATAKU O 2 PKT
            print("#################")
            print("Awansowałeś !!!\nNa poziom: ", self.poziom)
            print("#################")

    def stan_zdrowia(self):
        if self.pkt_zycia <= 20:  # SPRAWDZA PUNKTY ZYCIA JAK PONIZEJ 20PKT WYSWIETLI KOMUNIKAT
            print("######################")
            print("Masz mało życia. \nUdaj sie na odpoczynek.\n", self.pkt_zycia, "/", self.pkt_maxzycia)
            print("#######################")
            if self.pkt_zycia < 0:
                self.pkt_zycia = 0

    def sprawdzplecak(self):
        if len(self.plecak) == 0:                       # SPRAWDZA CZY W PLECAKU COS JEST
            print("Plecak jest pusty.")
        else:
            print("________________________________")   # ZWRACA ZAWARTOSC PLECAKA
            for lp, rzecz in enumerate(self.plecak):
                lp += 1
                print("Nr.", lp, rzecz, sep=" ")
            print("________________________________")

    def naprawaeq(self):
        print("Przed walka musze sprawdzic stan swojego oręża:",
              "\npancerz:", self.stan_pancerz, "|| broń:", self.stan_bron)
        print("#######" * 5)

        if self.stan_bron and self.stan_pancerz >= 5:              # SPRAWDZA STAN BRONI I PANCERZA
            print("Ekwipunek w doskonałym stanie.")
        elif self.stan_bron < 5 or self.stan_pancerz < 5:
            print("Powinieneś naprawić ekwipunek. Narzedzia można znaleść u Kowala.")

        if Przedmiot.mlotek in self.plecak:                     # SPRAWDZA CZY W PLECAKU JEST MŁOTEK
            print("Naprawiam pancerz.")
            time.sleep(1)
            while self.stan_pancerz < 5:                        # PODNOSI STAN PANCERZA DO 5
                time.sleep(3)
                self.stan_pancerz += 1
                print("stan:", self.stan_pancerz)

                if self.stan_pancerz == 5:
                    print("#######" * 5)
                    print("Naprawiłem.")
                    self.plecak.remove(Przedmiot.mlotek)            # USUWA MLOTEK Z PLECAKA
        else:
            print("Nie mam wymaganych narzedzi do naprawy pancerza.")

        if Przedmiot.oselka in self.plecak:                         # SPRAWDZA CZY W PLECAKU JEST OSEŁKA
            print("Naprawiam i szlifuje broń.")
            time.sleep(1)
            while self.stan_bron < 5:                               # PODNOSCI STAN BRONI DO 5
                time.sleep(3)
                self.stan_bron += 1
                print("stan:", self.stan_bron)

                if self.stan_bron == 5:
                    print("#######" * 5)
                    print("Naprawiłem.")
                    self.plecak.remove(Przedmiot.oselka)        # USUWA OSEŁKE Z PLECAKA
        else:
            print("Nie mam wymaganych narzedzi do ostrzenia broni.")

    def polowanie(self):
        print("Czas ruszyć po jedzenie.")
        print("1: Las"
              "\n2: Bagna")

        zw_las = ["Sarna", "Królik", "Wilk"]
        zw_bagna = ["Kaczka", "Gęś", "Czapla"]
        zw_czesci = []

        for i in range(1):
            zw_czesci.append(Przedmiot.mieso)
            zw_czesci.append(Przedmiot.skora)
            zw_czesci.append(Przedmiot.watroba)
            zw_czesci.append(Przedmiot.jelita)


        m_miejsce = int(input("Wybierz gdzie chcesz sie udać: "))

        if m_miejsce == 1:
            print("Jestem w lesie: ...... szukam śladów zwierzyny.")
            time.sleep(3)
            zwierze = random.choice(zw_las)
            print("Znalazłem ślady: ", zwierze)
            szansa_zwierze = random.randint(0, 2)

            if szansa_zwierze == 2:                                     # SZANSA NA UPOLOWANIE.
                time.sleep(3)
                print("Udało mi sie upolować", zwierze)
                time.sleep(3)
                self.plecak.append(random.choice(zw_czesci))            # DODAJE DO PLECAKA 2 ELEMENTY
                self.plecak.append(random.choice(zw_czesci))

            else:
                time.sleep(2)
                print(zwierze, "uciekło.", "\nNic nie upolowałem.")

        if m_miejsce == 2:
            print("Jestem na bagnach: ...... szukam śladów zwierzyny.")
            time.sleep(3)
            zwierze = random.choice(zw_bagna)
            szansa_zwierze = random.randint(0, 2)

            if szansa_zwierze == 2:                                     # SZANSA NA UPOLOWANIE.
                time.sleep(3)
                print("Udało mi sie upolować", zwierze)
                time.sleep(3)
                self.plecak.append(random.choice(zw_czesci))            # DODAJE DO PLECAKA 2 ELEMENTY
                self.plecak.append(random.choice(zw_czesci))

            else:
                time.sleep(2)
                print("Zwierze uciekło.")

    def ognisko(self):
        print("Do przygotowania 'potrawki', będziesz potrzebował 'mięsa' oraz 'wątroby'.")

        if Przedmiot.mieso and Przedmiot.watroba in self.plecak:     # SPRAWDZA WARUNEK
            print("W plecaku sa składniki na 'potrawke'.")
            print("\nAby rozpalić ognisko będę potrzebował drewna.")

            if Przedmiot.mieso in self.plecak:      # JAK PRZEDMIOT JEST TO USUWA
                self.plecak.remove(Przedmiot.mieso)
            if Przedmiot.watroba in self.plecak:
                self.plecak.remove(Przedmiot.watroba)

            self.plecak.append(Przedmiot.potrawka)   # DODAJE PRZEDMIOT DO PLECAKA

            drewno = 0
            time.sleep(2)
            print("Szukam drewna.")

            while drewno < 3:    # DODAJE PRZEDMIOT DOPUKI NIE BEDZIE MIAL 3
                time.sleep(2)
                print("znalazłem 'kawałek drewna'.")
                time.sleep(1)
                drewno += 1
                self.plecak.append(Przedmiot.patyki)

            print("Zebrałem :", self.plecak.count(Przedmiot.patyki),
                  "kawałki drewna \nTyle drewna powinno wystarczyć.")

            ognisko = 0
            print("Próbuje rozpalić ognisko.")

            while ognisko <= 3:
                time.sleep(3)
                print("cyk, cyk, cyk")
                ognisko += 1
            print("Ognisko płonie.")
            print("Otrzymujesz 'potrawkę'.")

            if Przedmiot.patyki in self.plecak:                 # SPRAWDZA KAWAŁEK DREWNA W PLECAKU, JAK JEST TO USUWA.
                while Przedmiot.patyki in self.plecak:
                    self.plecak.remove(Przedmiot.patyki)

            else:
                print("Nie mam już drewna.")

        else:
            print("W plecaku nie ma skladników na 'potrawke'. Udaj sie na Polowanie.")

    def odpoczynek(self):
        print("Możesz troche odpocząc, przywróci ci to punkty życia.")

        if self.pkt_zycia == self.pkt_maxzycia:
            print("Jesteś pełni sił.")
        else:
            pass

        odpoczynek = input("Chcesz odpocząc: (T/N): ")           # ODNOWIENIE ZYCIA (ODPOCZYNEK)

        if odpoczynek == str("T"):
            print("Odpoczywasz.")
            self.pkt_zycia += 50
            for i in range(5):
                time.sleep(1)
                print("życie +10")

        else:
            print("Może innym razem.")

        if Przedmiot.potrawka in self.plecak:
            zjesc = input("Zjeść potrawkę, |życie + 80|. [T/N]?: ")        # ODNOWIENIE ZYCIA (POTRAWKA)

            if zjesc == str("T"):
                self.plecak.remove(Przedmiot.potrawka)
                self.pkt_zycia += 80
                print("życie +80")

            if zjesc == str("N"):
                print("Zostawiam na pozniej.")

    def gornictwo(self):
        rudy_metali = []

        for i in range(1):                              # DODANIE DO LISTY
            rudy_metali.append(Przedmiot.ruda_zelaza)
            rudy_metali.append(Przedmiot.ruda_miedzi)
            rudy_metali.append(Przedmiot.ruda_brazu)
            rudy_metali.append(Przedmiot.ruda_niklu)
            rudy_metali.append(Przedmiot.ruda_zlota)
            rudy_metali.append(Przedmiot.ruda_srebra)

        if Przedmiot.kilof in self.plecak:              # SPRAWDZA CZY PRZEDMIOT JEST W PLECAKU
            print("\nSzukam złóż: ")
            time.sleep(5)
            ruda = random.choice(rudy_metali)           # WYBIERA DOWOLNA WARTOSC Z LISTY
            szansa = random.randint(0, 4)
            time.sleep(1)
            print("Zanalazłem:", ruda)

            if szansa == 2:
                print("Wydobyłem: ", ruda)
                time.sleep(2)
                self.plecak.append(ruda)

            elif szansa == 1:
                print("Wydobyłem: ", ruda)
                time.sleep(2)
                self.plecak.append(ruda)
                self.plecak.append(Przedmiot.brylka)

            elif szansa == 3:
                print("Wydobyłem: ", ruda)
                time.sleep(2)
                print("udało sie jeszcze wydobyć: 'ołów'")
                self.plecak.append(ruda)
                self.plecak.append(Przedmiot.olow)

            else:
                time.sleep(2)
                print("Nic nie wydobyłem.")

        else:
            print("Potrzebuje kilof. Możesz go znaleść u Kowala.")

    def wymiana(self):

        print("\n1. Monety ===> 'bryłka złota'.")
        print("2. Monety <=== 'bryłka złota'.")

        wybor = int(input("\nWybierz: "))

        if wybor == 1:

            if self.sakwa >= 30:                       # 30 LUB WIECEJ MONET W SAKWIE
                self.plecak.append(Przedmiot.brylka)   # DODAJE BRYlKE
                self.sakwa -= 30                       # USUWA 30 MONET
                print("Otrzymujesz 'bryłka złota'")
                print("W sakiewce zostało ci: ", self.sakwa, "monet")

        if wybor == 2:

            if Przedmiot.brylka in self.plecak:         # JAK JEST BRYLKA W PLECAKU
                self.plecak.remove(Przedmiot.brylka)    # USUWA BRYLKE
                self.sakwa += 30                        # DO SAKWY PLUS 30 MONET
                print("Do sakiewki dodano 30 monet.")
                print("W plecaku zostało ci: ", self.plecak.count(Przedmiot.brylka), "bryłek")


class Wojownik(Bohater):
    def __init__(self, imie, specjalnosc, plecak, pkt_ataku, pkt_obrony, pkt_zycia):
        super().__init__(imie, specjalnosc, plecak, pkt_ataku, pkt_obrony, pkt_zycia)
        self.plecak = []
        self.stan_pancerz = random.randint(0, 2)
        self.stan_bron = random.randint(1, 3)
        self.sakwa = int(17)
        self.pkt_dosw = 0


class Lotrzyk(Bohater):
    def __init__(self, imie, specjalnosc, plecak, pkt_ataku, pkt_obrony, pkt_zycia):
        super().__init__(imie, specjalnosc, plecak, pkt_ataku, pkt_obrony, pkt_zycia)
        self.plecak = []
        self.stan_pancerz = random.randint(0, 3)
        self.stan_bron = random.randint(0, 4)
        self.sakwa = int(25)
        self.pkt_dosw = 0


class Driud(Bohater):
    def __init__(self, imie, specjalnosc, plecak, pkt_ataku, pkt_obrony, pkt_zycia):
        super().__init__(imie, specjalnosc, plecak, pkt_ataku, pkt_obrony, pkt_zycia)
        self.plecak = []
        self.stan_pancerz = random.randint(2, 3)
        self.stan_bron = random.randint(2, 3)
        self.sakwa = int(22)
        self.pkt_dosw = 0
