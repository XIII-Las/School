class Account:
    def __init__(self, balance):
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Vklad: +{amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Nedostatek peněz")
        else:
            self.balance -= amount
            self.history.append(f"Výběr: -{amount}")

    def show_history(self):
        if not self.history:
            print("Žádné transakce.")
        else:
            print("Historie transakcí:")
            for transaction in self.history:
                print(transaction)

    def __str__(self):
        return f"\nZůstatek na účtě: {self.balance}\n"


Zustatek = 45000
Ucet = Account(Zustatek)

while True:
    print(Ucet)
    print("Menu:")
    print("D - Vklad")
    print("W - Výběr")
    print("H - Historie")
    print("Q - Konec")

    y = input("Zadejte požadavek: ").upper()

    if y == 'D' or y == 'd':
        amount = int(input("Zadejte sumu: "))
        Ucet.deposit(amount)

    elif y == 'W' or y == 'w':
        amount = int(input("Zadejte sumu: "))
        Ucet.withdraw(amount)

    elif y == 'H' or y == 'h':
        Ucet.show_history()

    elif y == 'Q' or y == 'q':
        print("Odhlašujeme Vás.")
        break

    else:
        print("Zkus to jinak.")