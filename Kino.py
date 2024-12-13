from random import random


class Kolejka:
    def __init__(self):
        self.n = []

    def add(self, imie, nazwisko):
        self.n.append({'Imie': imie, "Nazwisko": nazwisko})

    def queue(self):
        if self.n:
            return self.n.pop(0)
        return None

    def show_queue(self):
        return self.n

class Kino:
    def __init__(self):
        self.seats = [[0 for _ in range(10)] for _ in range(10)]
        self.history = []

    def find(self):
        free_seats = [(r, c) for r in range(10) for c in range(10) if self.seats[r][c] == 0]
        return random.choice(free_seats) if free_seats else None

    def give_seat(self, customer):
        seat = self.find()
        if seat:
            r, c = seat
            self.seats[r][c] = 1
            self.history.append({"klient": customer, "miejsca": seat})
            return seat
        return None

    def show_seats(self):
        for i in self.seats:
            print(" ".join(str(m) for m in i))
            return self.history
