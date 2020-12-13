import random
import time
import Bohater
import Przedmiot


class Kowal:
    def __init__(self):
        self.imie = "Ryszard"
        self.wiek = 52
        self.specjanosc = "Kowal"

    def info(self):
        print("\nWitaj nazywam się: " + self.imie, ",jestem", self.specjanosc+"em")   #PRZEDSTAWIA SIE

    def skladniki(self, mojbohater: Bohater.Bohater):
        metale = []

        for i in range(1):                                  # DODANIE DO LISTY
            metale.append(Przedmiot.ruda_zelaza)
            metale.append(Przedmiot.ruda_miedzi)
            metale.append(Przedmiot.ruda_brazu)
            metale.append(Przedmiot.ruda_niklu)
            metale.append(Przedmiot.ruda_zlota)
            metale.append(Przedmiot.ruda_srebra)

        wybor = input("Za 'bryłke złota' mogę dać ci kilka róznych rud. (T/N): ")

        if wybor == str("T"):

            if Przedmiot.brylka in mojbohater.plecak:        # SPRAWDZA CZY JEST BRYLKA
                mojbohater.plecak.remove(Przedmiot.brylka)

                print("Otrzymujesz: ")

                for i in range(3):                            # DO PLECAKA DODAJE 3 ELEMENTY Z LISTY
                    time.sleep(2)
                    wyb_metale = random.choice(metale)
                    print(wyb_metale.__str__())
                    mojbohater.plecak.append(wyb_metale)

            else:
                print("Nie masz ani jednej 'bryłki złota', wróc do mnie jak bedziesz miał.")

        else:
            print("Wróc jak zmienisz zdanie.")

    def przetapianie(self, mojbohater: Bohater.Bohater):

        metale = []
        sztabki = []

        for i in range(1):                              # DODANIE DO POSZCZEGOLNYCH LIST
            metale.append(Przedmiot.ruda_zelaza)
            metale.append(Przedmiot.ruda_miedzi)
            metale.append(Przedmiot.ruda_brazu)
            metale.append(Przedmiot.ruda_niklu)
            metale.append(Przedmiot.ruda_zlota)
            metale.append(Przedmiot.ruda_srebra)

            sztabki.append(Przedmiot.sz_zelaza)
            sztabki.append(Przedmiot.sz_miedzi)
            sztabki.append(Przedmiot.sz_brazu)
            sztabki.append(Przedmiot.sz_niklu)
            sztabki.append(Przedmiot.sz_zlota)
            sztabki.append(Przedmiot.sz_srebra)

        for metal in metale:         # SPRAWDZA ILOSC RUD METALI W PLECAKU
            x = mojbohater.plecak.count(metal)
            print("ilość:", x, "|", metal.__str__())

        for metal in metale:
            x = mojbohater.plecak.count(metal)

            if x >= 3:                  # JAK JEST 3 LUB WIECEJ WTEDY USUWA 3 SZT I DAJE JEDNA SZTABKE .

                if metal == Przedmiot.ruda_zelaza:

                    for i in range(3):
                        mojbohater.plecak.remove(Przedmiot.ruda_zelaza)
                    mojbohater.plecak.append(Przedmiot.sz_zelaza)
                    print("Otrzymujesz:", Przedmiot.sz_zelaza.__str__())

                if metal == Przedmiot.ruda_miedzi:

                    for i in range(3):
                        mojbohater.plecak.remove(Przedmiot.ruda_miedzi)
                    mojbohater.plecak.append(Przedmiot.sz_miedzi)
                    print("Otrzymujesz:", Przedmiot.sz_miedzi.__str__())

                if metal == Przedmiot.ruda_brazu:

                    for i in range(3):
                        mojbohater.plecak.remove(Przedmiot.ruda_brazu)
                    mojbohater.plecak.append(Przedmiot.sz_brazu)
                    print("Otrzymujesz:", Przedmiot.sz_brazu.__str__())

                if metal == Przedmiot.ruda_niklu:

                    for i in range(3):
                        mojbohater.plecak.remove(Przedmiot.ruda_niklu)
                    mojbohater.plecak.append(Przedmiot.sz_niklu)
                    print("Otrzymujesz:", Przedmiot.sz_niklu.__str__())

                if metal == Przedmiot.ruda_zlota:

                    for i in range(3):
                        mojbohater.plecak.remove(Przedmiot.ruda_zlota)
                    mojbohater.plecak.append(Przedmiot.sz_zlota)
                    print("Otrzymujesz:", Przedmiot.sz_zlota.__str__())

                if metal == Przedmiot.ruda_srebra:

                    for i in range(3):
                        mojbohater.plecak.remove(Przedmiot.ruda_srebra)
                    mojbohater.plecak.append(Przedmiot.sz_srebra)
                    print("Otrzymujesz:", Przedmiot.sz_srebra.__str__())

    def handel(self, mojbohater: Bohater.Bohater):

        print("\nZobacz co mam na sprzedaż: ")
        print("{} {}".format("1.|", "Miecz: "))
        print("{} {}".format("2.|", "Pancerz: "))
        print("{} {}".format("3.|", "Tarcza: "))
        print("{} {}".format("4.|", "Hełm: "))
        print("{} {}".format("5.|", "Pozostałe: "))

        miecze = []
        pancerz = []
        tarcza = []
        helm = []
        pozostale = []

        for i in range(1):                          # DODAJE PRZEDMIOTY DO KONKRETNYCH LIST.
            miecze.append(Przedmiot.miecz_zardzewialy)
            miecze.append(Przedmiot.miecz_zwykly)
            miecze.append(Przedmiot.miecz_doskonaly)
            miecze.append(Przedmiot.miecz_stalowy)
            miecze.append(Przedmiot.miecz_zelazny)

            pancerz.append(Przedmiot.pancerz_sierzanta)
            pancerz.append(Przedmiot.pancerz_straznika)
            pancerz.append(Przedmiot.pancerz_oficera)

            tarcza.append(Przedmiot.tarcza_drewniana)
            tarcza.append(Przedmiot.tarcza_stalowa)
            tarcza.append(Przedmiot.tarcza_zelazna)
            tarcza.append(Przedmiot.tarcza_rogata)

            helm.append(Przedmiot.helm_skorzany)
            helm.append(Przedmiot.helm_stalowy)
            helm.append(Przedmiot.helm_zelazny)
            helm.append(Przedmiot.helm_rogaty)

            pozostale.append(Przedmiot.kilof)
            pozostale.append(Przedmiot.mlotek)
            pozostale.append(Przedmiot.oselka)

        wybor = int(input("\nWybierz: "))              # WYBIERAMY KATEGORIE

        if wybor == 1:
            nr = 0

            for rzecz in miecze:                     # POKAZE PRZEDMIOTY ZACZYNAJAC OD 1.
                nr += 1
                print("Nr:", str(nr), rzecz, sep=" ")

            kupiony = input("\nKtóry chcesz kupić: ")
            nr_przedmiotu = int(kupiony)
            nr_przedmiotu -= 1
            wartosc_przedmiotu = Przedmiot.Zwykly.kupno(miecze[nr_przedmiotu])

            if mojbohater.sakwa >= wartosc_przedmiotu:              # SPRAWDZA ILOSC MONET W SAKWIE DO CENY PRZEDMIOTU
                print("Mam odpowiednią ilość monet.")               # JAK NAS STAC TO KUPUJE.
                mojbohater.sakwa -= wartosc_przedmiotu
                mojbohater.plecak.append(miecze[nr_przedmiotu])
                print("Zostało mi:", mojbohater.sakwa)

            else:
                print("\nMasz za mało pieniedzy.",                  # JAK NIE STAC TO ZWRACA SAKWE I CENE PRZEDMIOTU
                      "\nSakwa:", mojbohater.sakwa, "|Cena przedmiotu:", wartosc_przedmiotu)

        elif wybor == 2:
            nr = 0

            for rzecz in pancerz:
                nr += 1
                print("Nr:", str(nr), rzecz, sep=" ")

            kupiony = input("\nKtóry chcesz kupić: ")
            nr_przedmiotu = int(kupiony)
            nr_przedmiotu -= 1
            wartosc_przedmiotu = Przedmiot.Zwykly.kupno(pancerz[nr_przedmiotu])

            if mojbohater.sakwa >= wartosc_przedmiotu:
                print("Mam odpowiednią ilość monet.")
                mojbohater.sakwa -= wartosc_przedmiotu
                mojbohater.plecak.append(pancerz[nr_przedmiotu])
                print("Zostało mi:", mojbohater.sakwa)

            else:
                print("\nMasz za mało pieniedzy.",
                      "\nSakwa:", mojbohater.sakwa, "|Cena przedmiotu:", wartosc_przedmiotu)

        elif wybor == 3:
            nr = 0

            for rzecz in tarcza:
                nr += 1
                print("Nr:", str(nr), rzecz, sep=" ")

            kupiony = input("\nKtóry chcesz kupić: ")
            nr_przedmiotu = int(kupiony)
            nr_przedmiotu -= 1
            wartosc_przedmiotu = Przedmiot.Zwykly.kupno(tarcza[nr_przedmiotu])

            if mojbohater.sakwa >= wartosc_przedmiotu:
                print("Mam odpowiednią ilość monet.")
                mojbohater.sakwa -= wartosc_przedmiotu
                mojbohater.plecak.append(tarcza[nr_przedmiotu])
                print("Zostało mi:", mojbohater.sakwa)
            else:
                print("\nMasz za mało pieniedzy.",
                      "\nSakwa:", mojbohater.sakwa, "|Cena przedmiotu:", wartosc_przedmiotu)

        elif wybor == 4:
            nr = 0

            for rzecz in helm:
                nr += 1
                print("Nr:", str(nr), rzecz, sep=" ")

            kupiony = input("\nKtóry chcesz kupić: ")
            nr_przedmiotu = int(kupiony)
            nr_przedmiotu -= 1
            wartosc_przedmiotu = Przedmiot.Zwykly.kupno(helm[nr_przedmiotu])

            if mojbohater.sakwa >= wartosc_przedmiotu:
                print("Kupiłeś: ", helm[nr_przedmiotu])
                mojbohater.sakwa -= wartosc_przedmiotu
                mojbohater.plecak.append(helm[nr_przedmiotu])
                print("Zostało mi:", mojbohater.sakwa)

            else:
                print("\nMasz za mało pieniedzy.",
                      "\nSakwa:", mojbohater.sakwa, "|Cena przedmiotu:", wartosc_przedmiotu)

        elif wybor == 5:
            nr = 0

            for rzecz in pozostale:
                nr += 1
                print("Nr:", str(nr), rzecz, sep=" ")
            kupiony = input("\nKtóry chcesz kupić: ")
            nr_przedmiotu = int(kupiony)
            nr_przedmiotu -= 1
            wartosc_przedmiotu = Przedmiot.Zwykly.kupno(pozostale[nr_przedmiotu])

            if mojbohater.sakwa >= wartosc_przedmiotu:
                print("Kupiłeś: ", pozostale[nr_przedmiotu])
                mojbohater.sakwa -= wartosc_przedmiotu
                mojbohater.plecak.append(pozostale[nr_przedmiotu])
                print("Zostało mi:", mojbohater.sakwa)

            else:
                print("\nMasz za mało pieniedzy.",
                      "\nSakwa:", mojbohater.sakwa, "|Cena przedmiotu:", wartosc_przedmiotu)

    def naprawa(self, mojbohater: Bohater.Bohater):             #NAPRAWA EKWIPUNKU
        print("\nZa 'bryłke złota' moge naprawić twoj ekwipunek.")
        print("Stan pancerza: {}, Stan broni {}".format(mojbohater.stan_pancerz, mojbohater.stan_bron))

        wybor = str(input("Czy chcesz dokonać naprawy: (T/N)"))

        if wybor == "T":
            if Przedmiot.brylka in mojbohater.plecak:           #SPRAWDZA CZY JEST BRYŁKA
                print("Naprawiam:")
                mojbohater.plecak.remove(Przedmiot.brylka)      #USUWA BRYŁKE

                while mojbohater.stan_pancerz < 5:              #NAPRAWIA W PETLI DO WARTOSCI 5.
                    time.sleep(2)
                    mojbohater.stan_pancerz += 1
                    print("+", mojbohater.stan_pancerz)

                print("Pancerz: ", mojbohater.stan_pancerz)

                while mojbohater.stan_bron < 5:
                    time.sleep(2)
                    mojbohater.stan_bron += 1
                    print("+", mojbohater.stan_bron)

                print("Broń: ", mojbohater.stan_bron)

            else:
                print("Nie masz 'bryłki złota', ilość:", mojbohater.plecak.count(Przedmiot.brylka))

        else:
            print("Wróć jak zmienisz zdanie.")

    def skup(self, mojbohater: Bohater.Bohater):
        print("Tutaj możesz sprzedać mi kilka twoich rzeczy: ")
        nr = 0

        for rzecz in mojbohater.plecak:
            nr += 1
            print("Nr:", str(nr), rzecz, sep=" ")

        sprzedany = input("Wybierz numer przedmiotu: ")
        nr_sprzedany = int(sprzedany)
        nr_sprzedany -= 1
        wartosc_przedmiotu = Przedmiot.Zwykly.sprzedaz(mojbohater.plecak[nr_sprzedany])
        print("Chcesz sprzedać za: ", wartosc_przedmiotu)

        wybor = input("T/N: ")

        if wybor == "T":
            mojbohater.plecak.remove(mojbohater.plecak[nr_sprzedany])
            mojbohater.sakwa += wartosc_przedmiotu

        else:
            print("Wróc jak zmienisz zdanie.")