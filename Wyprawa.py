import Bohater
import random
import time
import Przedmiot


class Potwor:
    def __init__(self, nazwa, zycie, atak):
        self.nazwa = nazwa
        self.zycie = zycie
        self.atak = atak

    def __str__(self):
        return self.nazwa


def wyprawa(mojbohater: Bohater.Bohater):
    print("Opuszczasz miasto, wybierz dokąd sie wybierasz: ")
    print("1.Las ({}) \n2.Las ({}) \n3.Bagna ({})".format("łatwy", "trudny", "trudny"))

    latwe_potwory = []
    trudne_potwory = []

    dzik = Potwor("Dzik", 15, 5)
    waz = Potwor("Wąż", 10, 3)
    orzel = Potwor("Orzeł", 12, 4)
    jelen = Potwor("Jeleń", 10, 4)
    niedzwiedz_b = Potwor("Niedzwiedz Brunatny", 75, 10)
    niedzwiedz_s = Potwor("Niedzwiedz Szary", 70, 14)
    wilk_s = Potwor("Wilk Szary", 45, 11)
    wilk_cz = Potwor("Wilk Czarny", 50, 9)

    for i in range(1):
        latwe_potwory.append(dzik)
        latwe_potwory.append(waz)
        latwe_potwory.append(orzel)
        latwe_potwory.append(jelen)
        trudne_potwory.append(niedzwiedz_b)
        trudne_potwory.append(niedzwiedz_s)
        trudne_potwory.append(wilk_s)
        trudne_potwory.append(wilk_cz)

    potwor_latwy = random.choice(latwe_potwory)
    potwor_trudny = random.choice(trudne_potwory)

    wybor = int(input("\nWybierz: "))

    if wybor == 1:
        print("Wkraczasz do Lasu: ")
        print("Atakuje:", potwor_latwy)
        potwor_latwy.zycie = random.randint(5, potwor_latwy.zycie)

        while potwor_latwy.zycie > 0 and mojbohater.pkt_zycia > 0:       # zycie potwora wieksze od 0 i boh. wieksze od 0.
            potw_atak = random.randint(1, potwor_latwy.atak)             # losuje jaka wartoscia uderzy potwor.
            boh_atak = random.randint(1, mojbohater.pkt_ataku)           # losuje jaka wartoscia uderzy bohater.
            boh_def = random.randint(1, mojbohater.pkt_obrony)           # losuje jaka wartosc zablokuje bohater.
            potwor_latwy.zycie -= boh_atak                               # zadane obrazenia odejete od zycia potwora
            print("###" * 10)
            print("Bohater: ", mojbohater.pkt_zycia, "życia.", "\nBohater atakuje: ", boh_atak)  # ile zycia ma bohater oraz ile zaatakuje
            time.sleep(1)
            print(potwor_latwy, ":", potwor_latwy.zycie, "zycia.")     # ilosc zycia potwora
            print(potwor_latwy, "atakuje:", potw_atak)                 # zadane obrazenia potwora
            print("Bohater blokuje tarcza: ", boh_def)                 # pokaze ile bohater blokuje
            zadane_obrPotw = potw_atak - boh_def

            if zadane_obrPotw < 0:      # JAK BEDA OBRAZENIA UJEMNE WTEDY ZMIENIA NA 0
                zadane_obrPotw = 0

            mojbohater.pkt_zycia -= zadane_obrPotw

        if potwor_latwy.zycie <= 0:
            print("\nPokonałeś:", potwor_latwy)
            brylka = random.randint(0, 8)                   # szansa na otrzymanie bryłki

            if brylka == 2:
                mojbohater.plecak.append(Przedmiot.brylka)
                print("Otrzymujesz 'bryłke złota'")

            mojbohater.sakwa += 3                           # dodanie do sakwy w ramach nagrody
            mojbohater.pkt_dosw += 5                        # bohater dostaje doswiadczenie

        else:
            print("##############")
            print(potwor_latwy, "cie zabił")

    if wybor == 2:
        print("Wkraczasz do Lasu: ")
        print("Atakuje:", potwor_trudny)
        potwor_trudny.zycie = random.randint(20, potwor_trudny.zycie)

        while potwor_trudny.zycie > 0 and mojbohater.pkt_zycia > 0:
            potw_atak = random.randint(5, potwor_trudny.atak)
            boh_atak = random.randint(1, mojbohater.pkt_ataku)
            boh_def = random.randint(1, mojbohater.pkt_obrony)
            potwor_trudny.zycie -= boh_atak
            print("###" * 10)
            print("Bohater: ", mojbohater.pkt_zycia, "życia.", "\nBohater atakuje: ", boh_atak)
            time.sleep(1)
            print(potwor_trudny, ":", potwor_trudny.zycie, "zycia.")
            print(potwor_trudny, "atakuje:", potw_atak)
            print("Bohater blokuje tarcza: ", boh_def)
            zadane_obrPotw = potw_atak - boh_def

            if zadane_obrPotw < 0:
                zadane_obrPotw = 0

            mojbohater.pkt_zycia -= zadane_obrPotw

        if potwor_trudny.zycie <= 0:
            print("\nPokonałeś:", potwor_trudny)
            brylka = random.randint(0, 5)

            if brylka == 1:
                mojbohater.plecak.append(Przedmiot.brylka)
                print("Otrzymujesz 'bryłke złota'")

            mojbohater.sakwa += 10
            mojbohater.pkt_dosw += 15

        else:
            print("##############")
            print(potwor_trudny, "cie zabił")

    if wybor == 3:
        print("Wchodzisz na Bagna: ")
        print("Atakuje:", potwor_trudny)
        potwor_trudny.zycie = random.randint(40, potwor_trudny.zycie)

        while potwor_trudny.zycie > 0 and mojbohater.pkt_zycia > 0:
            potw_atak = random.randint(5, potwor_trudny.atak) + 3
            boh_atak = random.randint(1, mojbohater.pkt_ataku)
            boh_def = random.randint(1, mojbohater.pkt_obrony)
            potwor_trudny.zycie -= boh_atak - 2
            print("###" * 10)
            print("Bohater: ", mojbohater.pkt_zycia, "życia.", "\nBohater atakuje: ", boh_atak)
            time.sleep(1)
            print(potwor_trudny, ":", potwor_trudny.zycie, "zycia.")
            print(potwor_trudny, "atakuje:", potw_atak)
            print("Bohater blokuje tarcza: ", boh_def)
            zadane_obrPotw = potw_atak - boh_def

            if zadane_obrPotw < 0:
                zadane_obrPotw = 0

            mojbohater.pkt_zycia -= zadane_obrPotw

            time.sleep(1)

        if potwor_trudny.zycie <= 0:
            print("\nPokonałeś:", potwor_trudny)
            brylka = random.randint(0, 3)

            if brylka == 1:
                mojbohater.plecak.append(Przedmiot.brylka)
                print("Otrzymujesz 'bryłke złota'")

            mojbohater.sakwa += 18
            mojbohater.pkt_dosw += 20

        else:
            print("##############")
            print(potwor_trudny, "cie zabił")
