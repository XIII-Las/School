class Book:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    def __str__(self):
        if self.pages >= 400:
            return f"Jméno knihy: {self.name} Počet stran: {self.pages}, kniha má přes 400 stran! Je rozhodně dlouhá."
        else:
            return f"Jméno knihy: {self.name} Počet stran: {self.pages}, kniha není zas tak dlouhá."

# Knihy jsou fiktivní
Book1 = Book("Příběh pana Kozáka a dvaceti ajťáků", 700)
Book2 = Book("Michal Bubílek; O smyslu života", 42)
Book3 = Book("O banánu, co se proletěl", 250)

Knihy = [Book1, Book2, Book3]

Books_sort = sorted(Knihy, key=lambda x: x.pages, reverse=True)

x = 0

for kniha in Books_sort:
    if x < 1:
        print("Ocenění za nejdelší knihu vyhrává:")
        x+=1
    print(f"{kniha} \n")