
class Animal:
    def __init__(self):
        print("Animal Ctor.......")
        self.a = 10

    def eat(self):
        print("Animals eat....")

    def fun(self):
        print("fun method of Animal....")
class Person:

    def __init__(self):
        print("Person Ctor......")

    def talk(self):
        print("Person talks......")

    def fun(self):
        print("fun method of Person....")


class Girl(Person, Animal):
    def __init__(self):
        super().__init__()          # CALLS THE PARENT CLASS
        Animal.__init__(self)

    def fly(self):
        print("Birds fly.......")

tina = Girl()
tina.eat()
tina.fly()
tina.talk()

#-----------------------

tina.fun()



