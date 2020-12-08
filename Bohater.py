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
        self.sakwa = 0

    def info(self):
        print("________" * 3)
        print("Imie:", self.imie, "\nKlasa:", self.specjalnosc)
        print("\nPunkty życia:", self.pkt_zycia, "/ 100",
              "\nStan pancerza:", self.stan_pancerz, "/ 5",
              "\nStan broni:", self.stan_bron, "/ 5",
              "\n\nSakwa:", self.sakwa, "monet"
              "\nIlość bryłek:", self.plecak.count(Przedmiot.brylka))
        print("________" * 3)

    def sprawdzplecak(self):
        if len(self.plecak) == 0:
            print("Plecak jest pusty.")
        else:
            print("________________________________")
            for lp, rzecz in enumerate(self.plecak):
                lp += 1
                print("Nr.", lp, rzecz, sep=" ")
            print("________________________________")

    def naprawaeq(self):
        print("Przed walka musze sprawdzic stan swojego oręża:",
              "\npancerz:", self.stan_pancerz, "|| broń:", self.stan_bron)
        print("#######" * 5)

        if self.stan_bron and self.stan_pancerz >= 5:               #SPRAWDZAM STAN BRONI I PANCERZA
            print("Ekwipunek w doskonałym stanie.")
        elif self.stan_bron < 5 or self.stan_pancerz < 5:
            print("Powinieneś naprawić ekwipunek. Narzedzia można znaleść u Kowala.")

        if Przedmiot.mlotek in self.plecak:                    #SPRAWDZA CZY W PLECAKU JEST MŁOTEK
            print("Naprawiam pancerz.")
            time.sleep(1)
            while self.stan_pancerz < 5:
                time.sleep(3)
                self.stan_pancerz += 1
                print("stan:", self.stan_pancerz)

                if self.stan_pancerz == 5:
                    print("#######" * 5)
                    print("Naprawiłem.")
                    self.plecak.remove(Przedmiot.mlotek)
        else:
            print("Nie mam wymaganych narzedzi do naprawy pancerza.")

        if Przedmiot.oselka in self.plecak:                         #SPRAWDZA CZY W PLECAKU JEST OSEŁKA
            print("Naprawiam i szlifuje broń.")
            time.sleep(1)
            while self.stan_bron < 5:
                time.sleep(3)
                self.stan_bron += 1
                print("stan:", self.stan_bron)

                if self.stan_bron == 5:
                    print("#######" * 5)
                    print("Naprawiłem.")
                    self.plecak.remove(Przedmiot.oselka)
        else:
            print("Nie mam wymaganych narzedzi do ostrzenia broni.")

    def polowanie(self):
        print("Czas ruszyć po jedzenie.")
        print("1: Las"
              "\n2: Bagna")

        zw_las = ["Sarna", "Królik", "Wilk"]
        zw_bagna = ["Kaczka", "Gęś", "Czapla"]
        zw_czesci = ["mięso", "skóra", "głowa", "wątroba"]
        m_miejsce = int(input("Wybierz gdzie chcesz sie udać: "))

        if m_miejsce == 1:
            print("Jestem w lesie: ...... szukam śladów zwierzyny.")
            time.sleep(3)
            zwierze = random.choice(zw_las)
            print("Znalazłem ślady: ", zwierze)
            szansa_zwierze = random.randint(0, 2)

            if szansa_zwierze == 2:                                     #SZANSA NA UPOLOWANIE.
                time.sleep(3)
                print("Udało mi sie upolować", zwierze)
                time.sleep(3)
                self.plecak.extend(random.sample(zw_czesci, k=2))        #DODAJE DO PLECAKA 2-ELEMENTY
                print("zebrałem:", self.plecak)
            else:
                time.sleep(2)
                print(zwierze, "spłoszone.", "\nNic nie upolowałem.")

        if m_miejsce == 2:
            print("Jestem na bagnach: ...... szukam śladów zwierzyny.")
            time.sleep(5)
            zwierze = random.choice(zw_bagna)
            szansa_zwierze = random.randint(0, 2)
            if szansa_zwierze == 2:                                     #SZANSA NA UPOLOWANIE.
                time.sleep(3)
                print("Udało mi sie upolować", zwierze)
                time.sleep(3)
                self.plecak.extend(random.sample(zw_czesci, k=2))       #DODAJE DO PLECAKA 2- ELEMENTY
                print("zebrałem:", self.plecak)
            else:
                time.sleep(2)
                print(zwierze, "spłoszone.", "\nNic nie upolowałem.")

    def ognisko(self):
        print("Do przygotowania 'potrawki', będziesz potrzebował 'mięsa' oraz 'wątroby'.")

        if 'mięso' and 'wątroba' in self.plecak:
            print("W plecaku sa składniki na 'potrawke'.")
            print("\nAby rozpalić ognisko będę potrzebował drewna.")

            if 'mięso' in self.plecak:
                self.plecak.remove('mięso')
            if 'wątroba' in self.plecak:
                self.plecak.remove('wątroba')

            self.plecak.append(Przedmiot.potrawka)

            drewno = 0
            time.sleep(2)
            print("Szukam drewna.")

            while drewno < 3:
                time.sleep(2)
                print("znalazłem 'kawałek drewna'.")
                time.sleep(1)
                drewno += 1
                self.plecak.append("kawałek drewna")

            print("Zebrałem :", self.plecak.count("kawałek drewna"),
                  "kawałki drewna \nTyle drewna powinno wystarczyć.")

            ognisko = 0
            print("Próbuje rozpalić ognisko.")

            while ognisko <= 3:
                time.sleep(3)
                print("cyk, cyk, cyk")
                ognisko += 1
            print("Ognisko płonie.")
            print("Otrzymujesz 'potrawkę'.")

            if 'kawałek drewna' in self.plecak:                 #SPRAWDZA KAWAŁEK DREWNA W PLECAKU, JAK JEST TO USUWA.
                while 'kawałek drewna' in self.plecak:
                    self.plecak.remove("kawałek drewna")
            else:
                print("Nie mam już drewna.")
        else:
            print("W plecaku nie ma skladników na 'potrawke'. Udaj sie na Polowanie.")

    def odpoczynek(self):
        print("Możesz troche odpocząc, przywróci ci to punkty życia.")

        if self.pkt_zycia == 100:
            print("Jesteś pełni sił.")
        else:
            pass

        odpoczynek = input("Chcesz odpocząc: (T/N): ")           #ODNOWIENIE ZYCIA (ODPOCZYNEK)

        if odpoczynek == str("T"):
            time.sleep(5)
            self.pkt_zycia = 100
            print("Jesteś w pełni zregenerowany: ", self.pkt_zycia, "/", self.pkt_zycia)
        else:
            print("Może innym razem.")

        if Przedmiot.potrawka in self.plecak:
            zjesc = input("Zjeść potrawkę, |życie = 100|. [T/N]?: ")        #ODNOWIENIE ZYCIA (POTRAWKA)
            if zjesc == str("T"):
                self.plecak.remove(Przedmiot.potrawka)
                self.pkt_zycia = 100
                print("Zycie Bohatera: ", self.pkt_zycia, "/", self.pkt_zycia)
            if zjesc == str("N"):
                print("Zostawiam na pozniej.")

    def gornictwo(self):
        rudy_metali = ["ruda Stali", " ruda Żelaza", "ruda Miedźi", "ruda Brązu", "ruda Niklu", "ruda Złota"]

        if Przedmiot.kilof in self.plecak:
            print("Szukam złóż: ")
            time.sleep(5)
            ruda = random.choice(rudy_metali)
            szansa = random.randint(0, 4)
            print(szansa, "moja szansa")
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
            print("Nie mam narzedzia do wydobycia. \nNarzedzia możesz znaleść u Kowala.")

    def wymiana(self):
        print("Za 30 monet możesz dostać: 1x 'bryłka złota \nlub wymienić 'bryłke złota' na 30 monet.")
        print("1.Wymiana monet na 'bryłke złota'")
        print("2.Wymiana 'bryłka złota' na monety")

        wybor = int(input("\nWybierz:"))
        if wybor == 1:
            if self.sakwa >= 1:
                self.plecak.append(Przedmiot.brylka)
                self.sakwa -= 1
                print("Otrzymujesz 'bryłka złota'")
                print("W sakiewce zostało ci: ", self.sakwa, "monet")

        if wybor == 2:
            if Przedmiot.brylka in self.plecak:
                self.plecak.remove(Przedmiot.brylka)
                self.sakwa += 30
                print("Do sakiewki dodano 30 monet.")
                print("W plecaku zostało ci: ", self.plecak.count(Przedmiot.brylka), "bryłek")
        else:
            print("Posiadasz:", self.sakwa, "monet", "\nIlość bryłek: ", self.plecak.count(Przedmiot.brylka))


class Wojownik(Bohater):
    def __init__(self, imie, specjalnosc, plecak, pkt_ataku, pkt_obrony, pkt_zycia):
        super().__init__(imie, specjalnosc, plecak, pkt_ataku, pkt_obrony, pkt_zycia)
        self.plecak = []
        self.stan_pancerz = random.randint(0, 2)
        self.stan_bron = random.randint(1, 3)
        self.sakwa = 0


class Lotrzyk(Bohater):
    def __init__(self, imie, specjalnosc, plecak, pkt_ataku, pkt_obrony, pkt_zycia):
        super().__init__(imie, specjalnosc, plecak, pkt_ataku, pkt_obrony, pkt_zycia)
        self.plecak = []
        self.stan_pancerz = random.randint(0, 3)
        self.stan_bron = random.randint(0, 4)
        self.sakwa = 0


class Driud(Bohater):
    def __init__(self, imie, specjalnosc, plecak, pkt_ataku, pkt_obrony, pkt_zycia):
        super().__init__(imie, specjalnosc, plecak, pkt_ataku, pkt_obrony, pkt_zycia)
        self.plecak = []
        self.stan_pancerz = random.randint(2, 3)
        self.stan_bron = random.randint(2, 3)
        self.sakwa = 0
