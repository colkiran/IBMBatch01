
class Animal:

    def eat(self):
        print("animals eat.....")

class Birds(Animal):

    def fly(self):
        print("Birds fly....")


class Chicken(Birds):

    def message(self):
        print("Chickens are breedled for consumption.....")

    def fly(self):
        print("Chickens seldoom fly....")

chick = Chicken()
chick.message()
chick.fly()
chick.eat()



