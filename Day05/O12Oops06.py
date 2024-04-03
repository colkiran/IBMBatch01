
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Rahul", 29)
ply1.get_details()

print("-" * 60)
ply2 = Player("Sehwag", 26)
ply2.get_details()

print("-" * 60)
# self will take the name of the object that called the method
ply2.runs = 150

# objects attributes or instance variable details will be stored in a dictionary __dict__

print(f"ply2 :{ply2.__dict__}")
print(f"ply2 :{ply1.__dict__}")
