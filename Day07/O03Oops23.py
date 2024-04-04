

class Animal:

    def eat(self):
        print("Animals eat.....")

class Bird(Animal):

    def fly(self):
        print("Birds Fly......")


class Chicken(Bird):

    def disp(self):
        print("Chickens are breeded for consumption......")


chic = Chicken()
chic.eat()

