
class Employee:

    def __init__(self, name):
        self.__name = name     # private variable
        self.tech = ['C', 'C++', 'Dotnet', 'Angular', 'React', 'Python']

    def __str__(self):
        return self.__name + " " + ",".join([str(v) for v in self.tech])

emp1 = Employee("Steve")
print(emp1)

print("-" * 60)
# print(emp1.__name)      # accessing the private var
print(f"emp :{emp1.__dict__}")
emp1._Employee__name = "Mark"
print(emp1._Employee__name)
