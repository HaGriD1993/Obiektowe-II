import random
import time
import Bohater
import Przedmiot


class Kowal():
    def __init__(self):
        self.imie = "Ryszard"
        self.wiek = 52
        self.specjanosc = "Kowal"

    def info(self):
        print("\nWitaj nazywam się: " + self.imie, ",jestem", self.specjanosc+"em")   #PRZEDSTAWIA SIE

    def skladniki(self, mojbohater: Bohater.Bohater):
        metale = ["ruda Stali", " ruda Żelaza", "ruda Miedzi", "ruda Brązu", "ruda Niklu", "ruda Złota"]
        dodatki = ["Drewno", "Węgiel", "Świńska skóra", "Diament"]

        wyb_metale = random.sample(metale, k=3)                 #RANDOMOWE ELEMENTY Z LISTY
        wyb_dodatki = random.sample(dodatki, k=2)               #RANDOMOWE ELEMENTY Z LISTY

        if Przedmiot.brylka in mojbohater.plecak:               #SPRAWDZA CZY MA BRYŁKE W PLECAKU
            wybor = input("Za 'bryłke złota' mogę dać ci kilka metali. (T/N): ")
            if wybor == str("T"):
                print("Za bryłke otrzymujesz: ")
                mojbohater.plecak.remove(Przedmiot.brylka)      #USUWA BRYŁKE Z PLECAKA
                print(wyb_metale)
                mojbohater.plecak.extend(wyb_metale)        #DODAJE DO PLECAKA Z LISTY METALI
                time.sleep(2)
                print("Dostajesz również: ", wyb_dodatki)
                mojbohater.plecak.extend(wyb_dodatki)      #DODAJE DO PLECAKA Z LISTY DODATKÓW

            if wybor == str("N"):
                print("Wróć jak zmienisz zdanie.")
        else:
            print("Nie masz 'bryłki złota'. Wróć jak znajdziesz.")    #JAK NIE MA BRYŁKI TO KONIEC

    def przetapianie(self, mojbohater: Bohater.Bohater):
        metale_lista = ["ruda Stali", " ruda Żelaza", "ruda Miedźi", "ruda Brązu", "ruda Niklu", "ruda Złota"]

        if Przedmiot.brylka in mojbohater.plecak:
            wybor = input("Za 'bryłke złota' mogę przetopię metal w sztabke.(T/N): ")
            if wybor == str("T"):
                mojbohater.plecak.remove(Przedmiot.brylka)
                for metal in metale_lista:                   #SPRAWDZA CZY Z ELEMENTY Z LISTY METALI SA W PLECAKU
                    if metal in mojbohater.plecak:
                        print("Ten metal moge przetopić: ", metal)
                        wybor_metal = input("Czy przetopic: (T/N): ")
                        if wybor_metal == str("T"):
                            mojbohater.plecak.remove(metal)                        #USUWA METAL Z PLECAKA, DODAJE SZTABKE
                            mojbohater.plecak.append(str("sztabka ") + metal[5:])  #USUNIE Z METALU 'RUDE'
                        else:
                            print("Może poźniej.")
                else:
                    print("Nie masz nic do przetopienia.")

    def handel(self, mojbohater: Bohater.Bohater):

        print("\nZobacz co mam na sprzedaż: ")
        print("{} {}".format("1.|", "Miecz: "))
        print("{} {}".format("2.|", "Pancerz: "))
        print("{} {}".format("3.|", "Tarcza: "))
        print("{} {}".format("4.|", "Hełm: "))

        miecze = []
        pancerz = []
        tarcza = []
        helm = []

        for i in range(1):              # DODAJE PRZEDMIOTY DO KONKRETNYCH LIST.
            miecze.append(Przedmiot.miecz_zardzewialy)
            miecze.append(Przedmiot.miecz_zwykly)
            miecze.append(Przedmiot.miecz_doskonaly)

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

        wybor = int(input("\nWybierz:"))              #WYBIERAMY KATEGORIE
        if wybor == 1:
            nr = 0
            for rzecz in miecze:                    #POKAZE PRZEDMIOTY ZACZYNAJAC OD 1.
                nr += 1
                print("Nr:", str(nr), rzecz, sep=" ")
            kupiony = input("\nKtóry chcesz kupić: ")
            nr_przedmiotu = int(kupiony)
            nr_przedmiotu -= 1
            wartosc_przedmiotu = Przedmiot.Zwykly.sprzedaz(miecze[nr_przedmiotu])  #FUNKCJA ZWORCI CENE PRZEDMIOTU

            if mojbohater.sakwa >= wartosc_przedmiotu:              #SPRAWDZA ILOSC MONET W SAKWIE DO CENY PRZEDMIOTU
                print("Mam odpowiednią ilość monet.")               # JAK NAS STAC TO KUPUJE.
                mojbohater.sakwa -= wartosc_przedmiotu
                mojbohater.plecak.append(miecze[nr_przedmiotu])
                print("Zostało mi:", mojbohater.sakwa)
            else:
                print("\nMasz za mało pieniedzy.",                  #JAK NIE STAC TO ZWRACA SAKWE I CENE PRZEDMIOTU
                      "\nSakwa:", mojbohater.sakwa, "|Cena przedmiotu:", wartosc_przedmiotu)

        elif wybor == 2:
            nr = 0
            for rzecz in pancerz:
                nr += 1
                print("Nr:", str(nr), rzecz, sep=" ")
            kupiony = input("\nKtóry chcesz kupić: ")
            nr_przedmiotu = int(kupiony)
            nr_przedmiotu -= 1
            wartosc_przedmiotu = Przedmiot.Zwykly.sprzedaz(pancerz[nr_przedmiotu])

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
            wartosc_przedmiotu = Przedmiot.Zwykly.sprzedaz(tarcza[nr_przedmiotu])

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
            wartosc_przedmiotu = Przedmiot.Zwykly.sprzedaz(helm[nr_przedmiotu])

            if mojbohater.sakwa >= wartosc_przedmiotu:
                print("Mam odpowiednią ilość monet.")
                mojbohater.sakwa -= wartosc_przedmiotu
                mojbohater.plecak.append(helm[nr_przedmiotu])
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
        wartosc_przedmiotu = Przedmiot.Zwykly.kupno(mojbohater.plecak[nr_sprzedany])
        print("Chcesz sprzedać za: ", wartosc_przedmiotu)
        wybor = input("T/N: ")

        if wybor == "T":
            mojbohater.plecak.remove(mojbohater.plecak[nr_sprzedany])
            mojbohater.sakwa += wartosc_przedmiotu
        else:
            print("Wróc jak zmienisz zdanie.")

