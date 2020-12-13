import random
import Bohater
import time
import Przedmiot


class Przeciwnik:
    def __init__(self):
        self.imie = "Lilith - Matka Sanktuarium"
        self.wiek = 50
        self.rasa = "Demon"
        self.pkt_ataku = 8
        self.pkt_obrony = 2
        self.pkt_zycia = 150

    def info(self):
        print("Nazywam się: " + self.imie)

    def walka(self, mojbohater: Bohater.Bohater):

        if mojbohater.stan_bron and mojbohater.stan_pancerz >= 5:               #SPRAWDZAM STAN BRONI I PANCERZA
            print("Ekwipunek w doskonałym stanie.")
            print("Zbliżasz sie Sanktuarium, możesz sie jeszcze wycofac. "
                  "\nWybierz 1. aby wejść do srodka i zmierzycz sie z 'Lilith'.")

            wybor = int(input(":"))

            if wybor == 1:
                print("Atakuje Lilith: ")

            while self.pkt_zycia > 0 and mojbohater.pkt_zycia > 0:
                self.pkt_ataku = random.randrange(1, 10, 2)
                mojbohater.pkt_ataku = random.randint(1, 10)
                mojbohater.pkt_obrony = random.randint(1, 3)
                self.pkt_zycia -= mojbohater.pkt_ataku
                print("###" * 10)
                print("Bohater: ", mojbohater.pkt_zycia, "życia.", "\nBohater atakuje: ", mojbohater.pkt_ataku)
                time.sleep(2)
                print("Lilith: ", self.pkt_zycia, "punkty życia.", "\nLilith atakuje: ", self.pkt_ataku)
                time.sleep(2)
                print("Bohater blokuje tarcza: ", mojbohater.pkt_obrony)
                mojbohater.pkt_zycia -= self.pkt_ataku - mojbohater.pkt_obrony
                time.sleep(2)

            if self.pkt_zycia <= 0:
                print("Zabiłeś Lilith")
                mojbohater.plecak.append(Przedmiot.korona)
                mojbohater.plecak.append(Przedmiot.brylka)
                mojbohater.stan_pancerz = 1
                mojbohater.stan_bron = 1

            else:
                print("Poległeś w walce ")

        elif mojbohater.stan_bron < 5 or mojbohater.stan_pancerz < 5:
            print("Powinieneś naprawić ekwipunek. Narzedzia można znaleść u Kowala.")














