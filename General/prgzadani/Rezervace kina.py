class Cinema:
    def __init__(self, seats_count):
        self.free_seats = []
        for i in range(1, seats_count + 1):
            self.free_seats.append(i)

    def reserve(self, seat_number):
        if seat_number in self.free_seats:
            self.free_seats.remove(seat_number)
            print("Rezervace proběhla úspěšně")
        else:
            print("Místo je obsazené nebo neexistuje")

    def show_seats(self):
        print("Volná místa:", self.free_seats)


pocet_mist = 10
Kino = Cinema(pocet_mist)

while True:
    print("\nMenu:")
    print("R - Rezervace")
    print("V - Volná místa")
    print("Q - Konec")

    volba = input("Zadejte požadavek: ").upper()

    if volba == "R" or volba == "r":
        misto = int(input("Zadejte číslo místa: "))
        
        if misto >= 1 and misto <= pocet_mist:
            Kino.reserve(misto)
        else:
            print("Neplatné číslo místa")

    elif volba == "V" or volba == "v":
        Kino.show_seats()

    elif volba == "Q" or volba == "q":
        print("Konec")
        break

    else:
        print("Zkus to jinak")