class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Ctor......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def CreatePlayer(cls, name, dob):
        from datetime import date, datetime
        stdt = datetime.strptime(dob, "%d-%m-%Y")
        fdt = str(stdt).split("-")[0]
        ldt = str(date.today()).split("-")[0]
        age = int(ldt) - int(fdt)
        return cls(name, age)




ply1 = Player("Micheal", 38)

print("-" * 60)
ply2 = Player.CreatePlayer("Ruben", "15-10-1985")
ply2.get_details()
