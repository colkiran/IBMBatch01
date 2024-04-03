
class Player:

    team = "India"          # class attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Iniliazed.....")

    def get_details(self):
        print(F"Name is :{self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 36)
ply1.get_details()

print("-" * 60)
ply2 = Player("Sourav", 35)
ply2.get_details()

print("-" * 60)
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")
print(f"ply2   :{ply2.team}")

print("-" * 60)
Player.team = "MI"
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")
print(f"ply2   :{ply2.team}")

print("-" * 60)
ply2.team = "KKR"
print(f"ply2   :{ply2.team}")
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")

print("-" * 60)
print(ply2.__dict__)            # print all the attributes of ply2