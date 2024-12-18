from Kino import Kino, Kolejka


class Cinema():
    def __init__(self):
        self.kino = Kino()
        self.kolejka = Kolejka()

    def menu(self):
        while True:
            print(f"1. Dodaj klienta")
            print(f"2. Obsłurz klienta")
            print(f"3. Wyświetl kolejkę")
            print(f"4. Wyświetl salę kinową")
            print(f"5. Wyświetl historię klientów")
            print(f"6. Zakończ")
            wybor = input("Wybierz opcję: ")

            if wybor == "1":
                imie = input("Podaj imię klienta: ")
                nazwisko = input("Podaj nazwisko klienta: ")
                self.kolejka.add(imie, nazwisko)
                print(f"Klient {imie} {nazwisko} został dodany do kolejki")

            elif wybor == "2":
                klient = self.kolejka.obsluz_klienta()
                if klient:
                    miejsce = self.kino.przydziel_miejsce(klient)
                    if miejsce:
                        print(f"Klient {klient['imie']} {klient['nazwisko']} został obsłużony.")
                        print(f"Przydzielono miejsce: rząd {miejsce[0] + 1}, miejsce {miejsce[1] + 1}.")
                    else:
                        print("Brak wolnych miejsc.")
                else:
                    print("Kolejka jest pusta.")

            elif wybor == "3":
                kolejka = self.kolejka.wyswietl_kolejke()
                if kolejka:
                    print("Aktualna kolejka:")
                    for klient in kolejka:
                        print(f"{klient['imie']} {klient['nazwisko']}")
                else:
                    print("Kolejka jest pusta.")

            elif wybor == "4":
                print("Aktualny stan sali kinowej:")
                self.kino.wyswietl_sale()

            elif wybor == "5":
                historia = self.kino.wyswietl_historie()
                if historia:
                    print("Historia obsłużonych klientów:")
                    for wpis in historia:
                        klient = wpis["klient"]
                        miejsce = wpis["miejsce"]
                        print(f"{klient['imie']} {klient['nazwisko']} - rząd {miejsce[0] + 1}, miejsce {miejsce[1] + 1}")
                else:
                    print("Brak obsłużonych klientów.")

            elif wybor == "6":
                print("Zakończenie programu.")
                break

            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")


if __name__ == '__main__':
    cinema = Cinema()
    cinema.menu()

