# Inheritance in Python

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showDetail(self):
        print(f"The name of Employee: {self.id} is {self.name}")
class Programmer (Employee):
    def showLanguage(self):
        print("The default language is Python")

e1 = Employee("Ahmed", 1)
e2 = Programmer("Ahsan", 2)
e3 = Employee("hamza", 3)
e4 = Employee("Bilal", 4)
e5 = Employee("Rafay", 5)
e1.showDetail()
e2.showDetail()
e2.showLanguage()
e3.showDetail()
e4.showDetail()
e5.showDetail()

