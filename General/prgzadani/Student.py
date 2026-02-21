class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def name(self):
        return self.name
    
    def grades(self):
        return self.grades
    
    def average(self):
        return sum(self.grades) / len(self.grades)
    
    def __str__(self):
        x = False
        if self.average() >= 4.5:
            x = True
        if x == False:
            return f"Jméno: {self.name} Známky: {self.grades} Průměr: {self.average()} Student prošel! :D"
        else:
            return f"Jméno: {self.name} Známky: {self.grades} Průměr: {self.average()} Student neprošel! :("
    
Student1 = Student("John Student", [5, 4, 5])
Student2 = Student("Michael", [1, 1, 1])
Student3 = Student("Martins", [3, 2, 1])

Studenti = [Student1, Student2, Student3]

Students_sort = sorted(Studenti, key=lambda x: x.average())

for školáček in Students_sort:
    print(školáček)