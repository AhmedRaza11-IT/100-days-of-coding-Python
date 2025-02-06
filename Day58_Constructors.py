# Constructor in python

class person:
    def __init__(self,n,o):
        print("Hello")
        self.name = n
        self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}")


a = person("Ahmed","Developer")
b = person("Ahsan","Accountant")
# c = person(1,2)
a.info()
b.info()
# c.info()
# print(a.name)
# a.name = "Ahsan"
# a.occ = "Accountant"
# print(a.name,a.occ)
# a.info()