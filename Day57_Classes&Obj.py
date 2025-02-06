# Class and Object

class person:
    name = ("Ahmed")
    occupation = "Back end developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
# a.name = "Ahsan"
# a.occupation = "Accountant"
# print(a.name,a.occupation)
a.info()