import Bohater
import Przeciwnik
import Alchemik
import Kowal
import Wyprawa


if __name__ == "__main__":
    print("Witaj w grze. Na początku podaj imie dla twojego bohatera: ")

    imie = input("\nImie bohatera: ")
    print("\nWybierz klase: ")
    print("{}| {}| {}| {}| {}|".format("1.", "Wojownik ", "Atak: 10 ", "Obrona: 3 ", "Życie: 90  "))
    print("{}| {} | {}| {}| {}|".format("2.", "Łotrzyk ", "Atak: 8  ", "Obrona: 5 ", "Życie: 95  "))
    print("{}| {}   | {}| {}| {}|".format("3.", "Druid ", "Atak: 9  ", "Obrona: 4 ", "Życie: 100 "))
    x = int(input("\nWybierz klase bohatera: "))
    if x == 1:
        postac = Bohater.Wojownik(imie, "Wojownik", [], 10, 3, 90)
    elif x == 2:
        postac = Bohater.Lotrzyk(imie, "Łotrzyk", [], 8, 5, 95)
    elif x == 3:
        postac = Bohater.Driud(imie, "Druid", [], 9, 4, 100)


    print("\n'bryłka złota'- możesz ja zdobyc na wyprawach oraz podczas kopania złóż metali.")

    kowal = Kowal.Kowal()
    alchemik = Alchemik.Alchemik()
    mob = Przeciwnik.Przeciwnik()


    #Menu:
    while True:

        print("\n1. Bohater:      Informacje |Naprawa ekwipunku |Polowanie |Ognisko |Wyprawa |Inwentarz |Odpoczynek")
        print("2. Kowal:        Informacje |Kuźnia  |Sklepik")
        print("3. Alchemik:     Informacje |Rośliny |Mikstury")
        print("4. Sanktuarium: ")
        print("5. Koniec gry.")
        wybor_1 = int(input("\nWybierz: "))



        #Bohater:
        if wybor_1 == 1:
            postac.info()
            postac.awans()
            postac.stan_zdrowia()
            print("\n1. Naprawa ekwipunku: ")
            print("2. Polowanie: ")
            print("3. Gotowanie: ")
            print("4. Wyprawa: ")
            print("5. Sprawdź plecak: ")
            print("6. Górnictwo: ")
            print("7. Odpoczynek: ")
            print("8. Sakiewka: ")

            wybor_2 = int(input("\nWybierz: "))
            if wybor_2 == 1:
                postac.naprawaeq()
            elif wybor_2 == 2:
                postac.polowanie()
            elif wybor_2 == 3:
                postac.ognisko()
            elif wybor_2 == 4:
                Wyprawa.wyprawa(postac)
            elif wybor_2 == 5:
                postac.sprawdzplecak()
            elif wybor_2 == 6:
                postac.gornictwo()
            elif wybor_2 == 7:
                postac.odpoczynek()
            elif wybor_2 == 8:
                postac.wymiana()
                continue

        #Kowal
        if wybor_1 == 2:
            kowal.info()
            print("\n\n1.Materiały i Rudy: ")
            print("2.Przetopy: ")
            print("3.Sklep: ")
            print("4.Skup przedmiotów: ")
            wybor_2 = int(input("\nWybierz: "))
            if wybor_2 == 1:
                kowal.skladniki(postac)
            elif wybor_2 == 2:
                kowal.przetapianie(postac)
            elif wybor_2 == 3:
                kowal.handel(postac)
            elif wybor_2 == 4:
                kowal.skup(postac)
                continue

        #Alchemik
        if wybor_1 == 3:
            alchemik.info()
            print("\n1.Rośliny: ")
            print("2.Mikstury ")
            print("3.Transmutacja (ołów -> złoto)")

            wybor_2 = int(input("Wybierz: "))
            if wybor_2 == 1:
                alchemik.zbieranie(postac)
            elif wybor_2 == 2:
                alchemik.mikstury(postac)
            elif wybor_2 == 3:
                alchemik.transmutacja(postac)
                continue

        #Walka z Lilith
        if wybor_1 == 4:
            mob.info()
            mob.walka(postac)

        #Kuniec:
        if wybor_1 == 5:
            print("Koniec gry, było miło. (-(-_-)-) ")
            break






