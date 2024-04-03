
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Iniliazed.....")

    def get_details(self):
        print(F"Name is :{self.name}\nAge is {self.age}")

ply1 = Player("Kevin", 28)
ply1.get_details()

print("-" * 60)
ply2 = Player("Richard", 32)
ply2.get_details()

