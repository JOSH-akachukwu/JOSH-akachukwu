###just testing my python skills on random projects"""

Fname = input("enter your first name:")
Lname = input("enter your last name:")

# parent class
class person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lname)

# child class
class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.gradautionyear = year
    def welcome(self):
        print("welcome",self.firstname, self.lastname," to the class of", self.gradautionyear)

x = student(Fname, Lname, 2027)
x.welcome()


