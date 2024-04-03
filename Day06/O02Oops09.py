

class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name is {self.name}\nAge is {self.age}"

ply1 = Player("Kevin", 25)
# ply1.get_details()

print("-" * 60)

print(str(ply1))

print("-" * 60)
print(ply1)     # this will implicitly call the __str__ method
