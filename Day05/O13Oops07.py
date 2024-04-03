
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Ctor......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod            # decorator
    def CreatePlayer(cls, fnm, lnm, age):
        print("Factory....")
        return cls(f"Mr.{fnm} {lnm}", age)        # calls the constructor


ply1 = Player("Kevin", 32)
ply1.get_details()

print("-" * 60)
"""
ply2's name has two parts 
1. first name  = virat
2. last name   = kholi
"""
ply2 = Player.CreatePlayer("Virat", "Kholi", 36)
ply2.get_details()