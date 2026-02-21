class Task:
    def __init__(self, text):
        self.text = text
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        if self.done:
            return f"{self.text} - Splněno"
        else:
            return f"{self.text} - Nesplněno"


tasks = []

while True:
    print("\nMenu:")
    print("P - Přidat úkol")
    print("S - Označit jako splněný")
    print("V - Vypsat úkoly")
    print("Q - Konec")

    volba = input("Zadejte požadavek: ").upper()

    if volba == "P" or volba == "p":
        text = input("Zadejte úkol: ")
        novy_ukol = Task(text)
        tasks.append(novy_ukol)
        print("Úkol byl přidán")

    elif volba == "S" or volba == "s":
        cislo = int(input("Zadejte číslo úkolu: "))
        
        if cislo >= 1 and cislo <= len(tasks):
            tasks[cislo - 1].mark_done()
            print("Úkol byl označen jako splněný")
        else:
            print("Neplatné číslo úkolu")

    elif volba == "V" or volba == "v":
        if len(tasks) == 0:
            print("Žádné úkoly")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif volba == "Q" or volba == "q":
        print("Koneeeeeeeeeeeec")
        break

    else:
        print("Zkus to jinak")