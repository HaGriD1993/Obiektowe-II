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

    dzik = Potwor("Dzik", 15, 7)
    waz = Potwor("Wąż", 10, 5)
    orzel = Potwor("Orzeł", 12, 4)
    jelen = Potwor("Jeleń", 10, 5)
    niedzwiedz_b = Potwor("Niedzwiedz Brunatny", 75, 12)
    niedzwiedz_s = Potwor("Niedzwiedz Szary", 70, 18)
    wilk_s = Potwor("Wilk Szary", 45, 13)
    wilk_cz = Potwor("Wilk Czarny", 50, 12)

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

        while potwor_latwy.zycie > 0 and mojbohater.pkt_zycia > 0:       #zycie potwora wieksze od 0 i boh. wieksze od 0.
            potw_atak = random.randint(1, potwor_latwy.atak)             #losuje jaka wartoscia uderzy potwor.
            boh_atak = random.randint(1, mojbohater.pkt_ataku)           #losuje jaka wartoscia uderzy bohater.
            boh_def = random.randint(1, mojbohater.pkt_obrony)           #losuje jaka wartosc zablokuje bohater.
            potwor_latwy.zycie -= boh_atak                               #zadane obrazenia odejete od zycia potwora
            print("###" * 10)
            print("Bohater: ", mojbohater.pkt_zycia, "życia.", "\nBohater atakuje: ", boh_atak)  #ile zycia ma bohater oraz ile zaatakuje
            time.sleep(1)
            print(potwor_latwy, ":", potwor_latwy.zycie, "zycia.")      #ilosc zycia potwora
            print(potwor_latwy, "atakuje:", potw_atak)                 #zadane obrazenia potwora
            print("Bohater blokuje tarcza: ", boh_def)                 #pokaze ile bohater blokuje
            mojbohater.pkt_zycia -= potw_atak - boh_def                #od zycia bohatera odejmnie wartosc ataku pomniejszona wartoscia bloku bohatera
            time.sleep(1)

        if potwor_latwy.zycie <= 0:
            print("\nPokonałeś:", potwor_latwy)
            brylka = random.randint(0, 8)                   #szansa na otrzymanie bryłki
            if brylka == 2:
                mojbohater.plecak.append(Przedmiot.brylka)
                print("Otrzymujesz 'bryłke złota'")
            mojbohater.sakwa += 3                           #dodanie do sakwy w ramach nagrody

        else:
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
            mojbohater.pkt_zycia -= potwor_trudny.atak - boh_def
            time.sleep(1)

        if potwor_trudny.zycie <= 0:
            print("\nPokonałeś:", potwor_trudny)
            brylka = random.randint(0, 5)
            if brylka == 1:
                mojbohater.plecak.append(Przedmiot.brylka)
                print("Otrzymujesz 'bryłke złota'")
            mojbohater.sakwa += 10

        else:
            print(potwor_trudny, "cie zabił")

    if wybor == 3:
        print("Wchodzisz na Bagna: ")
        print("Atakuje:", potwor_trudny)
        potwor_trudny.zycie = random.randint(40, potwor_trudny.zycie)

        while potwor_trudny.zycie > 0 and mojbohater.pkt_zycia > 0:
            potwor_trudny.atak = random.randint(8, potwor_trudny.atak + 3)
            mojbohater.pkt_ataku = random.randint(1, mojbohater.pkt_ataku + 2)
            mojbohater.pkt_obrony = random.randint(1, mojbohater.pkt_obrony + 1)
            potwor_trudny.zycie -= mojbohater.pkt_ataku
            print("###" * 10)
            print("Bohater: ", mojbohater.pkt_zycia, "życia.", "\nBohater atakuje: ", mojbohater.pkt_ataku)
            time.sleep(1)
            print(potwor_trudny, ":", potwor_trudny.zycie, "zycia.")
            print(potwor_trudny, "atakuje:", potwor_trudny.atak)
            print("Bohater blokuje tarcza: ", mojbohater.pkt_obrony)
            mojbohater.pkt_zycia -= potwor_trudny.atak - mojbohater.pkt_obrony
            time.sleep(1)

        if potwor_trudny.zycie <= 0:
            print("\nPokonałeś:", potwor_trudny)
            brylka = random.randint(0, 3)
            if brylka == 1:
                mojbohater.plecak.append(Przedmiot.brylka)
                print("Otrzymujesz 'bryłke złota'")
            mojbohater.sakwa += 18

        else:
            print(potwor_trudny, "cie zabił")
