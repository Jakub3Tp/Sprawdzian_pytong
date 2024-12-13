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
                client = self.kolejka.queue(client)
                if seat:
                    print(f"Klient {client['imie']} {client['nazwisko']} został obsłużony")

if __name__ == '__main__':
    cinema = Cinema()
    cinema.menu()

