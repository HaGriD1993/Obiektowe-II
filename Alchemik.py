import random
import time
import Bohater
import Przedmiot


class Alchemik:
    def __init__(self):
        self.imie = "Bogdan"
        self.wiek = 72
        self.specjanosc = "Zielarz"

    def info(self):
        print("Witaj nazywam się:", self.imie, ",jestem", self.specjanosc+"em")

    def zbieranie(self, mojapostac: Bohater.Bohater):
        las_ziola = ["Czerwone źiele", "Niebieski bez", "Korzeń piementu", "Kwiat drugrotu"]
        bagna_ziola = ["Bagienne źiele", "Kulczyba wronie oko", "Trójkolorowe źiele", "Jaskółcze źiele",
                       "Ziarna sporyszu"]

        print("Mogę zebrać składniki roslinne, wybierz gdzie mam się udać: "
              "\n1: Las "
              "\n2: Bagna ")

        zbieraj = int(input("Wybierz miejsce ___ : "))

        if zbieraj == 1:
            print("Ide do lasu. ")
            time.sleep(6)
            ziolo_1 = random.randint(0, 1)
            if ziolo_1 == 1:
                for ziolo in range(5):
                    wybrane = random.choice(las_ziola)
                    mojapostac.plecak.append(wybrane)
                    print("Zebrałem: ", wybrane)
                    time.sleep(1)
            elif ziolo_1 == 0:
                print("Nie udało mi sie nic znaleść.")

        if zbieraj == 2:
            print("Ide na bagna. ")
            ziolo_2 = random.randint(0, 1)
            time.sleep(10)
            if ziolo_2 == 1:
                for ziolo in range(5):
                    wybrane = random.choice(bagna_ziola)
                    mojapostac.plecak.append(wybrane)
                    print("Zebrałem: ", wybrane)
                    time.sleep(1)
            elif ziolo_2 == 0:
                print("Nie udało mi sie nic znaleść.")

    def mikstury(self, mojapostac: Bohater.Bohater):
        miksturki = {1: "Mała mikstura leczenia",
                     2: "Duża mikstura leczenia",
                     3: "Mikstura 'Powrót do korzeni'",
                     4: "Napar z utopca",
                     5: "Strychnina",
                     6: "Botulina"
                     }

        print("Moge ofiarowac ci kilka pomocnych mikstur: "
              "\n 1. Lęczące "
              "\n 2. Regeneracyjne "
              "\n 3. Trucizny ")

        pokaz_miks = int(input("Wybierz ___ : "))

        if pokaz_miks == 1:
            mojapostac.plecak.append(miksturki[1]), mojapostac.plecak.append(miksturki[2])
            print("Otrzymujesz: ", miksturki[1], ",", miksturki[2])
        elif pokaz_miks == 2:
            mojapostac.plecak.append(miksturki[3]), mojapostac.plecak.append(miksturki[4])
            print("Otrzymujesz: ", miksturki[3], ",", miksturki[4])
        elif pokaz_miks == 3:
            mojapostac.plecak.append(miksturki[5]), mojapostac.plecak.append(miksturki[6])
            print("Otrzymujesz: ", miksturki[5], ",", miksturki[6])

    def transmutacja(self, mojapostac: Bohater.Bohater):
        if Przedmiot.olow in mojapostac.plecak:
            szansa = [1, 2, 3, 4, 5]
            moja_szansa = random.choice(szansa)
            print("Moge zamienić ołów w złoto: ", "szansa: ", moja_szansa, "%")
            wybor = int(input("Zamienic ołów w złoto ?\n1.Tak \n2.Nie\n: "))
            if wybor == 1:
                print("Szansa na przemianę:", moja_szansa, "%")
                ulepszenie = random.randint(0, 1)
                if ulepszenie == 1:
                    print("Pomyślne ulepszenie, otrzymujesz 'Bryłka złota' ")
                    mojapostac.plecak.append(Przedmiot.brylka)
                elif ulepszenie == 0:
                    print("Zawiodłem, tracisz 'ołów' ")
                    mojapostac.plecak.remove(Przedmiot.olow)
            else:
                print("Nie chciałeś zaryzykować.")
        else:
            print("Nie masz: 'ołowiu' spróbuj wydobyć.")











