
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_detials(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    def test(self):
        Player.static_method_2()

    @staticmethod
    def static_method_1(dt1, dt2):
        from datetime import datetime
        print("This is a static method....")
        d1 = datetime.strptime(dt1, "%d-%m-%Y")
        d2 = datetime.strptime(dt2, "%d-%m-%Y")
        d3 = (d2 - d1).days
        print(round(d3 / 365, 2))

    @staticmethod
    def static_method_2():
        print("This is a static method....")

Player.static_method_1("10-10-2021", "01-06-2023")

ply1 = Player("Mike", 28)
ply1.test()
