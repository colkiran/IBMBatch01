
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary

emp1 = Employee("Slater", 35000)
print(emp1)

print("-" * 60)
emp2 = Employee("Jack", 25000)
print(emp2)

print("Arithmetic Operators".center(60, "-"))

# add
print(f"add - {emp1 + emp2}")

# sub
print(f"sub - {emp1 - emp2}")

# multiply
print(f"mul - {emp1 * emp2}")

# div
print(f"div - {emp1 / emp2}")

# floor div
print(f"floor div - {emp1 // emp2}")