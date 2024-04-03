
class Player:

    def __init__(self):
        self.name = "Sachin"
        self.age = 36
        print("Player Initialized.....")

    def getDetails(self):
        print("runs scored.....")
        print(f"name= {self.name}\nage = {self.age}")

ply1 = Player()
ply1.getDetails()

print("-" * 60)
ply2 = Player()
ply2.name = ("Rahul")
ply2.age = 32
ply2.getDetails()


