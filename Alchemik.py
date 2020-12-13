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

    def zbieranie(self, mojbohater: Bohater.Bohater):

        ziola_las = []
        ziola_bagna = []

        for i in range(1):
            ziola_las.append(Przedmiot.czerw_ziele)   # DODANIE ELEMENTOW DO POSZEGOLNYCH LIST
            ziola_las.append(Przedmiot.nieb_ziele)
            ziola_las.append(Przedmiot.korz_piem)
            ziola_las.append(Przedmiot.kwi_drug)

            ziola_bagna.append(Przedmiot.bag_ziele)
            ziola_bagna.append(Przedmiot.kulczyba)
            ziola_bagna.append(Przedmiot.tr_ziele)
            ziola_bagna.append(Przedmiot.jask_ziele)
            ziola_bagna.append(Przedmiot.ziar_spor)

        print("Za 'bryłke złota' dam ci kilka składników roślinnych:")
        print("\n1. Surowce z lasu: ")

        for i, surlas in enumerate(ziola_las):      # ZWRACA LISTE SUROWCOW Z (LASU)
            i += 1
            print(i, "-", surlas.__str__())

        print("\n2. Surowce z bagien: ")

        for i, surbagna in enumerate(ziola_bagna):   # ZWRACA LISTE SUROWCOW Z (BAGIEN)
            i += 1
            print(i, "-", surbagna.__str__())

        zbieraj = int(input("\nWybierz: "))

        if Przedmiot.brylka in mojbohater.plecak:   # ZA BRYŁKE DA 5 SUROWCOW Z LASU LUB BAGIEN

            if zbieraj == 1:

                for i in range(5):

                    wyb_ziol = random.choice(ziola_las)     # WYBIERZE DOWOLNE 5 Z LISTY
                    mojbohater.plecak.append(wyb_ziol)
                    time.sleep(1)
                    print("Otrzymujesz:", wyb_ziol.__str__())     # ZWRACA TO CO DOSTALISMY
                    time.sleep(1)

            elif zbieraj == 2:

                for i in range(5):
                    wyb_ziol = random.choice(ziola_bagna)   # WYBIERZE DOWOLNE 5 Z LISTY
                    mojbohater.plecak.append(wyb_ziol)
                    time.sleep(1)
                    print("Otrzymujesz:", wyb_ziol.__str__())  # ZWRACA TO CO DOSTALISMY
                    time.sleep(1)

        else:
            print("Nie masz 'bryłki złota', wróc poźniej.")

    def mikstury(self, mojbohater: Bohater.Bohater):

        surowce = []
        mikstury =[]

        for i in range(1):
            mikstury.append(Przedmiot.m_lecze)          # DODANIE MIKSTUR DO LISTY MIKSTURY
            mikstury.append(Przedmiot.d_lecze)
            mikstury.append(Przedmiot.m_pd)
            mikstury.append(Przedmiot.nap_ut)
            mikstury.append(Przedmiot.strych)
            mikstury.append(Przedmiot.botul)

            surowce.append(Przedmiot.czerw_ziele)       # DODANIE SUROWCOW DO LISTY SUROWCE
            surowce.append(Przedmiot.nieb_ziele)
            surowce.append(Przedmiot.korz_piem)
            surowce.append(Przedmiot.kwi_drug)

            surowce.append(Przedmiot.bag_ziele)
            surowce.append(Przedmiot.kulczyba)
            surowce.append(Przedmiot.tr_ziele)
            surowce.append(Przedmiot.jask_ziele)
            surowce.append(Przedmiot.ziar_spor)

        print("\nMikstury: ")

        for nr, mix in enumerate(mikstury):         # ZWRACA PONUMEROWANE MIKSTURY
            nr += 1
            print(nr, mix, sep=". ")

        wybor = str(input("\nSprzawdzić składniki w plecaku ? (T/N): "))

        if wybor == "T":

            for surowiec in surowce:            # ZWRACA ILOSCI KONKRETNYCH SUROWCOW W PLECAKU
                x = mojbohater.plecak.count(surowiec)
                print(x, "szt.", surowiec)

        else:
            print(" ")

        """         
        Duża mikstura leczenia:
        - Trójkolorowe ziele szt. 1
        - Bagienne ziele szt. 1
        - Korzen piementu szt. 2
        - Czerwone ziele szt. 2
        """
        if mojbohater.plecak.count(Przedmiot.tr_ziele) >= 1:

            if mojbohater.plecak.count(Przedmiot.bag_ziele) >= 1:

                if mojbohater.plecak.count(Przedmiot.korz_piem) >= 2:

                    if mojbohater.plecak.count(Przedmiot.czerw_ziele) >= 2:

                        print("\nPosiadasz odpowiednia ilość składników na: ", Przedmiot.d_lecze)
                        wykonac = str(input("Czy chcesz stworzyć ? (T/N): "))

                        if wykonac == "T":

                            for i in range(1):
                                mojbohater.plecak.remove(Przedmiot.tr_ziele)
                                mojbohater.plecak.remove(Przedmiot.bag_ziele)

                            for i in range(2):
                                mojbohater.plecak.remove(Przedmiot.korz_piem)
                                mojbohater.plecak.remove(Przedmiot.czerw_ziele)

                            mojbohater.plecak.append(Przedmiot.d_lecze)

                        else:
                            print("Wróć jak zmienisz zdanie.")
        """
        Mała mikstura leczenia:
        - Czerwone ziele szt. 1
        - Korzen piementu szt. 1
        - Bagienne ziele szt. 1
        """

        if mojbohater.plecak.count(Przedmiot.czerw_ziele) >= 1:

            if mojbohater.plecak.count(Przedmiot.korz_piem) >= 1:

                if mojbohater.plecak.count(Przedmiot.bag_ziele) >= 1:

                    print("\nPosiadasz odpowiednia ilość składników na: ", Przedmiot.m_lecze)
                    wykonac = str(input("Czy chcesz stworzyć ? (T/N): "))

                    if wykonac == "T":

                        for i in range(1):
                            mojbohater.plecak.remove(Przedmiot.czerw_ziele)
                            mojbohater.plecak.remove(Przedmiot.korz_piem)
                            mojbohater.plecak.remove(Przedmiot.bag_ziele)

                        mojbohater.plecak.append(Przedmiot.m_lecze)

                    else:
                        print("Wróć jak zmienisz zdanie.")
        """
        Strychnina:
        - Niebieskie źiele szt. 2
        - Ziarna sporyszu szt. 3
        - Kulczyba wronie oko szt. 3
        """

        if mojbohater.plecak.count(Przedmiot.nieb_ziele) >= 2:

            if mojbohater.plecak.count(Przedmiot.ziar_spor) >= 3:

                if mojbohater.plecak.count(Przedmiot.kulczyba) >= 3:

                    print("\nPosiadasz odpowiednia ilość składników na: ", Przedmiot.strych)

                    wykonac = str(input("Czy chcesz stworzyć ? (T/N): "))

                    if wykonac == "T":

                        for i in range(2):
                            mojbohater.plecak.remove(Przedmiot.nieb_ziele)

                        for i in range(3):
                            mojbohater.plecak.remove(Przedmiot.ziar_spor)
                            mojbohater.plecak.remove(Przedmiot.kulczyba)

                        mojbohater.plecak.append(Przedmiot.strych)

                    else:
                        print("Wróć jak zmienisz zdanie.")
        """
        Botulina:
        - Kwiat drugrotu szt. 2
        - Bagienne źiele szt. 2
        - Jaskółcze źiele szt. 3
        - Ziarna sporyszu szt. 4 
        """

        if mojbohater.plecak.count(Przedmiot.kwi_drug) >= 2:

            if mojbohater.plecak.count(Przedmiot.bag_ziele) >= 2:

                if mojbohater.plecak.count(Przedmiot.jask_ziele) >= 3:

                    if mojbohater.plecak.count(Przedmiot.ziar_spor) >= 4:

                        print("\nPosiadasz odpowiednia ilość składników na: ", Przedmiot.botul)

                        wykonac = str(input("Czy chcesz stworzyć ? (T/N): "))

                        if wykonac == "T":

                            for i in range(2):
                                mojbohater.plecak.remove(Przedmiot.kwi_drug)
                                mojbohater.plecak.remove(Przedmiot.bag_ziele)

                            for i in range(3):
                                mojbohater.plecak.remove(Przedmiot.jask_ziele)

                            for i in range(4):
                                mojbohater.plecak.remove(Przedmiot.ziar_spor)

                            mojbohater.plecak.append(Przedmiot.botul)

                        else:
                            print("Wróć jak zmienisz zdanie.")

        """
        Napar z utropca:
        - Kulczyba wronie oko szt. 2
        - Czerwone źiele szt. 3
        - Niebieskie źiele szt. 3
        - Ziarna sporyszu szt. 3
        """

        if mojbohater.plecak.count(Przedmiot.kulczyba) >= 2:

            if mojbohater.plecak.count(Przedmiot.czerw_ziele) >= 3:

                if mojbohater.plecak.count(Przedmiot.nieb_ziele) >= 3:

                    if mojbohater.plecak.count(Przedmiot.ziar_spor) >= 3:

                        print("\nPosiadasz odpowiednia ilość składników na: ", Przedmiot.nap_ut)

                        wykonac = str(input("Czy chcesz stworzyć ? (T/N): "))

                        if wykonac == "T":

                            for i in range(2):
                                mojbohater.plecak.remove(Przedmiot.kulczyba)

                            for i in range(3):
                                mojbohater.plecak.remove(Przedmiot.czerw_ziele)
                                mojbohater.plecak.remove(Przedmiot.nieb_ziele)
                                mojbohater.plecak.remove(Przedmiot.ziar_spor)

                            mojbohater.plecak.append(Przedmiot.nap_ut)

                        else:
                            print("Wróć jak zmienisz zdanie.")

        """
        Mikstura 'Powrót do korzeni':
        - Kulczyba wronie oko szt. 3
        - Trójkolorowe źiele szt. 5
        - Jaskółcze źiele szt. 5
        """
        if mojbohater.plecak.count(Przedmiot.kulczyba) >= 3:

            if mojbohater.plecak.count(Przedmiot.tr_ziele) >= 5:

                if mojbohater.plecak.count(Przedmiot.jask_ziele) >= 5:

                    print("\nPosiadasz odpowiednia ilość składników na: ", Przedmiot.nap_ut)

                    wykonac = str(input("Czy chcesz stworzyć ? (T/N): "))

                    if wykonac == "T":

                        for i in range(3):
                            mojbohater.plecak.remove(Przedmiot.kulczyba)

                        for i in range(5):
                            mojbohater.plecak.remove(Przedmiot.tr_ziele)
                            mojbohater.plecak.remove(Przedmiot.jask_ziele)

                        mojbohater.plecak.append(Przedmiot.m_pd)

                    else:
                        print("Wróć jak zmienisz zdanie.")

    def transmutacja(self, mojapostac: Bohater.Bohater):

        if Przedmiot.olow in mojapostac.plecak:   # SPRAWDZA CZY PRZEDMIOT OŁÓW JEST W PLECAKU

            ulepszenie = random.randint(0, 5)  # SZANSA NA ULEPSZENIE

            print("Moge zamienić ołów w złoto: ")

            wybor = str(input("Zamienic ołów w złoto ? (T/N): "))

            if wybor == "T":
                print("Szansa na przemianę:", ulepszenie, "%")

                if ulepszenie == 3:
                    print("Pomyślne ulepszenie, otrzymujesz 'Bryłka złota' ")
                    mojapostac.plecak.append(Przedmiot.brylka)

                else:
                    print("Zawiodłem, tracisz 'ołów' ")
                    mojapostac.plecak.remove(Przedmiot.olow)

            else:
                print("Nie chciałeś zaryzykować.")

        else:
            print("Nie masz: 'ołowiu' spróbuj wydobyć.")











