

class Employee:

    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C', 'C++', 'dotnet', 'sql Server', 'Angular', 'React']

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __iter__(self):
        return iter(self.tech)

    def __len__(self):
        return len(self.tech)

    def append(self, val):
        return self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, idx, value):
        self.tech[idx] = value

emp1 = Employee("Allen", 53000)
print(emp1)

print("-" * 60)

for e in emp1:
    print(e, end=' ')
print()

print("-" * 60)
print(len(emp1))

print("-" * 60)
emp1.append("python")

print("-" * 60)
for c in emp1:
    print(c, end=" ")
print()

print("-" * 60)
x = emp1[2]
print(f"x :{x}")

print("-" * 60)
emp1[2] = "JAVA"

for c in emp1:
    print(c, end=" ")
print()
